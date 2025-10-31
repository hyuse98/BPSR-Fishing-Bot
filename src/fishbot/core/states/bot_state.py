from abc import ABC, abstractmethod

from ..bot_component import BotComponent


class BotState(BotComponent, ABC):

    def __init__(self, bot):
        super().__init__(bot)
        self.level_check_interceptor = bot.level_check_interceptor

    @abstractmethod
    def handle(self, screen):
        pass