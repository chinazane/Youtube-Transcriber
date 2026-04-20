#!/bin/bash
# AI-Powered Japanese Video Transcriber - Claude Integration Wrapper

SCRIPT_DIR="$HOME/.claude/skills"
PYTHON_SCRIPT="$SCRIPT_DIR/transcribe-jp.py"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║      AI-Powered Japanese YouTube Video Transcriber            ║${NC}"
echo -e "${BLUE}║      Powered by Whisper AI + Claude AI                        ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check dependencies
if ! command -v yt-dlp &> /dev/null; then
    echo -e "${YELLOW}⚠️  yt-dlp not found. Installing...${NC}"
    pip3 install -q yt-dlp
fi

if ! python3 -c "import whisper" 2>/dev/null; then
    echo -e "${YELLOW}⚠️  openai-whisper not found. Installing...${NC}"
    pip3 install -q openai-whisper
fi

# Run the Python script
python3 "$PYTHON_SCRIPT" "$@"

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✨ Tip: You can now ask Claude to analyze the transcript!${NC}"
    echo -e "${GREEN}   Just say: 'Please analyze the transcript and create study materials'${NC}"
fi

exit $EXIT_CODE
