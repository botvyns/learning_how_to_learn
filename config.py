import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path(os.getenv("DATA_DIR", "data"))
AUDIO_DIR = Path(os.getenv("AUDIO_DIR", DATA_DIR / "audio"))
TRANSCRIPTS_DIR = Path(os.getenv("TRANSCRIPTS_DIR", DATA_DIR / "transcripts"))
SUMMARY_FILE = Path(os.getenv("SUMMARY_FILE", DATA_DIR / "transcription.md"))
YOUTUBE_URL = os.getenv('YOUTUBE_URL')

for directory in [DATA_DIR, AUDIO_DIR, TRANSCRIPTS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

WHISPER_MODEL = os.getenv('WHISPER_MODEL', 'tiny')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'llama3.2')
