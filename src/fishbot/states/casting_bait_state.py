import time
from .bot_state import BotState

class CastingBaitState(BotState):
    
    def handle(self, screen):
        
        self.bot.log("[CASTING_BAIT] 🎣 Aguardando 1.5 segundos...")
        time.sleep(1.5)
        
        center_x = self.config.monitor_width // 2 + self.config.monitor_x
        center_y = self.config.monitor_height // 2 + self.config.monitor_y
        
        self.bot.log(f"[CASTING_BAIT] 📍 Movendo mouse para centro da tela ({center_x}, {center_y})")
        self.controller.move_to(center_x, center_y)
        time.sleep(1)
        
        self.bot.log("[CASTING_BAIT] 🖱️  Clicando para garantir foco...")
        self.controller.click_at(center_x, center_y)
        time.sleep(0.5)
        
        self.bot.log("[CASTING_BAIT] 🎣 Lançando isca...")
        self.controller.mouse_down('left')
        time.sleep(0.1) 
        self.controller.mouse_up('left')
        time.sleep(2)
        
        return "WAITING_FOR_BITE"