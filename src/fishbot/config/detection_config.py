from .paths import TEMPLATES_PATH

class DetectionConfig:
    def __init__(self):
        self.precision = 0.8
        self.templates_path = str(TEMPLATES_PATH)

        self.templates = {
            "fishing_spot": "fishing_btn.png",
            "broken_rod": "empty_pole_slot.png",
            "new_rod": "add_new_pole_btn.png",
            "exclamation": "fish_bite_sinal.png",
            "left_arrow": "left_arrow.png",
            "right_arrow": "right_arrow.png",
            "success": "caught_sinal.png",
            "continue": "continue_fishing.png",
            "level_check": "level_check.png"
        }

        self.rois = {
            "fishing_spot": (1400, 540, 120, 54),
            "broken_rod": (1636, 985, 59, 60),
            "new_rod": (1626, 565, 182, 62),
            "exclamation": (932, 441, 47, 137),
            "left_arrow": (750, 490, 210, 100),
            "right_arrow": (960, 490, 210, 100),
            "success": None,
            "continue": (1442, 945, 301, 69),
            "level_check": (1101, 985, 130, 57)
        }