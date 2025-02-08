import whisper
from loguru import logger

import config
from src.downloader import Downloader
from src.summarizer import Summarizer


def main():
    logger.add("app.log", format="{time} - {level} - {message}", level="INFO")

    downloader = Downloader()
    summarizer = Summarizer()
    transcriber = whisper.load_model(config.WHISPER_MODEL)

    downloader.download(config.YOUTUBE_URL)

    audio_paths = [audio_path for audio_path in config.AUDIO_DIR.iterdir() if audio_path.is_file()]

    summaries = []
    for audio_path in audio_paths:
        logger.info(f"Transcribing: {audio_path}")
        audio_name = audio_path.stem
        transcript = transcriber.transcribe(str(audio_path))["text"]

        output_file = config.TRANSCRIPTS_DIR / f"{audio_name}.txt"
        output_file.write_text(transcript, encoding="utf-8")
        logger.info(f"Transcription saved to: {output_file}")

        summary = summarizer.summarize(transcript)
        full_summary = f"# {audio_name}\n\n{summary}"
        summaries.append(full_summary)

    with config.SUMMARY_FILE.open("w", encoding="utf-8") as f:
        f.writelines(f"{summary}\n\n" for summary in summaries)


if __name__ == "__main__":
    main()
