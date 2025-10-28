from abc import ABC, abstractmethod


class BotState(ABC):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config.bot
        self.detector = bot.detector
        self.controller = bot.controller
        self.level_check_interceptor = bot.level_check_interceptor

    @abstractmethod
    def handle(self, screen):
        pass
