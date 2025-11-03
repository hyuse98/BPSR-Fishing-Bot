from .paths import TEMPLATES_PATH

class DetectionConfig:
    def __init__(self):

        self.precision = 0.7

        self.templates_path = str(TEMPLATES_PATH)

        self.templates = {
            "fishing_spot": "fishing_spot.png",
            "broken_rod": "broken_rod.png",
            "new_rod": "new_rod.png",
            "exclamation": "exclamation.png",
            "left_arrow": "left_arrow.png",
            "right_arrow": "right_arrow.png",
            "success": "success.png",
            "continue": "continue.png",
            "level_check": "level_check.png"
        }

        self.rois = {
            "fishing_spot": None,
            "broken_rod": None,
            "new_rod": None,
            "exclamation": None,
            "left_arrow": None,
            "right_arrow": None,
            "success": None,
            "continue": None,
            "level_check": None
        }
