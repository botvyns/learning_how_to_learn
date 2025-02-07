import whisper
from loguru import logger

import config
from src.downloader import Downloader
from src.summarizer import Summarizer

logger.add("app.log", format="{time} - {level} - {message}", level="INFO")

downloader = Downloader()
summarizer = Summarizer()
transcriber = whisper.load_model(config.WHISPER_MODEL)

downloader.download(config.PLAYLIST_URL)

audio_files = [file for file in config.AUDIO_DIR.iterdir() if file.is_file()]

summaries = []
for audio_path in audio_files:
    logger.info(f"Transcribing: {audio_path}")
    result = transcriber.transcribe(str(audio_path))['text']

    output_file = config.TRANSCRIPTS_DIR / f"{audio_path.stem}.txt"
    output_file.write_text(result, encoding="utf-8")
    logger.info(f"Transcription saved to: {output_file}")

    summary = summarizer.summarize(result)
    summaries.append(summary)

with config.TRANSCRIPTION_FILE.open("a", encoding="utf-8") as f:
    f.writelines(f"{summary}\n" for summary in summaries)
