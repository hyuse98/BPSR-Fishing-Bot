from abc import ABC, abstractmethod

class BaseInterceptor(ABC):

    def __init__(self, bot):
        self.bot = bot
        self.detector = bot.detector
        self.controller = bot.controller

    @abstractmethod
    def check(self, screen):
        pass