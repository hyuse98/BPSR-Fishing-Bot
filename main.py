import time

from src.fishbot.core.fishing_bot import FishingBot
from src.fishbot.core.game.hotkeys import Hotkeys
from src.fishbot.utils.logger import log


def main():
    bot = FishingBot()
    hotkeys = Hotkeys(bot)

    bot.start()

    log("[INFO] Pressione F1 para iniciar o bot.")

    while not bot.is_stopped():
        if not hotkeys.paused:
            bot.update()

        time.sleep(0.1)

    log("[INFO] Bot Finalizado.")


if __name__ == "__main__":
    main()