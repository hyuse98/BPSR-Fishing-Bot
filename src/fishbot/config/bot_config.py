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
            "WAITING_FOR_BITE": 30,
            "PLAYING_MINIGAME": 60,
            "FINISHING": 30
        }

        # Habilitar finalização rápida após o minigame
        self.quick_finish_enabled = True

        self.debug_mode = False

        # Precisão de deteção (0.0 a 1.0)
        self.precision = 0.7

        # FPS alvo (capturas por segundo)
        # 0 significa sem limite
        self.target_fps = 0

        # Delays (em segundos)
        self.default_delay = 1.0
        self.finish_wait_delay = 1.5  # Delay para o Guard Rail 3

        # Coordenadas para trocar vara (x, y relativo à tela capturada)
        self.new_rod_coord = (1626, 565)
