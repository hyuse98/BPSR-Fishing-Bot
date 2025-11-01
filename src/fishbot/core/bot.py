import time

from src.fishbot.config import Config
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
        self.debug_mode = self.config.bot.debug_mode
        self.stats = {
            'cycles': 0,
            'fish_caught': 0,
            'rod_breaks': 0,
            'timeouts': 0
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

        self.state_start_time = time.time()

    def log(self, message):
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")

    def check_state_timeout(self):
        timeout_limit = self.config.bot.state_timeouts.get(self.current_state_name)

        if not timeout_limit:
            return False

        elapsed_time = time.time() - self.state_start_time

        if elapsed_time > timeout_limit:
            self.log(f"🚨 [TIMEOUT] Estado '{self.current_state_name}' excedeu {timeout_limit}s!")
            self.log("🚨 [TIMEOUT] Soltando controles e pressionando 'ESC' para resetar.")

            self.controller.release_all_controls()
            self.controller.press_key('esc')
            time.sleep(0.5)

            self.stats['timeouts'] += 1

            self.set_state("STARTING", force=True)

            return True

        return False

    def set_state(self, new_state_name, force=False):
        if not force and new_state_name == self.current_state_name:
            return

        if new_state_name not in self.states:
            self.log(f"ERRO: Tentativa de mudar para estado desconhecido: {new_state_name}")
            return

        if new_state_name != self.current_state_name:
            self.log(f"Mudando de estado: {self.current_state_name} -> {new_state_name}")
        elif force:
            self.log(f"Forçando reset do estado: {new_state_name}")

        self.current_state_name = new_state_name
        self.current_state = self.states[self.current_state_name]

        self.state_start_time = time.time()

    def run(self):
        self.log("🎣 Bot iniciado! Pressione Ctrl+C para parar")
        self.log("⚠️  IMPORTANTE: Mantenha o jogo em FOCO (janela ativa)")
        self.log(f"⚙️  Precisão: {self.config.bot.detection.precision * 100:.0f}%")
        self.log(f"⚙️  FPS alvo: {'MAX' if self.config.bot.target_fps == 0 else self.config.bot.target_fps}")
        self.log("\n🕐 Aguardando 5 segundos para você focar no jogo...")
        time.sleep(5)
        self.log("▶️  Iniciando bot!\n")

        target_delay = 1.0 / self.config.bot.target_fps if self.config.bot.target_fps > 0 else 0

        try:
            while self.running:
                loop_start = time.time()

                screen = self.detector.capture_screen()

                if self.check_state_timeout():
                    continue

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
                self.controller.release_all_controls()
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
        print(f"  🚨 Timeouts ocorridos: {self.stats['timeouts']}")
        print("=" * 50)
