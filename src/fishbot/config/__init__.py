from .bot_config import BotConfig
from .paths import PACKAGE_ROOT, ASSETS_PATH, TEMPLATES_PATH

class Config:
    """
    Classe de configuração unificada que atua como um ponto de acesso
    único para todas as configurações do projeto.
    """
    def __init__(self):
        self.bot = BotConfig()

        self.paths = {
            'package_root': PACKAGE_ROOT,
            'assets': ASSETS_PATH,
            'templates': TEMPLATES_PATH
        }

    def get_template_path(self, template_name):
        """
        Método auxiliar para obter o caminho absoluto de um template.
        """
        filename = self.bot.templates.get(template_name)
        if filename:
            return self.paths['templates'] / filename
        return None
