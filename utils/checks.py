from urllib.parse import ParseResult, parse_qs, urlparse


def is_playlist_url(url: str) -> bool:
    """
    Check if the provided URL is a playlist or a single video.

    Args:
        url (str): YouTube URL to check

    Returns:
        bool: True if URL is a playlist, False if single video
    """
    parsed_url: ParseResult = urlparse(url)
    query_params: dict[str, list[str]] = parse_qs(parsed_url.query)
    return "list" in query_params
