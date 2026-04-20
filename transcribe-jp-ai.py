#!/usr/bin/env python3
"""
AI-Powered Japanese YouTube Video Transcriber
Integrates with Claude AI for intelligent vocabulary extraction and analysis
"""

import os
import sys
import json
import whisper
import subprocess
import re
from pathlib import Path


class YouTubeTranscriber:
    """AI-powered YouTube transcriber with Claude integration"""

    def __init__(self, output_dir="~/Desktop"):
        self.output_dir = os.path.expanduser(output_dir)
        os.makedirs(self.output_dir, exist_ok=True)

    def download_audio(self, youtube_url, lesson_name=""):
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
            "-o", os.path.join(self.output_dir, output_template),
            youtube_url
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        # Find the downloaded file
        mp3_files = list(Path(self.output_dir).glob(f"youtube*{lesson_name}*.mp3"))
        if mp3_files:
            return str(max(mp3_files, key=lambda p: p.stat().st_mtime))

        raise FileNotFoundError("Could not find downloaded audio file")

    def transcribe_audio(self, audio_file):
        """Transcribe audio using Whisper"""
        print("🎤 Transcribing audio with Whisper AI...")
        print("   (This may take a few minutes...)")

        model = whisper.load_model("base")
        result = model.transcribe(audio_file, language="ja", task="transcribe")

        return result

    def get_video_info(self, youtube_url):
        """Get video metadata"""
        cmd = ["yt-dlp", "--print", "%(title)s", youtube_url]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip()

    def save_transcript(self, result, output_file, video_title, youtube_url):
        """Save raw transcript with timestamps"""
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"Video: {video_title}\n")
            f.write(f"URL: {youtube_url}\n")
            f.write(f"\n{'=' * 60}\n\n")
            f.write("FULL TRANSCRIPT:\n")
            f.write(result["text"])
            f.write(f"\n\n{'=' * 60}\n\nDETAILED SEGMENTS:\n\n")
            for segment in result["segments"]:
                f.write(f"[{segment['start']:.2f}s - {segment['end']:.2f}s] {segment['text']}\n")

        return result["text"], result["segments"]

    def create_claude_prompt(self, video_title, transcript_text, segments):
        """Create a prompt for Claude to analyze the transcript"""
        prompt = f"""Analyze this Japanese language learning video transcript and create comprehensive study materials.

Video Title: {video_title}

Transcript:
{transcript_text}

Please create:

1. **Vocabulary List**: Extract all important vocabulary from the transcript. For each word provide:
   - Japanese (kanji/kana)
   - Reading (hiragana)
   - Romaji (Roman spelling)
   - Chinese translation (中文)
   - English translation
   - Category (e.g., Personal Pronouns, Family, Verbs, etc.)

2. **Grammar Points**: Identify and explain key grammar patterns used in the video

3. **Example Sentences**: Show 3-5 example sentences with:
   - Japanese
   - Romaji
   - Chinese translation
   - English translation

4. **Study Tips**: Provide specific tips for learning this material

Format everything in clean Markdown with tables for vocabulary.

Use this format for vocabulary tables:

| Japanese | Reading | Romaji | 中文 | English | Timestamp |
|----------|---------|--------|------|---------|-----------|
| ... | ... | ... | ... | ... | ... |

Make sure EVERY Japanese word has proper romaji romanization.
"""
        return prompt

    def save_claude_instructions(self, prompt_file, prompt):
        """Save the Claude prompt to a file"""
        with open(prompt_file, "w", encoding="utf-8") as f:
            f.write("# Instructions for Claude AI\n\n")
            f.write("Please analyze the transcript and create study materials.\n\n")
            f.write("---\n\n")
            f.write(prompt)

    def process_video(self, youtube_url, lesson_name=""):
        """Main processing pipeline"""
        print("=" * 60)
        print("AI-Powered Japanese YouTube Video Transcriber")
        print("=" * 60)
        print()

        # Get video info
        video_title = self.get_video_info(youtube_url)
        print(f"📹 Video: {video_title}")
        print(f"🔗 URL: {youtube_url}")
        print()

        # Download audio
        audio_file = self.download_audio(youtube_url, lesson_name)
        print(f"✅ Audio downloaded: {audio_file}")
        print()

        # Transcribe
        result = self.transcribe_audio(audio_file)
        print("✅ Transcription complete!")
        print()

        # Save files
        base_name = f"youtube_{lesson_name}_" if lesson_name else "youtube_"

        transcript_file = os.path.join(self.output_dir, f"{base_name}transcript.txt")
        claude_prompt_file = os.path.join(self.output_dir, f"{base_name}claude_prompt.md")

        # Save transcript
        transcript_text, segments = self.save_transcript(
            result, transcript_file, video_title, youtube_url
        )

        # Create Claude analysis prompt
        claude_prompt = self.create_claude_prompt(video_title, transcript_text, segments)
        self.save_claude_instructions(claude_prompt_file, claude_prompt)

        print("📁 Files created:")
        print(f"   📝 Transcript: {transcript_file}")
        print(f"   🤖 Claude Prompt: {claude_prompt_file}")
        print()

        print("=" * 60)
        print("✅ Transcription Complete!")
        print("=" * 60)
        print()
        print("🤖 NEXT STEP: Claude AI Analysis")
        print()
        print("To generate study materials with Claude AI:")
        print(f"1. Open the Claude prompt file: {claude_prompt_file}")
        print("2. Copy the content")
        print("3. Paste into Claude Code")
        print("4. Claude will generate:")
        print("   • Vocabulary list with romaji and translations")
        print("   • Grammar explanations")
        print("   • Example sentences")
        print("   • Study tips")
        print()
        print("Or simply ask Claude:")
        print(f'   "Please analyze the transcript at {transcript_file}"')
        print()
        print("=" * 60)

        return transcript_file, claude_prompt_file


def main():
    if len(sys.argv) < 2:
        print("Usage: transcribe-jp <youtube-url> [lesson-name] [output-dir]")
        print("\nExample:")
        print("  transcribe-jp https://www.youtube.com/watch?v=QBhL5VtfXEc")
        print("  transcribe-jp https://www.youtube.com/watch?v=QBhL5VtfXEc lesson1")
        print("  transcribe-jp https://www.youtube.com/watch?v=QBhL5VtfXEc lesson1 ~/Documents")
        sys.exit(1)

    youtube_url = sys.argv[1]
    lesson_name = sys.argv[2] if len(sys.argv) > 2 else ""
    output_dir = sys.argv[3] if len(sys.argv) > 3 else "~/Desktop"

    transcriber = YouTubeTranscriber(output_dir)
    transcriber.process_video(youtube_url, lesson_name)


if __name__ == "__main__":
    main()
