from abc import ABC, abstractmethod

from ..bot_component import BotComponent


class BaseInterceptor(BotComponent, ABC):

    def __init__(self, bot):
        super().__init__(bot)

    @abstractmethod
    def check(self, screen):
        pass