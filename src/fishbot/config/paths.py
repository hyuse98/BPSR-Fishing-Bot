from pathlib import Path

# Path(__file__) é o caminho para este arquivo (paths.py)
# .resolve() torna o caminho absoluto
# .parent é o diretório 'config'
# .parent.parent é o diretório 'fishbot' que consideramos a raiz do pacote
PACKAGE_ROOT = Path(__file__).resolve().parent.parent
ASSETS_PATH = PACKAGE_ROOT / "assets"
TEMPLATES_PATH = ASSETS_PATH / "templates"
