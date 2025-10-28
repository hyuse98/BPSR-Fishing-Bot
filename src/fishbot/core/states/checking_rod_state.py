import time

from .bot_state import BotState


class CheckingRodState(BotState):

    def handle(self, screen):
        self.bot.log("[CHECKING_ROD] Verificando vara...")

        if self.detector.find(screen, "broken_rod"):
            self.bot.log("[CHECKING_ROD] ⚠️  Vara quebrada! Trocando...")
            self.bot.stats['rod_breaks'] += 1
            time.sleep(1)

            self.controller.press_key('m')
            time.sleep(1)

            roi = self.config.rois.get("new_rod")
            if roi:
                center_x = roi[0] + roi[2] // 2 + self.config.monitor_x
                center_y = roi[1] + roi[3] // 2 + self.config.monitor_y
            else:
                center_x = self.config.new_rod_coord[0] + self.config.monitor_x
                center_y = self.config.new_rod_coord[1] + self.config.monitor_y

            self.controller.move_to(center_x, center_y)
            time.sleep(0.5)
            self.controller.move_to(center_x, center_y)
            time.sleep(0.5)
            self.controller.click('left')
            time.sleep(1)

            self.bot.log("[CHECKING_ROD] ✅ Vara trocada")
        else:
            time.sleep(1)
            self.bot.log("[CHECKING_ROD] ✅ Vara OK")

        return "CASTING_BAIT"