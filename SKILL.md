---
name: transcribe-japanese-video
description: Transcribe Japanese YouTube videos and automatically create comprehensive study materials with vocabulary, romaji, translations, and grammar explanations. Use this skill when the user asks to transcribe, analyze, or study Japanese videos.
---

# Japanese YouTube Video Transcriber

Transcribe Japanese YouTube videos and automatically generate comprehensive study materials with AI-powered analysis.

## Quick Start

The simplest way to use this skill:

```
Transcribe this Japanese video: https://www.youtube.com/watch?v=VIDEO_ID
```

Claude will automatically:
1. Download and transcribe the video using Whisper AI
2. Analyze the transcript with AI language understanding
3. Extract vocabulary with timestamps
4. Generate romaji romanization
5. Provide Chinese and English translations
6. Explain grammar patterns
7. Create formatted study materials

## Usage Examples

### Basic Transcription

```
Transcribe this Japanese video: https://www.youtube.com/watch?v=QBhL5VtfXEc
```

### With Context

```
Transcribe this JLPT N5 lesson about family vocabulary: [URL]
```

```
Create study materials from this cooking video: [URL]
```

### With Specific Focus

```
Transcribe this video and focus on verb conjugations: [URL]
```

```
Analyze this video and create Anki-compatible flashcards: [URL]
```

## What You'll Get

### 1. Vocabulary Tables

Organized tables with:
- Japanese (kanji/kana)
- Reading (hiragana)
- Romaji romanization
- Chinese translation (中文)
- English translation
- Video timestamps for reference

Example output:
```markdown
| Japanese | Reading | Romaji | 中文 | English | Timestamp |
|----------|---------|--------|------|---------|-----------|
| 私 | わたし | watashi | 我 | I, me | 30s-58s |
| 家族 | かぞく | kazoku | 家庭 | Family | 366s-378s |
| お母さん | おかあさん | okaasan | 母亲 | Mother | 90s-102s |
```

### 2. Grammar Explanations

- Particles and their functions
- Verb conjugation patterns
- Sentence structures
- Usage notes and context

### 3. Example Sentences

Each sentence includes:
- Japanese text
- Romaji romanization
- Chinese translation
- English translation

### 4. Study Guide

- Organized by topic
- Study recommendations
- Key takeaways

## How It Works

When you ask Claude to transcribe a video:

1. **Claude executes** `python scripts/transcribe.py "URL"`
2. **Script downloads** audio from YouTube using yt-dlp
3. **Whisper AI transcribes** the Japanese audio with timestamps
4. **Claude automatically analyzes** the transcript using AI language understanding to:
   - Identify important vocabulary
   - Generate accurate romaji
   - Provide context-aware translations
   - Explain grammar patterns
   - Organize into study materials
5. **Claude presents** beautifully formatted results ready to use

## Advanced Options

### Manual Script Usage

You can also run the script directly:

```bash
python scripts/transcribe.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Options:
- `-o` or `--output`: Specify output directory (default: /mnt/user-data/outputs)
- `-n` or `--name`: Lesson name for file naming

Example:
```bash
python scripts/transcribe.py "URL" -o /custom/path -n "lesson1"
```

### Multiple Videos

```
Transcribe these 3 videos and combine the vocabulary:
1. [URL1]
2. [URL2]
3. [URL3]
```

### Custom Formats

```
Transcribe this video and format as CSV for import into spreadsheet: [URL]
```

## Time Savings

**Traditional approach:**
- Manual transcription: 30-60 minutes
- Vocabulary extraction: 60-90 minutes
- Dictionary lookups: 60-90 minutes
- Romaji generation: 30 minutes
- Formatting: 30 minutes
- **Total: 3.5-5 hours**

**With this skill:**
- You ask Claude: 30 seconds
- Transcription: 5 minutes
- AI analysis: 2 minutes
- **Total: ~7 minutes**

**Time saved: ~4 hours per video! ⚡**

## Requirements

The script automatically installs dependencies if needed:
- Python 3.8+
- yt-dlp (YouTube downloader)
- openai-whisper (speech-to-text)
- ffmpeg (system package)

On macOS, install ffmpeg:
```bash
brew install ffmpeg
```

## Important Notes

- Transcription accuracy depends on audio quality
- Longer videos take more time to process (~2-5 minutes for 10-minute video)
- First run downloads the Whisper model (~150MB for base model)
- Files are saved to `/mnt/user-data/outputs/` by default
- The skill works best with clear Japanese speech (lessons, tutorials, vlogs)

## Pro Tips

1. **Specify the level**: "This is an N5 lesson" helps Claude focus on appropriate vocabulary
2. **Mention the topic**: "This video is about cooking" helps with context
3. **Request specific formats**: Ask for Anki cards, CSV, or other formats
4. **Use timestamps**: The generated timestamps let you review specific parts of the video
5. **Combine videos**: Ask Claude to analyze multiple videos and create combined study materials

---

**Transform Japanese YouTube videos into comprehensive study materials - automatically!**
