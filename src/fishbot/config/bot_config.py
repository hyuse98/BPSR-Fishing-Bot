class BotConfig:

    def __init__(self):
        """
                Coordenadas do monitor (self.monitor_x, self.monitor_y)

                Isto define o canto superior esquerdo (ponto 0,0) da área
                que o ‘bot’ irá capturar com o MSS.

                O monitor onde o *JOGO ESTÁ ABERTO* é o monitor alvo.

                -------------------------------------------------------------------
                Cenário 1: O jogo está no seu MONITOR PRINCIPAL.
                -------------------------------------------------------------------
                self.monitor_x = 0
                self.monitor_y = 0

                -------------------------------------------------------------------
                Cenário 2: O jogo está no MONITOR SECUNDÁRIO, à ESQUERDA do principal.
                -------------------------------------------------------------------
                (Assumindo que o monitor secundário [o do jogo] tem 1920px de largura)
                self.monitor_x = −1920
                self.monitor_y = 0

                -------------------------------------------------------------------
                Cenário 3: O jogo está no MONITOR SECUNDÁRIO, à DIREITA do principal.
                -------------------------------------------------------------------
                (Assumindo que o monitor principal tem 1920px de largura)
                self.monitor_x = 1920
                self.monitor_y = 0
                -------------------------------------------------------------------
                """
        self.monitor_x = 0
        self.monitor_y = 0
        self.monitor_width = 1920
        self.monitor_height = 1080

        self.state_timeouts = {
            "STARTING": 15,
            "CHECKING_ROD": 15,
            "CASTING_BAIT": 15,
            "WAITING_FOR_BITE": 120,
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

        # Pasta dos templates
        self.templates_path = "src/fishbot/assets/templates/"

        # Templates
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

        # ROIs (x, y, width, height) - coordenadas sempre números positivos
        # relativos à tela capturada na resolução do monitor configurado
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