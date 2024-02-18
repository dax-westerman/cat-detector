class VideoURIBuilder:
    def __init__(
        self,
        *,
        username: str = "admin",
        password: str = "5Chz2sH8",
        ip: str = "192.168.0.168",
        width: int = 320,
        height: int = 240,
    ):
        self._video_url = f"http://{username}:{password}@{ip}/video.cgi?resolution={str(width)}x{str(height)}"  # noqa

    def __str__(self):
        return self._video_url

    def __repr__(self) -> str:
        return self.__str__()
