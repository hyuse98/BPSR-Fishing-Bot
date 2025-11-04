import keyboard
from src.fishbot.utils.logger import log

class Hotkeys:
    def __init__(self, bot):
        self.bot = bot
        self.paused = True
        self._register_hotkeys()

    def _register_hotkeys(self):
        keyboard.add_hotkey('f1', self._toggle_pause)
        keyboard.add_hotkey('f2', self._stop)
        log("[INFO] ✅ Hotkeys registradas: F1 (Pausar/Continuar), F2 (Sair)")

    def _toggle_pause(self):
        self.paused = not self.paused
        status = "PAUSADO" if self.paused else "EM EXECUÇÃO"
        log(f"[HOTKEY] Bot {status}.")

    def _stop(self):
        log("[HOTKEY] Parando o bot...")
        self.bot.stop()

    def wait_for_exit(self):
        keyboard.wait('f2')
