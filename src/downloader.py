import os
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs

import yt_dlp
from pytube import Playlist, YouTube

load_dotenv()

AUDIO_OUTPUT_DIR = os.getenv("AUDIO_DIR")


class Downloader:

    @property
    def ydl_opts(self) -> dict:
        return {
            "format": "bestaudio/best",
            "extract_audio": True,
            "outtmpl": f"{AUDIO_OUTPUT_DIR}/%(title)s.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

    def _get_video_urls_from_playlist(self, url: str) -> list:
        return [video.watch_url for video in Playlist(url).videos]

    def download(self, url: str) -> None:
        query_params = parse_qs(urlparse(url).query)
        watch_urls = self._get_video_urls_from_playlist(url) if "list" in query_params else [YouTube(url).watch_url]
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download(watch_urls)
