import time

from .bot_state import BotState


class StartingState(BotState):

    def __init__(self, bot):
        super().__init__(bot)
        self._last_search_log = 0

    def handle(self, screen):
        pos = self.detector.find(screen, "fishing_spot", debug=self.bot.debug_mode)

        if pos:
            self.bot.log(f"[STARTING] ✅ Ponto de pesca detectado em {pos}")
            self.bot.log("[STARTING] Pressionando 'F'...")
            time.sleep(1)

            self.controller.press_key('f')
            self.bot.log("[STARTING] Entrando no modo pesca")
            time.sleep(1)

            return "CHECKING_ROD"

        else:
            current_time = time.time()
            if current_time - self._last_search_log > 2:
                self.bot.log("[STARTING] 🔍 Procurando ponto de pesca...")
                if self.bot.debug_mode:
                    self.bot.log("[STARTING] 💡 Debug ativado")
                self._last_search_log = current_time

            return "STARTING"
