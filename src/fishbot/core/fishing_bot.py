import time

from src.fishbot.config import Config
from src.fishbot.core.game.controller import GameController
from src.fishbot.core.game.detector import Detector
from src.fishbot.core.interceptors.level_check_interceptor import LevelCheckInterceptor
from src.fishbot.core.state.impl.casting_bait_state import CastingBaitState
from src.fishbot.core.state.impl.checking_rod_state import CheckingRodState
from src.fishbot.core.state.impl.finishing_state import FinishingState
from src.fishbot.core.state.impl.playing_minigame_state import PlayingMinigameState
from src.fishbot.core.state.impl.starting_state import StartingState
from src.fishbot.core.state.impl.waiting_for_bite_state import WaitingForBiteState
from src.fishbot.core.state.state_machine import StateMachine
from src.fishbot.core.state.state_type import StateType
from src.fishbot.core.stats import StatsTracker
from src.fishbot.utils.logger import log


class FishingBot:
    def __init__(self):
        self.config = Config()
        self.stats = StatsTracker()
        self.log = log

        self.detector = Detector(self.config)
        self.controller = GameController(self.config)
        self.state_machine = StateMachine(self)

        self.level_check_interceptor = LevelCheckInterceptor(self)

        self.running = True
        self.debug_mode = self.config.bot.debug_mode

        self._register_states()

    def _register_states(self):
        self.state_machine.add_state(StateType.STARTING, StartingState(self))
        self.state_machine.add_state(StateType.CHECKING_ROD, CheckingRodState(self))
        self.state_machine.add_state(StateType.CASTING_BAIT, CastingBaitState(self))
        self.state_machine.add_state(StateType.WAITING_FOR_BITE, WaitingForBiteState(self))
        self.state_machine.add_state(StateType.PLAYING_MINIGAME, PlayingMinigameState(self))
        self.state_machine.add_state(StateType.FINISHING, FinishingState(self))



    def run(self):
        log("[INFO] 🎣  Bot iniciado! Pressione Ctrl+C para parar")
        log("[INFO] ⚠️  IMPORTANTE: Mantenha o jogo em FOCO (janela ativa)")
        log(f"[INFO] ⚙️  Precisão: {self.config.bot.detection.precision * 100:.0f}%")
        log(f"[INFO] ⚙️  FPS alvo: {'MAX' if self.config.bot.target_fps == 0 else self.config.bot.target_fps}")
        log(f"[INFO] 🕐 Aguardando {self.config.bot.start_time_delay} segundos para você focar no jogo...")
        time.sleep(self.config.bot.start_time_delay)
        log("[INFO] ▶️  Iniciando bot!")

        self.state_machine.set_state(StateType.STARTING)

        target_delay = 1.0 / self.config.bot.target_fps if self.config.bot.target_fps > 0 else 0

        try:
            while self.running:
                loop_start = time.time()

                screen = self.detector.capture_screen()
                self.state_machine.handle(screen)

                if target_delay > 0:
                    loop_time = time.time() - loop_start
                    sleep_time = max(0, target_delay - loop_time)
                    if sleep_time > 0:
                        time.sleep(sleep_time)

        except KeyboardInterrupt:
            log("[BOT] 🛑 Bot encerrado pelo usuário")
            try:
                self.controller.release_all_controls()
            except Exception as e:
                pass
            self.stats.show()