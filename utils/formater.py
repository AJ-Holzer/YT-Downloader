import re


def make_title_save(video_title: str) -> str:
    return re.sub(r"[^\w\-_.() ]", "_", video_title)
