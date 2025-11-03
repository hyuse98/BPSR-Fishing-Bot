import time

from ..bot_state import BotState
from ..state_type import StateType


class CheckingRodState(BotState):

    def handle(self, screen):
        self.bot.log("[CHECKING_ROD] Verificando vara...")

        time.sleep(1)

        if self.detector.find(screen, "broken_rod"):
            self.bot.log("[CHECKING_ROD] ⚠️  Vara quebrada! Trocando...")
            self.bot.stats.increment('rod_breaks')
            time.sleep(1)

            self.controller.press_key('m')
            time.sleep(1)

            self.controller.move_to(1650, 580)
            time.sleep(0.5)
            self.controller.move_to(1650, 580)
            time.sleep(0.5)
            self.controller.click('left')
            time.sleep(1)

            self.bot.log("[CHECKING_ROD] ✅ Vara trocada")
        else:
            time.sleep(1)
            self.bot.log("[CHECKING_ROD] ✅ Vara OK")

        return StateType.CASTING_BAIT