#!/bin/bash
# Japanese YouTube Video Transcription Skill
# Wrapper script for easy command-line usage

SCRIPT_DIR="$HOME/.claude/skills"
PYTHON_SCRIPT="$SCRIPT_DIR/transcribe-jp-video.py"

if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: transcribe-jp-video.py not found at $PYTHON_SCRIPT"
    exit 1
fi

# Check dependencies
if ! command -v yt-dlp &> /dev/null; then
    echo "Error: yt-dlp is not installed"
    echo "Install with: pip3 install yt-dlp"
    exit 1
fi

if ! python3 -c "import whisper" 2>/dev/null; then
    echo "Error: openai-whisper is not installed"
    echo "Install with: pip3 install openai-whisper"
    exit 1
fi

# Run the Python script
python3 "$PYTHON_SCRIPT" "$@"
