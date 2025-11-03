import time

import pyautogui as auto

from src.fishbot.utils.logger import log


class GameController:
    def __init__(self, config):
        self.config = config.bot
        auto.FAILSAFE = True
        auto.PAUSE = 0.05

    def press_key(self, key):
        log(f"[CONTROLLER] 🔘 Pressionando tecla: {key}")
        auto.press(key)
        time.sleep(0.1)

    def click(self, button='left', clicks=1, interval=0.1):
        log(f"[CONTROLLER] 🖱️  Clicando: {button} ({clicks}x)")
        auto.click(button=button, clicks=clicks, interval=interval)
        time.sleep(0.15)

    def click_at(self, x, y, button='left'):
        log(f"[CONTROLLER] 🖱️  Clicando em ({x}, {y})")
        auto.click(x, y, button=button)
        time.sleep(0.15)

    def move_to(self, x, y):
        log(f"[CONTROLLER] 📍 Movendo mouse para: ({x}, {y})")
        auto.moveTo(x, y, duration=0.2)
        time.sleep(0.1)

    def mouse_down(self, button='left'):
        log(f"[CONTROLLER] 🖱️ ⬇️  Segurando mouse: {button}")
        auto.mouseDown(button=button)
        time.sleep(0.1)

    def mouse_up(self, button='left'):
        log(f"[CONTROLLER] 🖱️ ⬆️  Soltando mouse: {button}")
        auto.mouseUp(button=button)
        time.sleep(0.1)

    def key_down(self, key):
        log(f"[CONTROLLER] 🔘 ⬇️  Segurando tecla: {key}")
        auto.keyDown(key)

    def key_up(self, key):
        log(f"[CONTROLLER] 🔘 ⬆️  Soltando tecla: {key}")
        auto.keyUp(key)

    def release_all_controls(self):
        log("[CONTROLLER] ⚠️  Soltando todos os controles...")
        self.mouse_up('left')
        self.mouse_up('right')
        self.key_up('a')
        self.key_up('d')