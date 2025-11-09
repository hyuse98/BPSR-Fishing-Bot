import keyboard
import multiprocessing
from src.fishbot.utils.logger import log
from src.fishbot.utils.roi_visualizer import main as show_roi_visualizer

class Hotkeys:
    def __init__(self, bot):
        self.bot = bot
        self.paused = True
        self.visualizer_process = None
        self._register_hotkeys()

    def _register_hotkeys(self):
        keyboard.add_hotkey('f1', self._toggle_pause)
        keyboard.add_hotkey('f2', self._stop)
        keyboard.add_hotkey('f3', self._toggle_visualizer)
        log("[INFO] ✅ Hotkeys registradas: F1 (Pausar/Continuar), F2 (Sair), F3 (Visualizador de ROI)")

    def _toggle_pause(self):
        self.paused = not self.paused
        status = "PAUSADO" if self.paused else "EM EXECUÇÃO"
        log(f"[HOTKEY] Bot {status}.")

    def _stop(self):
        log("[HOTKEY] Parando o bot...")
        if self.visualizer_process and self.visualizer_process.is_alive():
            self.visualizer_process.terminate()
        self.bot.stop()

    def _toggle_visualizer(self):
        if self.visualizer_process and self.visualizer_process.is_alive():
            log("[HOTKEY] Fechando o visualizador de ROI.")
            self.visualizer_process.terminate()
            self.visualizer_process = None
        else:
            log("[HOTKEY] Abrindo o visualizador de ROI.")
            # Executa o visualizador em um processo separado para não bloquear a UI principal
            self.visualizer_process = multiprocessing.Process(target=show_roi_visualizer, daemon=True)
            self.visualizer_process.start()

    def wait_for_exit(self):
        """Mantém o script em execução até que a hotkey de saída seja pressionada."""
        keyboard.wait('f2')
