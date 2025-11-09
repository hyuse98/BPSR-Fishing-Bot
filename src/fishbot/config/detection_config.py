from .paths import TEMPLATES_PATH

class DetectionConfig:
    def __init__(self):

        self.precision = 0.7

        self.templates_path = str(TEMPLATES_PATH)

        self.templates = {
            "fishing_spot_btn": "fishing_spot_btn.png",
            "broken_rod": "broken_rod.png",
            "new_rod": "new_rod.png",
            "exclamation": "exclamation.png",
            "left_arrow": "left_arrow.png",
            "right_arrow": "right_arrow.png",
            "success": "success.png",
            "continue": "continue.png",
            "level_check": "level_check.png"
        }

        # General Resolutions Config, But Slow Response Time
        # self.rois = {
        #     "fishing_spot": None,
        #     "broken_rod": None,
        #     "new_rod": None,
        #     "exclamation": None,
        #     "left_arrow": None,
        #     "right_arrow": None,
        #     "success": None,
        #     "continue": None,
        #     "level_check": None
        # }

        #FullHD 1080p Config
        self.rois = {
            "fishing_spot_btn": (1400, 540, 121, 55),
            "broken_rod": (1635, 982, 250, 63),
            "new_rod": (1624, 563, 185, 65),
            "exclamation": (929, 438, 52, 142),
            "left_arrow": (740, 490, 220, 100),
            "right_arrow": (960, 490, 220, 100),
            "success": (710, 620, 570, 130),
            "continue": (1439, 942, 306, 75),
            "level_check": (1101, 985, 131, 57)
        }