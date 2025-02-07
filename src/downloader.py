import os
from dotenv import load_dotenv

import yt_dlp
from pytube import Playlist

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

    def _get_video_urls(self, playlist_url: str) -> list:
        return [video.watch_url for video in Playlist(playlist_url).videos]

    def download(self, playlist_url: str) -> None:
        video_urls = self._get_video_urls(playlist_url)
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download(video_urls)
