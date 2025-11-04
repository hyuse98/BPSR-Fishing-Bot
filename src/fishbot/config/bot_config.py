from .screen_config import ScreenConfig
from .detection_config import DetectionConfig

class BotConfig:
    def __init__(self):

        self.screen = ScreenConfig()
        self.detection = DetectionConfig()

        self.state_timeouts = {
            "STARTING": 10,
            "CHECKING_ROD": 15,
            "CASTING_BAIT": 15,
            "WAITING_FOR_BITE": 25,
            "PLAYING_MINIGAME": 40,
            "FINISHING": 10
        }

        # Habilitar finalização rápida após o minigame
        self.quick_finish_enabled = True

        self.debug_mode = False

        # FPS alvo (capturas por segundo)
        # 0 significa sem limite
        self.target_fps = 0

        # Delays (em segundos)
        self.default_delay = 1.0
        self.finish_wait_delay = 1.5