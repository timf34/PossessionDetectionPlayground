# Config for PossessionDetectionPlayground
from typing import Dict, Tuple


class Config:
    def __init__(self):
        self.image_dir: str = "data/images"
        self.blue_player_bbox: Dict[str, int] = {"x1": 680, "y1": 515, "x2": 750, "y2": 635}
        self.white_player_bbox: Dict[str, int] = {"x1": 730, "y1": 320, "x2": 790, "y2": 415}
        self.blue_player_img_path: str = "data/images/blue_player.jpg"
        self.white_player_img_path: str = "data/images/white_player.jpg"

        self.image_reszie_size: Tuple[int, int] = (20, 45)

        self.classifier_xml_file: str = "data/classifier.xml"

