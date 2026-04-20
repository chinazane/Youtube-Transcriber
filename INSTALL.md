# Installation Guide - AI Skill

## For Claude Code Users (Recommended)

### Step 1: Clone to Claude Skills Directory

```bash
git clone https://github.com/chinazane/Youtube-Transcriber.git ~/.claude/skills/transcribe-jp-video
cd ~/.claude/skills/transcribe-jp-video
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

On macOS, also install ffmpeg:
```bash
brew install ffmpeg
```

### Step 3: Verify Installation

Ask Claude:
```
List my available skills
```

You should see `transcribe-jp-video` or `transcribe-japanese-video` in the list.

### Step 4: Use the Skill

Just ask Claude:
```
Transcribe this Japanese video: https://www.youtube.com/watch?v=QBhL5VtfXEc
```

Claude will automatically:
- Run the transcription
- Analyze the content  
- Create study materials
- Present formatted results

✅ Done! No manual steps needed!

---

## For Standalone Use (Without Claude Code)

### Step 1: Clone Anywhere

```bash
git clone https://github.com/chinazane/Youtube-Transcriber.git
cd Youtube-Transcriber
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Transcription

```bash
python transcribe.py <youtube-url> [lesson-name]
```

Example:
```bash
python transcribe.py "https://www.youtube.com/watch?v=QBhL5VtfXEc" "n5-lesson1"
```

### Step 4: Analyze with Claude

The script outputs JSON with the transcript. Copy the transcript text and ask Claude:

```
Please analyze this Japanese transcript and create study materials with vocabulary tables, romaji, and translations:

[paste transcript here]
```

---

## Troubleshooting

### "yt-dlp not found"
```bash
pip install yt-dlp
```

### "whisper module not found"
```bash
pip install openai-whisper
```

### "ffmpeg not found"
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

### Skill not recognized by Claude

Make sure you installed in the correct directory:
```bash
ls ~/.claude/skills/transcribe-jp-video/
```

You should see:
- skill.md
- transcribe.py
- requirements.txt

---

## Updating

To get the latest version:

```bash
cd ~/.claude/skills/transcribe-jp-video
git pull origin main
pip install -r requirements.txt --upgrade
```

---

## Uninstalling

### Remove AI Skill
```bash
rm -rf ~/.claude/skills/transcribe-jp-video
```

### Remove Dependencies (optional)
```bash
pip uninstall yt-dlp openai-whisper
```

---

**Need help?** Open an issue at: https://github.com/chinazane/Youtube-Transcriber/issues
