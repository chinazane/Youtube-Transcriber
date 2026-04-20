# Japanese YouTube Video Transcriber

🎌 A Python tool for transcribing Japanese YouTube videos and creating study materials with romaji and Chinese translations.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- 🎥 **Automatic audio download** from YouTube videos
- 🎤 **High-quality transcription** using OpenAI Whisper
- ⏱️ **Timestamped segments** for easy video reference
- 📝 **Study material templates** with romaji and Chinese translation placeholders
- 🎴 **Flashcard generation** for vocabulary review
- 📚 **Comprehensive study guides** with grammar notes

## Quick Start

### Installation

1. Clone this repository:
```bash
git clone https://github.com/chinazane/japanese-youtube-transcriber.git
cd japanese-youtube-transcriber
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

**Basic usage:**
```bash
python transcribe-jp-video.py <youtube-url>
```

**With lesson name:**
```bash
python transcribe-jp-video.py <youtube-url> lesson1
```

**Specify output directory:**
```bash
python transcribe-jp-video.py <youtube-url> lesson1 ~/Documents/Japanese
```

### Examples

**Example 1: Transcribe a Japanese N5 vocabulary video**
```bash
python transcribe-jp-video.py "https://www.youtube.com/watch?v=QBhL5VtfXEc" "n5-lesson1"
```

**Output:**
- `youtube_n5-lesson1_transcript.txt` - Full transcript with timestamps
- `youtube_n5-lesson1_flashcards.txt` - Flashcard template
- `youtube_n5-lesson1_review.md` - Study guide template

## Output Files

### 1. Transcript (`*_transcript.txt`)
Raw transcription with timestamped segments

### 2. Flashcards (`*_flashcards.txt`)
Vocabulary flashcard template with romaji and Chinese

### 3. Review Guide (`*_review.md`)
Comprehensive study material with vocabulary tables and grammar notes

## Requirements

- Python 3.8 or higher
- yt-dlp
- openai-whisper
- ffmpeg

Install all dependencies:
```bash
pip install -r requirements.txt
```

## License

MIT License - see LICENSE file for details

## Author

Created by [@chinazane](https://github.com/chinazane)

---

**Happy Learning! 🎌 頑張ってください！**
