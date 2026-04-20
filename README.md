# Japanese YouTube Transcriber - AI Skill 🎌🤖

An intelligent Claude AI skill for transcribing Japanese YouTube videos and automatically generating comprehensive study materials.

[![AI Powered](https://img.shields.io/badge/AI-Claude%20Powered-blueviolet)](https://www.anthropic.com)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## ⚡ What Makes This Special

This is **NOT just a Python script** - it's an **AI-powered skill** for Claude Code that automatically:

✅ Transcribes Japanese videos  
✅ **Extracts vocabulary automatically** using AI  
✅ **Generates romaji** intelligently  
✅ **Provides translations** (Chinese + English)  
✅ **Explains grammar patterns**  
✅ **Creates formatted study materials**  

**All in ONE step** - just ask Claude!

---

## 🚀 Quick Start

### For Claude Code Users (Recommended)

1. **Install the skill**:
```bash
# Clone to your Claude skills directory
git clone https://github.com/chinazane/Youtube-Transcriber.git ~/.claude/skills/transcribe-jp-video

# Install dependencies
cd ~/.claude/skills/transcribe-jp-video
pip install -r requirements.txt
```

2. **Use with Claude**:
```
Just ask Claude:
"Transcribe this Japanese video: https://www.youtube.com/watch?v=VIDEO_ID"

Claude will automatically handle everything!
```

---

### For Standalone Use

```bash
# Clone anywhere
git clone https://github.com/chinazane/Youtube-Transcriber.git
cd Youtube-Transcriber

# Install dependencies
pip install -r requirements.txt

# Run transcription
python transcribe.py <youtube-url> [lesson-name]
```

Then ask Claude to analyze the generated transcript.

---

## 💡 How It Works

### Traditional Approach:
```
1. Run Python script manually
2. Get transcript file
3. Copy transcript to Claude
4. Ask Claude to analyze
5. Wait for Claude to extract vocabulary
6. Wait for Claude to generate romaji
7. Format results manually

Time: 15-20 minutes of manual work
```

### AI Skill Approach:
```
1. Ask Claude: "Transcribe this video: [URL]"

Claude automatically:
- Runs transcription
- Analyzes content
- Extracts vocabulary
- Generates romaji
- Creates translations
- Formats study materials
- Presents results

Time: 30 seconds + 5 min processing = Done!
```

**Time Saved: ~15 minutes per video**

---

## 📖 Example Usage

### With Claude Code (AI Skill)

**You**:
```
Transcribe this Japanese N5 lesson:
https://www.youtube.com/watch?v=QBhL5VtfXEc
```

**Claude**:
```
I'll transcribe and analyze that for you!

[Transcribing...]
✅ Video: 日语 N5 词汇 Lesson 1【家族・人】①

Here are your study materials:

## Vocabulary

| Japanese | Reading | Romaji | 中文 | English | Timestamp |
|----------|---------|--------|------|---------|-----------|
| 私 | わたし | watashi | 我 | I, me | 30s-58s |
| あなた | あなた | anata | 你 | You | 58s-68s |
| 彼 | かれ | kare | 他 | He | 68s-84s |
| 彼女 | かのじょ | kanojo | 她 | She | 84s-90s |
| お母さん | おかあさん | okaasan | 母亲 | Mother | 90s-102s |
...

## Grammar Points

### Personal Pronouns
The lesson covers basic Japanese personal pronouns...

### Family Terms - Polite vs Plain
Japanese has different forms for family terms...

## Study Tips
1. Practice the polite/plain distinction
2. Use timestamps to review specific vocabulary
3. Focus on the お〜さん pattern for polite forms

[Complete, formatted study materials ready to use!]
```

---

### Standalone Use

```bash
python transcribe.py "https://www.youtube.com/watch?v=QBhL5VtfXEc" "n5-lesson1"
```

Output:
```
📥 Downloading audio...
✅ Audio downloaded
🎤 Transcribing with Whisper AI...
✅ Transcription complete!

📁 Files created:
   📝 youtube_n5-lesson1_transcript.txt
   
{
  "video_title": "日语 N5 词汇 Lesson 1【家族・人】①",
  "youtube_url": "https://www.youtube.com/watch?v=QBhL5VtfXEc",
  "transcript_text": "みなさんこんにちは...",
  "segments": [...]
}
```

Then paste the transcript into Claude for analysis.

---

## 🎯 Features

### Automatic Transcription
- Downloads audio from YouTube automatically
- Uses OpenAI Whisper for high-quality Japanese transcription
- Generates timestamped segments for easy video reference

### AI-Powered Analysis (Claude)
- **Vocabulary Extraction**: Claude identifies important words automatically
- **Romaji Generation**: AI-generated romanization (handles special readings)
- **Smart Translation**: Context-aware Chinese and English translations
- **Grammar Analysis**: Identifies and explains patterns used
- **Study Tips**: Personalized learning recommendations

### Formatted Output
- Beautiful markdown tables
- Ready-to-use flashcards
- Organized by topic
- Includes timestamps for video reference

---

## 📦 What's Included

```
Youtube-Transcriber/
├── skill.md              # AI skill documentation
├── transcribe.py         # Transcription script
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── LICENSE              # MIT License
└── examples/            # Sample outputs
    ├── sample_transcript.txt
    ├── sample_flashcards.txt
    └── sample_review.md
```

---

## 🔧 Installation

### Prerequisites

- Python 3.8 or higher
- Claude Code (for AI skill features)
- ffmpeg (for audio processing)

### Install Dependencies

```bash
pip install -r requirements.txt
```

On macOS:
```bash
brew install ffmpeg
```

---

## 📚 Use Cases

### For Language Learners
- Study Japanese from YouTube videos
- Get AI-analyzed vocabulary automatically
- Save hours of manual work

### For Teachers
- Create lesson materials quickly
- Generate consistent study guides
- Focus on teaching, not formatting

### For Content Creators
- Transcribe videos for subtitles
- Create study guides for viewers
- Analyze language usage patterns

---

## 🎓 Advanced Usage

### Specify Lesson Level
```
Transcribe this JLPT N3 lesson: [URL]
```
Claude will focus on N3-level patterns.

### Focus on Specific Topics
```
Transcribe this video and focus on verb conjugations: [URL]
```

### Multiple Videos
```
Transcribe these videos and combine the vocabulary:
1. [URL1]
2. [URL2]
3. [URL3]
```

### Custom Formats
```
Transcribe this video and create Anki-compatible flashcards: [URL]
```

---

## ⏱️ Performance

- **Audio Download**: ~10-30 seconds
- **Transcription**: ~2-5 minutes for 10-minute video
- **AI Analysis** (with Claude): ~1-2 minutes
- **Total Time**: ~7-8 minutes for complete study materials

**vs Manual Approach**: ~2-4 hours

**Time Saved: ~3.5 hours per video!**

---

## 🤖 How the AI Skill Works

When you ask Claude to transcribe a video:

1. **Claude recognizes** the request triggers this skill
2. **Claude executes** the transcription script
3. **Claude reads** the generated transcript
4. **Claude analyzes** using its language understanding:
   - Identifies key vocabulary
   - Generates accurate romaji
   - Provides context-aware translations
   - Explains grammar patterns
   - Creates study recommendations
5. **Claude formats** everything into beautiful tables
6. **Claude presents** complete study materials to you

All automatically - no manual steps!

---

## 🆚 Comparison

| Feature | Manual Script | AI Skill |
|---------|--------------|----------|
| Installation | Anywhere | Claude skills directory |
| Usage | Run Python | Ask Claude |
| Vocabulary | Manual extraction | Auto-extracted |
| Romaji | Manual | AI-generated |
| Translations | Look up manually | AI-provided |
| Grammar | Analyze yourself | AI-explained |
| Time | 15-20 min manual | 30 sec asking |
| Output | Raw data | Formatted materials |

---

## 📖 Documentation

- **Skill Guide**: See [skill.md](skill.md)
- **Examples**: See [examples/](examples/)
- **Requirements**: See [requirements.txt](requirements.txt)

---

## 🤝 Contributing

Contributions welcome!

- 🐛 Report bugs
- 💡 Suggest features  
- 🔧 Submit pull requests
- ⭐ Star the repository

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) - Speech recognition
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube downloading
- [Claude AI](https://www.anthropic.com) - Intelligent analysis
- Japanese language learning community

---

## 💬 Support

- 🐛 **Issues**: https://github.com/chinazane/Youtube-Transcriber/issues
- ⭐ **Star** if you find this helpful!
- 🔗 **Share** with other Japanese learners

---

## 🎯 Quick Links

- **Install as Claude Skill**: `git clone https://github.com/chinazane/Youtube-Transcriber.git ~/.claude/skills/transcribe-jp-video`
- **Standalone Use**: `git clone https://github.com/chinazane/Youtube-Transcriber.git`
- **Documentation**: [skill.md](skill.md)

---

**Transform Japanese YouTube videos into comprehensive study materials with the power of AI!**

**頑張ってください！🎌**

---

*Powered by OpenAI Whisper + Claude AI*
