[![Live on X](https://img.shields.io/badge/Live-@kirshbot-000000?style=for-the-badge&logo=x)](https://x.com/kirshbot)
[![Powered by OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI%20API-412991?style=for-the-badge&logo=openai)](https://openai.com)
[![Automated with N8N](https://img.shields.io/badge/Automated%20with-N8N-FB6467?style=for-the-badge&logo=n8n)](https://n8n.io)
[![Python](https://img.shields.io/badge/Python-3.x-3776ab?style=for-the-badge&logo=python)](https://www.python.org/)
[![Speech Analysis](https://img.shields.io/badge/Speech-Analysis-00d9ff?style=for-the-badge)](https://github.com/banastas/kirshbot)

# <a href="https://x.com/kirshbot">@kirshbot</a>

<img src="https://github.com/banastas/kirshbot/blob/main/assets/hero-image.fill.size_1248x702.v1755690341.jpg?raw=true">

## Overview

@kirshbot is an AI character agent that embodies the Observer from *Scorpion Monologues*, posting authentic tweets twice daily at 6am and 4pm PT. The bot leverages comprehensive speech pattern analysis from multiple episodes to maintain character consistency and authentic voice delivery.

## Architecture

### Multi-Episode Speech Analysis System
- **Comprehensive Character Profiling**: Analyzes dialogue patterns across all available episodes (`S01E01` through `S01E06`)
- **Speech Pattern Recognition**: Measures speaking pace (120 WPM target), reading level (Grade 4-6), and strategic pause usage
- **Dialogue Repository**: Maintains unique dialogue samples with episode attribution for authentic voice reference

### Intelligent Content Generation
- **Context-Aware Topics**: Curated themes across episodes including empathy inversion, post-human embodiment, militarized command, ethical interrogation, and identity confrontation
- **Time-Based Selection**: Morning posts focus on practical/tactical content, evening posts lean philosophical
- **Anti-Repetition System**: Analyzes recent posts to avoid overused patterns and topic repetition

### Quality Assurance Pipeline
- **Enhanced Voice Validation**: Multi-layered authenticity scoring based on speech patterns, sentence structure, and tone
- **Safety Checks**: Family-friendly content filtering, appropriate length validation, substance verification
- **Character Consistency**: Ensures posts match the measured, strategic communication style observed in source material

## Technical Stack

<img src="https://github.com/banastas/kirshbot/blob/main/assets/kirshbot.png?raw=true">

### N8N Workflow Components
1. **Daily at 6am + 4pm PT** - Scheduled trigger
2. **Fetch Recent Tweets** - Google Sheets integration for history analysis
3. **Analyze Recent Content** - Pattern detection and avoidance rule generation
4. **Fetch Episode Manifest** - Dynamic episode discovery from hosted analysis files
5. **Multi-Episode Data Aggregator** - Parallel fetching of speech analysis data
6. **Enhanced Character Database** - Comprehensive profile building from all episodes
7. **Enhanced Topic Generator** - Context-aware content planning
8. **Enhanced Character AI Agent** - OpenAI-powered content generation with character constraints
9. **Enhanced Voice Validator** - Multi-metric authenticity scoring
10. **Enhanced Safety Check** - Content safety and quality verification
11. **Post to Twitter** - Final posting with success logging

### Data Sources
- **Episode Analysis Files**: Hosted at `https://kirshbot.banast.as/`
  - `analysis_features.json` - Speech metrics, reading level, timing data
  - `analysis_context.json` - Dialogue segments with word-level timestamps  
  - `analysis_flags.txt` - Speech characteristic flags
- **Google Sheets**: Tweet history tracking and analytics
- **Dynamic Manifest**: Auto-discovery of new episodes as they become available

### Speech Analysis Metrics
- **Words Per Minute**: 120 target WPM, ranging 107-137 across episodes
- **Reading Level**: Flesch-Kincaid Grade 4-6 (accessible but authoritative)
- **Pause Patterns**: Short-frequent style with strategic timing
- **Filler Usage**: Minimal (0-3.5 per minute across episodes)
- **Sentence Structure**: Simple clause chains with parataxis and triplets

## Character Voice Characteristics

### Core Traits
- Fatalist anthropologist narrating human ascent and animal law
- Plain, declarative register with wide pitch span (cap ~500 Hz)
- Pattern recognition specialist across different survival contexts
- Measured, strategic communicator who weighs words carefully
- Keen observer of human nature and cosmic purpose

### Speech Patterns
- Simple clause chains with parataxis and triplets (≤1 per tweet)
- Ascent → reversal and definition → inevitabilities rhetoric patterns
- Strategic brevity with maximum impact per word
- Final cadence ending with concrete nouns
- Maintains Grade 4-6 accessibility while demonstrating expertise

### Topic Categories
- **Empathy Inversion**: Post-human embodiment and human ascent then reversal
- **Animal Law**: Predator-prey dynamics and natural order observations
- **Militarized Command**: Authority invocation and tactical delegation
- **Ethical Interrogation**: Moral metaphor and culpability questions
- **Identity Confrontation**: Family vs cosmic purpose and human vs machine
- **Scientific Authority**: Procedural measurements and forensic analysis

## Quality Metrics

### Validation Scoring
- **Speech Pattern Score**: Sentence length, structure, filler usage alignment
- **Authenticity Score**: Tone consistency, plain declarative delivery, natural flow
- **Overall Validation**: Combined score requiring 70%+ for posting approval
- **Safety Score**: Content appropriateness, length guidelines, substance requirements

### Success Criteria
- Character count: 240 characters maximum (without URL)
- Structure variants: Hypothesis → inversion → noun stop, Ascent list → reversal clause → mortality noun
- Forbidden elements: emoji, exclamation marks, hashtags
- Allowed punctuation: periods, commas, colons, semicolons
- Consistent voice across all posting contexts

## Deployment & Monitoring

### Automated Posting
- **Schedule**: Twice daily at 6am and 4pm Pacific Time
- **Retry Logic**: Single retry with fresh topic on validation failure
- **Skip Protection**: Quality control override prevents poor content posting
- **Success Logging**: Comprehensive metrics tracking in Google Sheets

### Analytics Dashboard
- Real-time posting success rates
- Speech pattern adherence metrics
- Topic diversity tracking
- Character authenticity scoring trends
- Safety validation statistics

---

**Disclaimer**: Fan-created content inspired by the Observer from *Scorpion Monologues* with comprehensive speech pattern analysis for authentic character representation.
