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
            "fishing_spot": (1400, 540, 121, 55),
            "broken_rod": (1636, 985, 250, 60),
            "new_rod": (1626, 565, 183, 65),
            "exclamation": (932, 441, 49, 139),
            "left_arrow": (750, 490, 210, 100),
            "right_arrow": (960, 490, 210, 100),
            "success": None,
            "continue": (1442, 945, 301, 71),
            "level_check": (1101, 985, 131, 57)
        }
