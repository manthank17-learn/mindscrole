"""
Mindscrole – Phase 2
Complete local transcription pipeline
- Instagram Reel URL
- yt-dlp audio extraction
- Whisper (CPU) transcription
- Save transcript to file
"""

import sys
import subprocess
from pathlib import Path
from datetime import datetime
import whisper


def extract_audio(reel_url: str, output_wav: Path):
    """
    Download audio from Instagram reel and convert to WAV
    """
    print("[INFO] Extracting audio with yt-dlp...")

    cmd = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "wav",
        "--audio-quality", "0",
        "-o", str(output_wav),
        reel_url,
    ]

    subprocess.run(cmd, check=True)
    print("[INFO] Audio extraction complete.")


def transcribe_audio(audio_path: Path) -> str:
    """
    Transcribe audio using Whisper on CPU
    """
    print("[INFO] Loading Whisper model (CPU)...")
    model = whisper.load_model("small", device="cpu")

    print("[INFO] Transcribing audio...")
    result = model.transcribe(str(audio_path))

    print("[INFO] Transcription complete.")
    return result["text"]


def main():
    if len(sys.argv) != 2:
        print("Usage: python transcribe.py <instagram_reel_url>")
        sys.exit(1)

    reel_url = sys.argv[1]
    print(f"[INFO] Reel URL received: {reel_url}")

    base_dir = Path(__file__).parent
    audio_dir = base_dir / "data" / "audio"
    transcript_dir = base_dir / "data" / "transcripts"

    audio_dir.mkdir(parents=True, exist_ok=True)
    transcript_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    audio_path = audio_dir / f"reel_{timestamp}.wav"
    transcript_path = transcript_dir / f"reel_{timestamp}.txt"

    print(f"[INFO] Audio path      : {audio_path}")
    print(f"[INFO] Transcript path : {transcript_path}")

    # Step 1 — extract audio
    extract_audio(reel_url, audio_path)

    # Step 2 — transcribe with Whisper
    transcript_text = transcribe_audio(audio_path)

    # Step 3 — save transcript
    transcript_path.write_text(transcript_text, encoding="utf-8")
    print(f"[INFO] Transcript saved to {transcript_path}")

    print("[SUCCESS] Transcription pipeline completed.")


if __name__ == "__main__":
    main()

