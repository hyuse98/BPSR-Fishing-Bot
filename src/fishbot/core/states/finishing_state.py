import time

from .bot_state import BotState


class FinishingState(BotState):

    def __init__(self, bot):
        super().__init__(bot)

    def handle(self, screen):

        # # --- [GUARD RAIL 1 (Interceptor)] ---
        # new_state = self.level_check_interceptor.check(screen)
        # if new_state:
        #     self.bot.log("[FINISHING] ⚠️ Level Check detectado durante o finalização.")
        #     return new_state
        # # --- [FIM DO GUARD RAIL] ---

        pos = self.detector.find(screen, "continue")

        if pos:
            self.bot.log("[FINISHING] 🖱️  Clicando em 'Continue'...")
            self.controller.move_to(pos[0], pos[1])
            time.sleep(0.2)
            self.controller.click('left')

        return "FINISHING"