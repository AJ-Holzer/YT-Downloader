import os
from typing import Any

from yt_dlp import YoutubeDL  # type:ignore[import-untyped]

from env.config import config
from utils.checks import is_playlist_url


class VideoDownloader:
    def __init__(self, download_path: str = config.PATH_DEFAULT_DOWNLOADS) -> None:
        # Define download options
        self._download_options: dict[str, Any] = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "merge_output_format": "mp4",
            "ignoreerrors": True,
            "no_warnings": False,
            "extract_flat": False,
            # Disable all additional downloads
            "writesubtitles": True,
            "writethumbnail": True,
            "writeautomaticsub": True,
            "postprocessors": [
                {
                    "key": "FFmpegVideoConvertor",
                    "preferedformat": "mp4",
                }
            ],
            # Clean up options
            "keepvideo": False,
            "clean_infojson": True,
            # Rate limit: 30 MB/s (30 * 1024 * 1024 bytes)
            "ratelimit": 30 * 1024 * 1024,  # Rate limit of 30 MB/s
        }

        # Configure download directory
        self._download_path: str = download_path
        
        self._create_download_dir()

    def _create_download_dir(self) -> None:
        os.makedirs(name=self._download_path, exist_ok=True)

    def download(self, url: str) -> None:
        # Skip if no url provided
        if not url:
            return

        if is_playlist_url(url=url):
            self._download_options["outtmpl"] = os.path.join(
                self._download_path,
                "%(playlist_title)s",
                "%(playlist_index)s-%(title)s.%(ext)s",
            )
            print("Detected playlist URL. Downloading entire playlist...")
        else:
            self._download_options["outtmpl"] = os.path.join(
                self._download_path, "%(title)s.%(ext)s"
            )
            print("Detected single video URL. Downloading video...")

        # Download content
        with YoutubeDL(self._download_options) as ydl:
            ydl.download([url])  # type:ignore
            print(
                f"\nDownload completed successfully! Files saved to: {self._download_path}"
            )
