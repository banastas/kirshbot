# <a href="https://x.com/kirshbot">@kirshbot</a>

<img src="https://kirshbot.banast.as/assets/hero-image.fill.size_1248x702.v1755690341.jpg">

## Overview

@kirshbot is an AI character agent that embodies Kirsh from *Alien: Earth*, posting authentic tweets twice daily at 6am and 4pm PT. The bot leverages comprehensive speech pattern analysis from multiple episodes to maintain character consistency and authentic voice delivery.

## Architecture

### Multi-Episode Speech Analysis System
- **Comprehensive Character Profiling**: Analyzes dialogue patterns across all available episodes (`S01E01`, `S01E02`, etc.)
- **Speech Pattern Recognition**: Measures speaking pace (~108 WPM), reading level (Grade 4.24), and strategic pause usage
- **Dialogue Repository**: Maintains 25+ unique dialogue samples with episode attribution for authentic voice reference

### Intelligent Content Generation
- **Context-Aware Topics**: 60+ curated topics across 6 categories (survival wisdom, human nature observations, tactical insights, philosophical depth, practical leadership, meta-commentary)
- **Time-Based Selection**: Morning posts focus on practical/tactical content, evening posts lean philosophical
- **Anti-Repetition System**: Analyzes recent posts to avoid overused patterns and topic repetition

### Quality Assurance Pipeline
- **Enhanced Voice Validation**: Multi-layered authenticity scoring based on speech patterns, sentence structure, and tone
- **Safety Checks**: Family-friendly content filtering, appropriate length validation, substance verification
- **Character Consistency**: Ensures posts match the measured, strategic communication style observed in source material

## Technical Stack

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
- **Words Per Minute**: 107.6 overall, 125.4 articulation rate
- **Reading Level**: Flesch-Kincaid Grade 4.24 (accessible but authoritative)
- **Pause Patterns**: 76 strategic pauses, median 0.1s duration
- **Filler Usage**: Minimal (0.5 per minute, primarily "you know")
- **Sentence Structure**: ~8-word average, measured delivery style

## Character Voice Characteristics

### Core Traits
- Accumulated tactical wisdom from proven field experience
- Pattern recognition specialist across different survival contexts
- Measured, strategic communicator who weighs words carefully
- Authority built on demonstrated competence, not position
- Keen observer of human nature under extreme stress

### Speech Patterns
- Strategic brevity with maximum impact per word
- Consistently grounds philosophical observations in practical reality
- References universal patterns without becoming preachy
- Uses concrete examples from diverse scenarios
- Maintains Grade 4+ accessibility while demonstrating expertise

### Topic Categories
- **Survival Wisdom**: Reading warning signs, backup plans, resource allocation
- **Human Nature**: Stress responses, group dynamics, behavioral patterns  
- **Tactical Insights**: Strategic positioning, timing, controlled unpredictability
- **Philosophy**: Cycles, adaptation, evolution, universal truths
- **Leadership**: Authority without position, decision-making under pressure
- **Meta-Commentary**: Expertise visibility, experience vs. records, pattern recognition

## Quality Metrics

### Validation Scoring
- **Speech Pattern Score**: Sentence length, structure, filler usage alignment
- **Authenticity Score**: Tone consistency, understated delivery, natural flow
- **Overall Validation**: Combined score requiring 70%+ for posting approval
- **Safety Score**: Content appropriateness, length guidelines, substance requirements

### Success Criteria
- Character count: 80-240 characters optimal
- Word count: 15-35 words per tweet
- Multiple sentence validation when appropriate
- Strategic pause simulation through punctuation
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

**Disclaimer**: Fan-created content inspired by Kirsh from *Alien: Earth* with comprehensive speech pattern analysis for authentic character representation.
