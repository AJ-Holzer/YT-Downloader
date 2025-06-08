import os
import sys

from env.classes.downloader import VideoDownloader


def main() -> None:
    yt_downloader: VideoDownloader = VideoDownloader()

    while True:
        # Clear the terminal

        # trunk-ignore(bandit/B605)
        os.system("cls" if sys.platform == "nt" else "clear")

        # Ask for url
        yt_url: str = input("Enter the url of the video to download: ")

        # Download the video
        yt_downloader.download(url=yt_url)


if __name__ == "__main__":
    main()
