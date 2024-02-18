# import numpy as np
import cv2 as cv
import atexit
from contextlib import contextmanager

from video_uri_builder import VideoURIBuilder


def register_cleanup():
    """Register cleanup when code exits to destroy all windows"""

    def clean_cv_windows():
        cv.destroyAllWindows

    atexit.register(clean_cv_windows)


@contextmanager
def managed_video_capture(uri: VideoURIBuilder):
    """Managed connection to video source

    Args:
        uri (VideoURIBuilder): _description_

    Yields:
        _type_: _description_
    """

    cam = cv.VideoCapture(str(uri))
    try:
        yield cam
    finally:
        cam.release()


def main(uri: VideoURIBuilder):
    """main

    Args:
        uri (VideoURIBuilder): _description_
    """
    register_cleanup()

    with managed_video_capture(uri=uri) as cam:
        if not cam.isOpened():
            print("Error opening camera")
            exit()

        while True:
            ret, frame = cam.read()

            if not ret:
                print("Error in retrieving frame.")
                exit()

            cv.imshow("frame", frame)

            if cv.waitKey(1) == ord("q"):
                break


if __name__ == "__main__":
    main(uri=VideoURIBuilder())
