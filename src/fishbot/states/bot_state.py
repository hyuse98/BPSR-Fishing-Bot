from abc import ABC, abstractmethod

class BotState(ABC):
    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config
        self.detector = bot.detector
        self.controller = bot.controller

    @abstractmethod
    def handle(self, screen):
        pass