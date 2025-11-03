import time

from .base_interceptor import BaseInterceptor


class RodCheckInterceptor(BaseInterceptor):

    def check(self, screen):

        if self.detector.find(screen, "broken_rod"):
            self.bot.log("[CHECKING_ROD] ⚠️  Vara quebrada! Trocando...")

            self.controller.release_all_controls()
            return True

        return False