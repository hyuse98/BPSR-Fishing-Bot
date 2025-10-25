import time

from .config import Config
from .controller import GameController
from .detector import Detector
from .interceptors.level_check_interceptor import LevelCheckInterceptor
from .states.casting_bait_state import CastingBaitState
from .states.checking_rod_state import CheckingRodState
from .states.finishing_state import FinishingState
from .states.playing_minigame_state import PlayingMinigameState
from .states.starting_state import StartingState
from .states.waiting_for_bite_state import WaitingForBiteState


class FishingBot:
    def __init__(self):

        self.config = Config()
        self.detector = Detector(self.config)
        self.controller = GameController(self.config)

        self.running = True
        self.debug_mode = self.config.debug_mode
        self.stats = {
            'cycles': 0,
            'fish_caught': 0,
            'rod_breaks': 0
        }

        self.level_check_interceptor = LevelCheckInterceptor(self)

        self.states = {
            "STARTING": StartingState(self),
            "CHECKING_ROD": CheckingRodState(self),
            "CASTING_BAIT": CastingBaitState(self),
            "WAITING_FOR_BITE": WaitingForBiteState(self),
            "PLAYING_MINIGAME": PlayingMinigameState(self),
            "FINISHING": FinishingState(self),
        }

        self.current_state_name = "STARTING"
        self.current_state = self.states[self.current_state_name]

    def log(self, message):

        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")

    def set_state(self, new_state_name):

        if new_state_name != self.current_state_name:
            if new_state_name not in self.states:
                self.log(f"ERRO: Tentativa de mudar para estado desconhecido: {new_state_name}")
                return

            self.log(f"Mudando de estado: {self.current_state_name} -> {new_state_name}")
            self.current_state_name = new_state_name
            self.current_state = self.states[self.current_state_name]

    def run(self):
        self.log("🎣 Bot iniciado! Pressione Ctrl+C para parar")
        self.log("⚠️  IMPORTANTE: Mantenha o jogo em FOCO (janela ativa)")
        self.log(f"⚙️  Precisão: {self.config.precision * 100:.0f}%")
        self.log(f"⚙️  FPS alvo: {'MAX' if self.config.target_fps == 0 else self.config.target_fps}")
        self.log("\n🕐 Aguardando 5 segundos para você focar no jogo...")
        time.sleep(5)
        self.log("▶️  Iniciando bot!\n")

        target_delay = 1.0 / self.config.target_fps if self.config.target_fps > 0 else 0

        try:
            while self.running:
                loop_start = time.time()

                screen = self.detector.capture_screen()

                new_state_name = self.current_state.handle(screen)

                self.set_state(new_state_name)

                if target_delay > 0:
                    loop_time = time.time() - loop_start
                    sleep_time = max(0, target_delay - loop_time)
                    if sleep_time > 0:
                        time.sleep(sleep_time)

        except KeyboardInterrupt:
            self.log("\n🛑 Bot encerrado pelo usuário")
            try:
                self.log("... Soltando todas as teclas e mouse.")
                self.controller.mouse_up('left')
                self.controller.key_up('a')
                self.controller.key_up('d')
            except Exception as e:
                pass
            self.show_stats()

    def show_stats(self):
        print("\n" + "=" * 50)
        print("📊 ESTATÍSTICAS")
        print("=" * 50)
        print(f"  🔄 Ciclos completados: {self.stats['cycles']}")
        print(f"  🐟 Peixes capturados: {self.stats['fish_caught']}")
        print(f"  🔧 Varas quebradas: {self.stats['rod_breaks']}")
        print("=" * 50)
