import json, re, argparse, statistics as stats, pathlib
import numpy as np
import librosa
import soundfile as sf

# Optional VAD and spaCy. Script degrades if unavailable.
try:
    import webrtcvad
    VAD_OK = True
except Exception:
    VAD_OK = False

try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    SPACY_OK = True
except Exception:
    SPACY_OK = False

FILLERS = [
    "uh","um","er","like","you know","kind of","sort of","basically",
    "actually","literally","i mean","so yeah","right","okay","ok"
]

def word_boundary_count(text, phrase):
    pattern = r"\b" + re.escape(phrase) + r"\b"
    return len(re.findall(pattern, text, flags=re.IGNORECASE))

def filler_stats(text):
    counts = {f: word_boundary_count(text, f) for f in FILLERS}
    return {"by_token": counts, "total": int(sum(counts.values()))}

def syllables_in_word(w):
    w = re.sub(r"[^a-z]", "", w.lower())
    if not w:
        return 0
    vowels = "aeiouy"
    groups = 0
    prev = False
    for c in w:
        v = c in vowels
        if v and not prev:
            groups += 1
        prev = v
    if w.endswith("e") and groups > 1:
        groups -= 1
    return max(groups, 1)

def count_syllables(words):
    return sum(syllables_in_word(w) for w in words)

def split_sentences(text):
    if SPACY_OK:
        return [s.text.strip() for s in nlp(text).sents if s.text.strip()]
    parts = re.split(r"[\.!?]\s+", text)
    return [p.strip() for p in parts if p.strip()]

def flesch_kincaid_grade(text):
    sentences = split_sentences(text)
    words = re.findall(r"\b[\w']+\b", text)
    if len(sentences) == 0 or len(words) == 0:
        return {"fk_grade": 0.0, "flesch_reading_ease": 0.0, "words": 0, "sentences": 0, "syllables": 0}
    syllables = count_syllables(words)
    W = len(words)
    S = len(sentences)
    SYL = syllables
    fk = 0.39 * (W / S) + 11.8 * (SYL / W) - 15.59
    fre = 206.835 - 1.015 * (W / S) - 84.6 * (SYL / W)
    return {
        "fk_grade": round(fk, 2),
        "flesch_reading_ease": round(fre, 2),
        "words": W,
        "sentences": S,
        "syllables": SYL
    }

def load_whisper_json(path_json):
    data = json.load(open(path_json, "r", encoding="utf-8"))
    segs = data.get("segments", [])
    for s in segs:
        s.setdefault("words", [])
    full_text = " ".join(s.get("text", "").strip() for s in segs).strip()
    return segs, full_text

def load_audio_safe(path, target_sr=16000):
    # Avoids audioread which imports aifc on Python 3.13
    y, sr = sf.read(path, dtype="float32", always_2d=False)
    if y.ndim == 2:
        y = y.mean(axis=1)
    if sr != target_sr:
        y = librosa.resample(y, orig_sr=sr, target_sr=target_sr)
        sr = target_sr
    return y, sr

def extract_pauses_with_vad(y, sr, frame_ms=30, vad_level=3):
    if not VAD_OK:
        return [], []
    vad = webrtcvad.Vad(vad_level)
    frame_len = int(sr * frame_ms / 1000)
    speech_flags = []
    for i in range(0, len(y) - frame_len, frame_len):
        frame = (y[i:i+frame_len] * 32768.0).astype(np.int16).tobytes()
        speech_flags.append(vad.is_speech(frame, sr))
    times = np.arange(len(speech_flags)) * frame_ms / 1000.0
    pauses = []
    start = None
    for t, flag in zip(times, speech_flags):
        if not flag and start is None:
            start = t
        if flag and start is not None:
            pauses.append((start, t))
            start = None
    if start is not None:
        pauses.append((start, times[-1] + frame_ms / 1000.0))
    speech_spans = []
    start = None
    for t, flag in zip(times, speech_flags):
        if flag and start is None:
            start = t
        if not flag and start is not None:
            speech_spans.append((start, t))
            start = None
    if start is not None:
        speech_spans.append((start, times[-1] + frame_ms / 1000.0))
    return pauses, speech_spans

def extract_energy_pitch(y, sr):
    rms = librosa.feature.rms(y=y, frame_length=2048, hop_length=512)[0]
    S = np.abs(librosa.stft(y, n_fft=2048, hop_length=512))
    pitches, mags = librosa.piptrack(S=S, sr=sr, hop_length=512)
    f0 = pitches[mags.argmax(axis=0), range(mags.shape[1])]
    f0 = f0[f0 > 0]
    return rms, f0

