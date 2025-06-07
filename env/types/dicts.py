from typing import TypedDict


class DownloadOptionsDict(TypedDict):
    format: str
    merge_output_format: str
    ignoreerrors: bool
    no_warnings: bool
    extract_flat: bool
    writesubtitles: bool
    writethumbnail: bool
    writeautomaticsub: bool
    postprocessors: list[dict[str, str]]
    keepvideo: bool
    clean_infojson: bool
