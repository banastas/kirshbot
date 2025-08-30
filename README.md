# @kirshbot

<img src="https://kirshbot.banast.as/assets/hero-image.fill.size_1248x702.v1755690341.jpg" alt="Kirshbot Hero Image">

An AI character bot that authentically recreates the voice and personality of Kirsh from "Alien: Earth" using advanced speech analysis and natural language processing.

## Project Overview

@kirshbot is a sophisticated character AI that analyzes actual dialogue from the TV series to understand and replicate Kirsh's unique speaking patterns, personality traits, and communication style. The bot uses real speech data to generate authentic social media content that stays true to the character's voice.

## Key Features

### Advanced Speech Analysis
- **Real-time Voice Processing**: Analyzes actual dialogue from episodes using librosa and webrtcvad
- **Speaking Pattern Recognition**: Measures WPM, pause patterns, sentence structure, and vocal characteristics
- **Authenticity Scoring**: Validates generated content against actual speech patterns
- **Multi-episode Support**: Can analyze and switch between different episodes for variety

### Character Intelligence
- **Personality Modeling**: Deep character profiling based on actual dialogue samples
- **Context-aware Posting**: Adapts content based on time of day and situational context
- **Speech Pattern Matching**: Ensures generated text matches character's measured speaking pace (107.6 WPM)
- **Understated Voice**: Maintains Kirsh's characteristic dry, matter-of-fact delivery style

### Quality Control
- **Multi-layer Validation**: Speech pattern validation, authenticity scoring, and safety checks
- **Content Filtering**: Prevents harmful, inappropriate, or out-of-character content
- **Automated Logging**: Comprehensive tracking of performance metrics and posting history

### Automated Workflows
- **Scheduled Posting**: Automated tweets at 6am and 4pm PT
- **Dynamic Episode Selection**: Randomly selects episodes if no new content is available for 8+ days
- **Fallback Systems**: Robust error handling and default configurations

## Technical Architecture

### Speech Analysis Pipeline
```
Audio Input → Whisper Transcription → Speech Analysis → Character Modeling → Content Generation
```

### Core Components
- **Speech Analyzer**: Python script using librosa, webrtcvad, and spaCy
- **Character Database**: Dynamic character profiling with speech pattern integration
- **Content Generator**: OpenAI-powered agent with character-specific prompting
- **Validation System**: Multi-stage authenticity and safety validation
- **Automation Framework**: n8n workflow for scheduling and orchestration

## Project Structure

```
kirshbot/
├── S01E01/                          # Episode-specific analysis
│   ├── analyze_whisper_output.py    # Speech analysis script
│   ├── analysis_features.json       # Extracted speech features
│   ├── analysis_segments.json       # Segmented dialogue data
│   ├── analysis_context.json        # Complete episode context
│   ├── analysis_flags.txt           # Speech pattern flags
│   └── S01E01_16k.json              # Whisper transcription
├── manifest.json                    # Episode manifest and metadata
└── README.md                        # Project documentation
```

## Speech Analysis Features

### Measured Characteristics
- **Speaking Pace**: 107.6 WPM overall, 125.4 WPM articulation rate
- **Pause Patterns**: 76 pauses with 0.23s average duration
- **Language Complexity**: Grade 4.24 reading level (accessible language)
- **Filler Usage**: Minimal at 0.5 per minute
- **Sentence Structure**: Average 7.2 words per sentence

### Voice Authenticity Metrics
- **Speech Pattern Score**: Validates sentence length and language complexity
- **Authenticity Score**: Checks for understated delivery and appropriate brevity
- **Overall Validation**: Combined score ensuring character consistency

## Getting Started

### Prerequisites
```bash
# Python dependencies
pip install librosa soundfile webrtcvad spacy numpy
python -m spacy download en_core_web_sm

# Optional for enhanced analysis
pip install papaparse  # For CSV processing if needed
```

