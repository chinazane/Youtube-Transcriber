#!/usr/bin/env python3
"""
Japanese YouTube Video Transcriber
Transcribes Japanese YouTube videos using Whisper AI and prepares data for Claude analysis.
"""

import argparse
import sys
import subprocess
import json
import os
import tempfile
from pathlib import Path


def check_dependencies():
    """Check if required packages are installed, install if not."""
    try:
        import whisper
    except ImportError:
        print("Installing openai-whisper...")
        subprocess.run([sys.executable, "-m", "pip", "install", "openai-whisper"], check=True)

    try:
        subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Installing yt-dlp...")
        subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp"], check=True)


def get_video_info(url):
    """Get information about the video."""
    result = subprocess.run(
        ["yt-dlp", "--dump-json", "--no-playlist", url],
        capture_output=True,
        text=True,
        check=True
    )
    info = json.loads(result.stdout)
    return info.get("title", "Unknown Title")


def download_audio(url, output_dir):
    """Download audio from YouTube video."""
    print("📥 Downloading audio...")

    # Create temporary file for audio
    audio_file = os.path.join(output_dir, "temp_audio.mp3")

    cmd = [
        "yt-dlp",
        "-x",  # Extract audio
        "--audio-format", "mp3",
        "--audio-quality", "0",  # Best quality
        "-o", audio_file,
        "--no-playlist",
        url
    ]

    subprocess.run(cmd, check=True, capture_output=True)
    print("✅ Audio downloaded")

    return audio_file


def transcribe_audio(audio_file):
    """Transcribe audio using Whisper."""
    print("🎤 Transcribing with Whisper AI...")

    import whisper

    # Load model (base is good for Japanese)
    model = whisper.load_model("base")

    # Transcribe
    result = model.transcribe(audio_file, language="ja", verbose=False)

    print("✅ Transcription complete!")

    return result


def save_transcript(result, output_file, video_title, video_url):
    """Save transcript to file."""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Video: {video_title}\n")
        f.write(f"URL: {video_url}\n")
        f.write("-" * 80 + "\n\n")
        f.write(result["text"])

    return result["text"], result.get("segments", [])


def transcribe_video(url, output_dir="/mnt/user-data/outputs", lesson_name=""):
    """
    Main function to transcribe a YouTube video.

    Args:
        url: YouTube video URL
        output_dir: Directory to save outputs
        lesson_name: Optional lesson name for file naming

    Returns:
        Dictionary with transcript data
    """
    check_dependencies()

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Get video info
    video_title = get_video_info(url)
    print(f"\n📺 Video: {video_title}\n")

    # Download audio
    with tempfile.TemporaryDirectory() as temp_dir:
        audio_file = download_audio(url, temp_dir)

        # Transcribe
        result = transcribe_audio(audio_file)

    # Save transcript
    base_name = f"youtube_{lesson_name}_" if lesson_name else "youtube_"
    transcript_file = os.path.join(output_dir, f"{base_name}transcript.txt")

    transcript_text, segments = save_transcript(result, transcript_file, video_title, url)

    print(f"\n📁 Files created:")
    print(f"   📝 {transcript_file}")

    # Return structured data for Claude to analyze
    return {
        "video_title": video_title,
        "youtube_url": url,
        "transcript_text": transcript_text,
        "segments": [
            {
                "start": seg.get("start", 0),
                "end": seg.get("end", 0),
                "text": seg.get("text", "")
            }
            for seg in segments
        ],
        "transcript_file": transcript_file
    }


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe Japanese YouTube videos using Whisper AI"
    )
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "-o", "--output",
        default="/mnt/user-data/outputs",
        help="Output directory (default: /mnt/user-data/outputs)"
    )
    parser.add_argument(
        "-n", "--name",
        default="",
        help="Lesson name for file naming"
    )

    args = parser.parse_args()

    try:
        result = transcribe_video(args.url, args.output, args.name)
        print("\n" + json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
