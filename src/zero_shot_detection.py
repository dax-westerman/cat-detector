from itertools import chain
from transformers import pipeline
import os
import glob
from pprint import pprint
import atexit
import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw
import random

IMAGE_PATH = (
    "/home/dax/dev/cat-detector/.test_images/non_cat_images/20200625_090958.jpg"
)


def show_image(image):
    image.show()


def register_cleanup():
    """Register cleanup when code exits to destroy all windows"""

    def clean_cv_windows():
        cv.destroyAllWindows

    atexit.register(clean_cv_windows)


checkpoint = "google/owlvit-base-patch32"
detector = pipeline(model=checkpoint, task="zero-shot-object-detection")


# image = skimage.data.astronaut()

# img_path = IMAGE_PATH


def check_for_cat(show_image, detector, img_path):
    print(f'Checking {img_path}')
    if not os.path.isfile(img_path):
        return
    image = Image.open(img_path)  # noqa
    image = Image.fromarray(np.uint8(image)).convert("RGB")

    predictions = detector(
        image,
        candidate_labels=[
            "cat"
        ],  # noqa
    )

    if len(predictions) > 0:
        print(f'Cat found in {img_path}')
        pprint(predictions)

        draw = ImageDraw.Draw(image)

        for prediction in predictions:
            box = prediction["box"]
            label = prediction["label"]
            score = prediction["score"]

            xmin, ymin, xmax, ymax = box.values()
            draw.rectangle((xmin, ymin, xmax, ymax), outline="red", width=10)
            draw.text((xmin, ymin), f"{label}: {round(score, 2)}", fill="white")  # noqa

        show_image(image)

    else:
        print(f'Cat NOT found in {img_path}')

image_list = glob.glob(
    "C:/dev/cat-detector/.test_images/**/*.jpg", recursive=True
)
random_image_list = random.sample(image_list, len(image_list))

for img_path in random_image_list:  # noqa
    check_for_cat(show_image, detector, img_path)