### Speech Analysis Usage
```bash
python analyze_whisper_output.py \
  --audio S01E01_16k.wav \
  --json S01E01_16k.json \
  --out_prefix analysis
```

This generates:
- `analysis_features.json` - Quantified speech metrics
- `analysis_segments.json` - Timestamped dialogue segments  
- `analysis_context.json` - Complete episode analysis
- `analysis_flags.txt` - Speech pattern classifications

### Character Profile Integration
The system automatically processes speech analysis data to create enhanced character profiles including:
- Real dialogue samples from episodes
- Measured speaking characteristics
- Personality trait modeling
- Context-appropriate content generation

## Content Generation Examples

### Character Voice Samples
Based on actual dialogue analysis:
- *"What if, while I'm squashing it, another scorpion stings me to protect its friend?"*
- *"Think of how the scorpion must feel, trapped under glass, menaced by giants."*
- *"She's not human anymore. Why are we pretending she is?"*

### Generated Content Style
- **Measured Pace**: Reflects 107.6 WPM speaking rate in text structure
- **Strategic Pauses**: Uses punctuation to mirror speech patterns
- **Simple Language**: Maintains Grade 4.24 reading level
- **Understated Delivery**: Avoids excessive enthusiasm or overwording

## Quality Metrics

### Validation Thresholds
- **Speech Pattern Matching**: ≥70% similarity to analyzed patterns
- **Authenticity Score**: ≥70% character consistency
- **Safety Score**: ≥90% content appropriateness
- **Character Count**: ≤280 characters for platform compliance

### Performance Tracking
- Comprehensive logging of all posts and validation scores
- Episode usage tracking and rotation
- Speech analysis version control
- Automated quality reporting

## Configuration

### Episode Management
```json
{
  "latest_episode": "S01E01",
  "episodes": [
    {
      "episode_id": "S01E01",
      "analyzed": true,
      "speech_data_available": true
    }
  ],
  "updated_at": "2025-01-XX"
}
```

### Speech Analysis Flags
- `slow_overall`: Indicates measured, deliberate speaking pace
- `high_fillers`: Detects excessive filler usage (rarely triggered for Kirsh)
- `long_pauses`: Identifies strategic pause usage
- `monotone_pitch_loud_variance`: Advanced vocal pattern analysis

## Automation Workflow

### Posting Schedule
- **6:00 AM PT**: Morning practical wisdom and survival advice
- **4:00 PM PT**: Afternoon philosophical observations and understated insights

### Content Categorization
- **Survival Wisdom**: Backup plans, preparation, adaptation
- **Philosophical Observations**: Humanity, evolution, cycles of life
- **Practical Advice**: Problem-solving, communication, decision-making
- **Understated Wisdom**: Leadership insights, strategic silence

## Advanced Features

### Dynamic Episode Selection
- Uses latest episode when available
- Falls back to random selection after 8 days without updates
- Maintains variety while preserving character consistency

### Multi-layered Safety
- Content filtering for harmful or inappropriate material
- Character consistency validation
- Platform compliance checking
- Family-friendly content assurance

### Comprehensive Logging
- Google Sheets integration for performance tracking
- Detailed metrics on speech pattern adherence
- Success/failure analysis with improvement recommendations
- Version control for analysis algorithms

## Technical Requirements

### Core Dependencies
- **Python 3.8+**: Core speech analysis
- **librosa**: Audio processing and feature extraction
- **webrtcvad**: Voice activity detection
- **spaCy**: Natural language processing
- **OpenAI API**: Content generation
- **n8n**: Workflow automation

### External Services
- **Twitter API**: Social media posting
- **Google Sheets API**: Logging and analytics
- **File hosting**: Speech analysis data distribution

## License & Usage

This is a fan-created project inspired by "Alien: Earth". All character references and dialogue samples are used for educational and entertainment purposes in accordance with fair use principles.

---

**Follow [@kirshbot](https://x.com/kirshbot)** for authentic character AI content powered by advanced speech analysis.
