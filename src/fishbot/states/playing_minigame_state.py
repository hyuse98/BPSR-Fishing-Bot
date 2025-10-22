import time
from .bot_state import BotState

class PlayingMinigameState(BotState):
    
    def __init__(self, bot):
        super().__init__(bot)
        self._current_arrow = None
        self.switch_delay = 0.7

    def handle(self, screen):

        if self.detector.find(screen, "success"):
            self.bot.log("[MINIGAME] 🐟 Peixe capturado!")
            self.bot.stats['fish_caught'] += 1
            
            self.controller.mouse_up('left')
            self.controller.key_up('a')
            self.controller.key_up('d')
            self._current_arrow = None

            if self.config.quick_finish_enabled:
                self.bot.log("[MINIGAME] ⏩ Finalizando rapidamente...")
                self.controller.press_key('esc')
                time.sleep(0.5)
                return "STARTING"
            else:            
                return "FINISHING"

        #TODO Need Improvement
        
        if self.detector.find(screen, "left_arrow"):

            if self._current_arrow is None:
                self.bot.log("[MINIGAME] ⬅️  Movendo para a esquerda (Segurando 'A')")
                self.controller.key_down('a')
                self._current_arrow = 'left'
                time.sleep(self.switch_delay)
            
            if self._current_arrow == 'right':
                self.bot.log("[MINIGAME] ⬅️  Movendo para a esquerda (Soltando 'D')")
                self.controller.key_up('d')
                self._current_arrow = None
                time.sleep(self.switch_delay)
                
        if self.detector.find(screen, "right_arrow"):

            if self._current_arrow is None:
                self.bot.log("[MINIGAME] ➡️  Movendo para a direita (Segurando 'D')")
                self.controller.key_down('d')
                self._current_arrow = 'right'
                time.sleep(self.switch_delay)

            if self._current_arrow == 'left':
                self.bot.log("[MINIGAME] ➡️  Movendo para a direita (Soltando 'A')")
                self.controller.key_up('a')
                self._current_arrow = None
                time.sleep(self.switch_delay)
                
        return "PLAYING_MINIGAME"