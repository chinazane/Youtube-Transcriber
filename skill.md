---
name: transcribe-japanese-video
description: Transcribe Japanese YouTube videos and automatically create comprehensive study materials with vocabulary, romaji, and translations - all powered by Claude AI
version: 3.0.0
---

# Transcribe Japanese Video - AI Skill

When you ask me to transcribe a Japanese YouTube video, I will:

1. **Download and transcribe** the video using Whisper AI
2. **Automatically analyze** the transcript (no separate prompt needed!)
3. **Extract vocabulary** and categorize it intelligently
4. **Generate romaji** for all Japanese text
5. **Provide translations** in Chinese and English
6. **Explain grammar patterns** found in the video
7. **Create formatted study materials** ready to use

## How to Use

Just ask me naturally:

```
Transcribe this Japanese video: https://www.youtube.com/watch?v=VIDEO_ID
```

Or:

```
Create study materials from: [YouTube URL]
```

I'll handle everything automatically!

## What I'll Create For You

### 1. Vocabulary Flashcards
Formatted tables with:
- Japanese (kanji/kana)
- Reading (hiragana)
- Romaji
- Chinese translation (中文)
- English translation
- Timestamps

### 2. Grammar Explanations
- Particles used and their functions
- Verb conjugations
- Sentence patterns
- Cultural context

### 3. Example Sentences
Each with:
- Japanese text
- Romaji romanization
- Chinese translation
- English translation

### 4. Study Guide
- Organized by topic
- Difficulty-appropriate explanations
- Study tips and recommendations

## Example Interaction

**You**: Transcribe this Japanese N5 lesson: https://www.youtube.com/watch?v=QBhL5VtfXEc

**Me**: I'll transcribe and analyze that video for you!

*[I run the transcription script]*
*[I automatically analyze the transcript]*
*[I create formatted study materials]*

Here's what I found in this lesson about family vocabulary:

### Vocabulary

| Japanese | Reading | Romaji | 中文 | English | Timestamp |
|----------|---------|--------|------|---------|-----------|
| 私 | わたし | watashi | 我 | I, me | 30s-58s |
| 家族 | かぞく | kazoku | 家庭 | Family | 366s-378s |
...

### Grammar Points
...

*[Complete formatted study materials]*

## Integration with Claude

This skill is different because:

- ✅ **No manual prompting needed** - I analyze automatically
- ✅ **Real-time generation** - Vocabulary and romaji created instantly  
- ✅ **Context-aware** - I understand the lesson type and adjust
- ✅ **Complete automation** - One command, full study materials
- ✅ **Claude-powered** - Uses my language understanding throughout

## Time Savings

**Without this skill:**
- Transcribe: 5 minutes
- Manual vocabulary extraction: 30-60 minutes
- Look up meanings: 60-90 minutes
- Generate romaji: 30 minutes
- Format everything: 30 minutes
**Total: 2.5-4 hours**

**With this skill:**
- You ask me → 30 seconds
- I transcribe → 5 minutes
- I analyze → 2 minutes  
- I format → instant
**Total: 7-8 minutes**

**Time saved: ~3.5 hours per video!**

## Behind the Scenes

When you invoke this skill, I:

1. Execute the transcription script
2. Read the generated transcript
3. Use my language understanding to:
   - Identify important vocabulary
   - Generate accurate romaji
   - Provide context-appropriate translations
   - Explain grammar patterns
   - Create organized study materials
4. Format everything beautifully
5. Present it to you ready to use

## Requirements

- Python 3.8+
- yt-dlp
- openai-whisper
- Claude AI (that's me!)

## Pro Tips

- Specify the lesson level: "This is an N5 lesson"
- Ask for specific focus: "Focus on verb conjugations"
- Request formats: "Create Anki-compatible flashcards"
- Multiple videos: "Combine vocabulary from these 3 videos"

This is a true AI skill - I do all the intelligent work automatically!
