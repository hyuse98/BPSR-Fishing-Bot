class BotComponent:

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config.bot
        self.detector = bot.detector
        self.controller = bot.controller