from .bot_state import BotState
import time

class WaitingForBiteState(BotState):
    
    def __init__(self, bot):
        super().__init__(bot)
        self._last_wait_log = 0

    def handle(self, screen):

        pos = self.detector.find(screen, "exclamation", debug=self.bot.debug_mode)
        
        if pos:
            self.bot.log("[WAITING_FOR_BITE] ❗ Peixe fisgado!")
            self.controller.mouse_down('left')
            return "PLAYING_MINIGAME"
        else:
            current_time = time.time()
            if current_time - self._last_wait_log > 5:
                self.bot.log("[WAITING_FOR_BITE] ⏳ Aguardando peixe...")
                self._last_wait_log = current_time
            
            return "WAITING_FOR_BITE"