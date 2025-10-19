# ============================================================
# === MAIN (Ponto de Entrada, como o Main.java) ==============
# ============================================================
# Este arquivo é o único que você precisa executar.
# Ele importa a classe principal do bot e a inicia.
#
# Para executar, use no seu terminal, a partir da pasta
# raiz do projeto (ex: MeuBotDePesca/):
# python main.py
# ============================================================

from fishbot.bot import FishingBot

if __name__ == "__main__":
    bot = FishingBot()
    bot.run()