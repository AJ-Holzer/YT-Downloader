class Config:
    # Default paths
    PATH_DEFAULT_DOWNLOADS: str = "./YT-Downloads"
    
    # Download options
    DOWNLOAD_OPTION_FORMAT: str = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
    DOWNLOAD_OPTION_MERGE_OUTPUT_FORMAT: str = "mp4"
    DOWNLOAD_OPTION_IGNORE_ERRORS: bool = True
    DOWNLOAD_OPTION_NO_WARNINGS: bool = False
    DOWNLOAD_OPTION_EXTRACT_FLAT: bool = False
    DOWNLOAD_OPTION_WRITE_SUBTITLES: bool = False
    DOWNLOAD_OPTION_WRITE_THUMBNAIL: bool = True
    DOWNLOAD_OPTION_WRITE_AUTOMATIC_SUB: bool = False
    DOWNLOAD_OPTION_POST_PROCESSORS: list[dict[str, str]] = [
        {
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mp4",
        }
    ]
    DOWNLOAD_OPTION_KEEP_VIDEO: bool = False
    DOWNLOAD_OPTION_CLEAN_INFO_JSON: bool = True

config = Config()
