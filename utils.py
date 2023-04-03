import cv2
import numpy as np


def crop_image(image: np.ndarray, x: int, y: int, w: int, h: int) -> np.ndarray:
    # Change w and h to abs values
    w = abs(w)
    h = abs(h)
    return image[y:y+h, x:x+w]


def save_image(image: np.ndarray, path: str) -> None:
    cv2.imwrite(path, image)


def load_image(path: str) -> np.ndarray:
    return cv2.imread(path)