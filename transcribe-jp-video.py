#!/usr/bin/env python3
"""
Japanese YouTube Video Transcription Tool
Extracts vocabulary and creates study materials with romaji and Chinese translations
"""

import os
import sys
import whisper
import subprocess
import re
from pathlib import Path


def download_audio(youtube_url, output_dir=".", lesson_name=""):
    """Download audio from YouTube video"""
    print("📥 Downloading audio from YouTube...")

    if lesson_name:
        output_template = f"youtube_{lesson_name}_%(title)s.%(ext)s"
    else:
        output_template = "youtube_audio_%(title)s.%(ext)s"

    cmd = [
        "yt-dlp",
        "-x",
        "--audio-format", "mp3",
        "-o", os.path.join(output_dir, output_template),
        youtube_url
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    # Find the downloaded file
    for line in result.stdout.split('\n'):
        if 'Destination:' in line or 'ExtractAudio' in line:
            match = re.search(r'youtube_.*?\.mp3', line)
            if match:
                return os.path.join(output_dir, match.group())

    # Fallback: find the most recent mp3 file
    mp3_files = list(Path(output_dir).glob("youtube_*.mp3"))
    if mp3_files:
        return str(max(mp3_files, key=lambda p: p.stat().st_mtime))

    raise FileNotFoundError("Could not find downloaded audio file")


def transcribe_audio(audio_file):
    """Transcribe audio using Whisper"""
    print("🎤 Transcribing audio with Whisper AI...")
    print("   (This may take a few minutes...)")

    model = whisper.load_model("base")
    result = model.transcribe(audio_file, language="ja", task="transcribe")

    return result


def get_video_info(youtube_url):
    """Get video metadata"""
    cmd = [
        "yt-dlp",
        "--print", "%(title)s",
        youtube_url
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()


def save_transcript(result, output_file, video_title, youtube_url):
    """Save raw transcript with timestamps"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Video: {video_title}\n")
        f.write(f"URL: {youtube_url}\n")
        f.write(f"\n{'=' * 60}\n\n")
        f.write(result["text"])
        f.write(f"\n\n{'=' * 60}\n\nDetailed Segments:\n\n")
        for segment in result["segments"]:
            f.write(f"[{segment['start']:.2f}s - {segment['end']:.2f}s] {segment['text']}\n")


def create_flashcards_template(video_title, youtube_url, output_file):
    """Create a template flashcard file"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# Japanese Vocabulary Flashcards\n")
        f.write(f"# Video: {video_title}\n")
        f.write(f"# URL: {youtube_url}\n")
        f.write(f"# Format: 日本語 (hiragana / romaji) → 中文 | English\n\n")
        f.write("## Vocabulary\n\n")
        f.write("# TODO: Add vocabulary items in this format:\n")
        f.write("# 単語 (たんご / tango) → 词汇 | Vocabulary\n\n")
        f.write("---\n")
        f.write("**格式说明**: 日本語 (平假名 / 罗马音) → 中文 | English\n")


def create_review_template(video_title, youtube_url, output_file):
    """Create a template review guide"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# {video_title}\n\n")
        f.write(f"**Video URL**: {youtube_url}\n\n")
        f.write("---\n\n")
        f.write("## Vocabulary List\n\n")
        f.write("| Japanese | Reading | Romaji | 中文 | English | Timestamp |\n")
        f.write("|----------|---------|--------|------|---------|-----------||\n")
        f.write("| TODO | TODO | TODO | TODO | TODO | TODO |\n\n")
        f.write("---\n\n")
        f.write("## Grammar Points\n\n")
        f.write("TODO: Add grammar explanations\n\n")
        f.write("---\n\n")
        f.write("## Study Tips\n\n")
        f.write("TODO: Add study tips\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: transcribe-jp-video <youtube-url> [lesson-name] [output-dir]")
        print("\nExample:")
        print("  transcribe-jp-video https://www.youtube.com/watch?v=QBhL5VtfXEc")
        print("  transcribe-jp-video https://www.youtube.com/watch?v=QBhL5VtfXEc lesson2")
        print("  transcribe-jp-video https://www.youtube.com/watch?v=QBhL5VtfXEc lesson2 ~/Desktop")
        sys.exit(1)

    youtube_url = sys.argv[1]
    lesson_name = sys.argv[2] if len(sys.argv) > 2 else ""
    output_dir = sys.argv[3] if len(sys.argv) > 3 else os.path.expanduser("~/Desktop")

    print("=" * 60)
    print("Japanese YouTube Video Transcription Tool")
    print("=" * 60)
    print()

    # Get video info
    video_title = get_video_info(youtube_url)
    print(f"📹 Video: {video_title}")
    print(f"🔗 URL: {youtube_url}")
    print()

    # Download audio
    audio_file = download_audio(youtube_url, output_dir, lesson_name)
    print(f"✅ Audio downloaded: {audio_file}")
    print()

    # Transcribe
    result = transcribe_audio(audio_file)
    print("✅ Transcription complete!")
    print()

    # Save files
    base_name = f"youtube_{lesson_name}_" if lesson_name else "youtube_"

    transcript_file = os.path.join(output_dir, f"{base_name}transcript.txt")
    flashcards_file = os.path.join(output_dir, f"{base_name}flashcards.txt")
    review_file = os.path.join(output_dir, f"{base_name}review.md")

    save_transcript(result, transcript_file, video_title, youtube_url)
    create_flashcards_template(video_title, youtube_url, flashcards_file)
    create_review_template(video_title, youtube_url, review_file)

    print("📁 Files created:")
    print(f"   📝 Transcript: {transcript_file}")
    print(f"   🎴 Flashcards: {flashcards_file}")
    print(f"   📚 Review: {review_file}")
    print()

    print("=" * 60)
    print("✅ Done!")
    print()
    print("💡 Next steps:")
    print("   1. Review the transcript to identify vocabulary")
    print("   2. Fill in the flashcards template with romaji and Chinese")
    print("   3. Complete the review guide with grammar notes")
    print("=" * 60)


if __name__ == "__main__":
    main()
