import time

from ..bot_state import BotState
from ..state_type import StateType


class WaitingForBiteState(BotState):

    def __init__(self, bot):
        super().__init__(bot)
        self._last_wait_log = 0

    def handle(self, screen):

        pos = self.detector.find(screen, "exclamation", debug=self.bot.debug_mode)

        if pos:
            self.bot.log("[WAITING_FOR_BITE] ❗ Peixe fisgado!")
            self.controller.mouse_down('left')
            return StateType.PLAYING_MINIGAME
        else:
            current_time = time.time()
            if current_time - self._last_wait_log > 5:
                self.bot.log("[WAITING_FOR_BITE] ⏳ Aguardando peixe...")
                self._last_wait_log = current_time

            return StateType.WAITING_FOR_BITE