def percentiles(a, ps):
    return {f"p{p}": float(np.percentile(a, p)) for p in ps}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audio", required=True)
    ap.add_argument("--json", required=True)
    ap.add_argument("--out_prefix", default="analysis")
    args = ap.parse_args()

    segs, text = load_whisper_json(args.json)

    y, sr = load_audio_safe(args.audio, target_sr=16000)
    duration = len(y) / sr if sr > 0 else 0.0

    rms, f0 = extract_energy_pitch(y, sr)

    energy_stats = {
        "mean": float(np.mean(rms)),
        "std": float(np.std(rms)),
        **percentiles(rms, [10, 50, 90])
    }

    if f0.size:
        pitch_pcts = {k: round(v, 1) for k, v in percentiles(f0, [10, 50, 90]).items()}
        pitch_stats = {
            "mean_hz": round(float(np.mean(f0)), 1),
            "std_hz": round(float(np.std(f0)), 1),
            **pitch_pcts
        }
    else:
        pitch_stats = {"mean_hz": 0.0, "std_hz": 0.0, "p10": 0.0, "p50": 0.0, "p90": 0.0}

    pauses, speech_spans = extract_pauses_with_vad(y, sr)
    pause_durs = [round(b - a, 3) for a, b in pauses]
    speech_time = sum(max(0.0, b - a) for a, b in speech_spans) if speech_spans else duration

    words = re.findall(r"\b[\w']+\b", text)
    w_total = len(words)
    wpm_overall = (w_total / (duration / 60.0)) if duration > 0 else 0.0
    wpm_articulation = (w_total / (speech_time / 60.0)) if speech_time > 0 else 0.0

    fill = filler_stats(text)
    filler_per_min = (fill["total"] / (duration / 60.0)) if duration > 0 else 0.0

    rl = flesch_kincaid_grade(text)

    seg_table = []
    for s in segs:
        seg_entry = {
            "start": round(float(s.get("start", 0.0)), 2),
            "end": round(float(s.get("end", 0.0)), 2),
            "text": s.get("text", "").strip()
        }
        if isinstance(s.get("words"), list) and s["words"]:
            seg_entry["words"] = [
                {
                    "start": round(float(w.get("start", 0.0)), 2),
                    "end": round(float(w.get("end", 0.0)), 2),
                    "text": w.get("word", "").strip()
                }
                for w in s["words"]
                if w.get("end") is not None and w.get("start") is not None
            ]
        seg_table.append(seg_entry)

    features = {
        "duration_sec": round(duration, 2),
        "speech_time_sec": round(speech_time, 2),
        "segments": len(segs),
        "words": w_total,
        "wpm_overall": round(wpm_overall, 1),
        "wpm_articulation": round(wpm_articulation, 1),
        "fillers_total": int(fill["total"]),
        "fillers_per_min": round(filler_per_min, 2),
        "fillers_by_token": fill["by_token"],
        "pause_count": len(pause_durs),
        "pause_durations_sec": {
            "mean": round(stats.mean(pause_durs), 2) if pause_durs else 0.0,
            "median": round(stats.median(pause_durs), 2) if pause_durs else 0.0,
            "p95": round(float(np.percentile(pause_durs, 95)), 2) if pause_durs else 0.0
        },
        "volume_energy_stats": {k: round(v, 6) for k, v in energy_stats.items()},
        "pitch_stats": pitch_stats,
        "reading_level": rl
    }

    out = pathlib.Path(".")
    (out / f"{args.out_prefix}_transcript.txt").write_text(text, encoding="utf-8")
    json.dump({"segments": seg_table}, open(out / f"{args.out_prefix}_segments.json", "w"), ensure_ascii=False, indent=2)
    json.dump(features, open(out / f"{args.out_prefix}_features.json", "w"), ensure_ascii=False, indent=2)
    context = {"transcript": text, "segments": seg_table, "features": features}
    json.dump(context, open(out / f"{args.out_prefix}_context.json", "w"), ensure_ascii=False, indent=2)

    flags = []
    if features["wpm_overall"] < 110:
        flags.append("slow_overall")
    if features["wpm_overall"] > 190:
        flags.append("fast_overall")
    if features["fillers_per_min"] > 4:
        flags.append("high_fillers")
    if features["pause_durations_sec"]["p95"] > 1.0:
        flags.append("long_pauses")
    if pitch_stats["std_hz"] < 15 and energy_stats["std"] > (energy_stats["mean"] * 0.8):
        flags.append("monotone_pitch_loud_variance")
    (out / f"{args.out_prefix}_flags.txt").write_text("\n".join(flags), encoding="utf-8")

if __name__ == "__main__":
    main()