import time

from .base_interceptor import BaseInterceptor


class LevelCheckInterceptor(BaseInterceptor):

    def check(self, screen):

        if self.detector.find(screen, "level_check"):
            self.bot.log("[GUARD RAIL 1] ⚠️  UI de 'Level Check' detectada!")
            self.bot.log("[GUARD RAIL 1] Resetando para o estado de checagem de vara.")

            self.controller.mouse_up('left')
            self.controller.key_up('a')
            self.controller.key_up('d')

            if hasattr(self.bot.states["PLAYING_MINIGAME"], '_current_arrow'):
                self.bot.states["PLAYING_MINIGAME"]._current_arrow = None
            self.bot.set_state("CHECKING_ROD")
            time.sleep(1)
            return True

        return False