import time

from ..bot_state import BotState
from ..state_type import StateType


class PlayingMinigameState(BotState):

    def __init__(self, bot):
        super().__init__(bot)
        self._current_direction = None
        self.switch_delay = 0.5

    def _handle_arrow(self, direction, screen):
        arrow_template = f"{direction}_arrow"
        key_to_press = 'a' if direction == 'left' else 'd'
        key_to_release = 'd' if direction == 'left' else 'a'
        opposite_direction = 'right' if direction == 'left' else 'left'

        if self.detector.find(screen, arrow_template):
            if self._current_direction is None:
                self.bot.log(f"[MINIGAME] ▶️ Movendo para a {direction} (Segurando '{key_to_press}')")
                self.controller.key_down(key_to_press)
                self._current_direction = direction
                time.sleep(self.switch_delay)

            if self._current_direction == opposite_direction:
                self.bot.log(f"[MINIGAME] ◀️ Trocando para a {direction} (Soltando '{key_to_release}')")
                self.controller.key_up(key_to_release)
                self._current_direction = None
                time.sleep(self.switch_delay)

    def handle(self, screen):
        if self.detector.find(screen, "success"):
            self.bot.log("[MINIGAME] 🐟 Peixe capturado!")
            self.bot.stats.increment('fish_caught')

            self.controller.release_all_controls()
            self._current_direction = None

            if self.config.quick_finish_enabled:
                self.bot.log("[MINIGAME] ⏩ Finalizando rapidamente...")
                self.controller.press_key('esc')
                time.sleep(0.5)
                return StateType.STARTING
            else:
                return StateType.FINISHING

        self._handle_arrow('left', screen)
        self._handle_arrow('right', screen)

        return StateType.PLAYING_MINIGAME