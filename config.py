# Config for PossessionDetectionPlayground
from typing import Dict, Tuple


class Config:
    def __init__(self):
        self.image_dir: str = "data/images"
        self.blue_player_bbox: Dict[str, int] = {"x1": 660, "y1": 505, "x2": 760, "y2": 635}
        self.white_player_bbox: Dict[str, int] = {"x1": 715, "y1": 310, "x2": 800, "y2": 435}

        self.image_reszie_size: Tuple[int, int] = (20, 45)
