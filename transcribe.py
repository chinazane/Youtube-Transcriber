#!/usr/bin/env python3
"""
Integrated AI Skill - Transcribe Japanese Video
This script is called by Claude and returns data that Claude automatically analyzes
"""

import sys
import json
import subprocess
import os
from pathlib import Path

def transcribe_and_prepare_for_claude(youtube_url, lesson_name=""):
    """
    Transcribe video and return transcript in Claude-ready format
    """
    output_dir = os.path.expanduser("~/Desktop")

    # Import the transcription functions
    sys.path.insert(0, os.path.expanduser("~/.claude/skills"))
    from transcribe_jp import YouTubeTranscriber

    transcriber = YouTubeTranscriber(output_dir)

    # Get video info
    video_title = transcriber.get_video_info(youtube_url)

    # Download and transcribe
    audio_file = transcriber.download_audio(youtube_url, lesson_name)
    result = transcriber.transcribe_audio(audio_file)

    # Save transcript
    base_name = f"youtube_{lesson_name}_" if lesson_name else "youtube_"
    transcript_file = os.path.join(output_dir, f"{base_name}transcript.txt")

    transcript_text, segments = transcriber.save_transcript(
        result, transcript_file, video_title, youtube_url
    )

    # Return structured data for Claude to analyze
    return {
        "video_title": video_title,
        "youtube_url": youtube_url,
        "transcript_text": transcript_text,
        "segments": [
            {
                "start": seg["start"],
                "end": seg["end"],
                "text": seg["text"]
            }
            for seg in segments
        ],
        "transcript_file": transcript_file,
        "audio_file": audio_file
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "YouTube URL required"}))
        sys.exit(1)

    youtube_url = sys.argv[1]
    lesson_name = sys.argv[2] if len(sys.argv) > 2 else ""

    try:
        result = transcribe_and_prepare_for_claude(youtube_url, lesson_name)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)
