<p align="right">
  <a href="./README.md">English</a> |
  <a href="./README.pt-BR.md">Português (Brasil)</a>
</p>

<p align="left">
    <a href="#"><img alt="Status do Build" src="https://github.com/your-username/BPSR-Fishing-Bot/actions/workflows/main.yml/badge.svg"></a>
    <a href="#"><img alt="Versão do Projeto" src="https://img.shields.io/badge/version-1.0.0-blue"></a>
    <a href="./LICENSE"><img alt="Licença" src="https://img.shields.io/badge/license-GPL--3.0-brightgreen"></a>
    <a href="https://www.python.org"><img alt="Python" src="https://img.shields.io/badge/Python-3.8+-3776AB?logo=python"></a>
    <a href="https://opencv.org"><img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-4.x-5C3EE8?logo=opencv"></a>
</p>

# BPSR Fishing Bot

Um bot de pesca automatizado e de código aberto, construído em Python. Ele utiliza detecção de imagem para identificar eventos na tela e interagir com o minigame de pesca de um jogo, automatizando todo o processo.

---

## Sumário

*   [Funcionalidades](#funcionalidades)
*   [Guia de Início Rápido](#guia-de-início-rápido)
    *   [Pré-requisitos](#1-pré-requisitos)
    *   [Instalação](#2-instalação)
    *   [Como Executar](#3-como-executar)
*   [Problemas Conhecidos e Soluções](#problemas-conhecidos-e-soluções)
*   [Configuração](#configuração)
*   [Para Desenvolvedores](#para-desenvolvedores)
    *   [Arquitetura](#arquitetura)
    *   [Estrutura do Projeto](#estrutura-do-projeto)
*   [Planos Futuros](#planos-futuros)

---

## Funcionalidades

*   **Pesca Totalmente Automatizada:** Lança a isca, detecta a fisgada e inicia o minigame.
*   **Minigame Player Inteligente:** Joga o minigame de forma autônoma, movendo para a esquerda e para a direita conforme necessário.
*   **Troca Automática de Vara:** Detecta quando a vara de pescar quebra e a substitui por uma nova, permitindo sessões de pesca ininterruptas.
*   **Controle por Hotkeys:** Inicie, pause, retome e encerre o bot facilmente usando teclas de atalho (F1 e F2).
*   **Configuração Flexível:** Permite ajustar facilmente a precisão da detecção, as regiões de interesse (ROI) e os tempos de espera através de arquivos de configuração dedicados.
*   **Arquitetura Robusta:** Construído com uma máquina de estados e princípios de design sólidos, tornando o código fácil de entender e estender.

---

## Guia de Início Rápido

### 1. Pré-requisitos

*   **Python 3.8+**
*   O jogo configurado para rodar em modo janela na resolução **1920x1080**.

### 2. Instalação

1.  Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/BPSR-Fishing-Bot.git
    cd BPSR-Fishing-Bot
    ```

2.  Instale as dependências a partir do `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### 3. Como Executar

1.  Abra o jogo e certifique-se de que ele esteja visível na tela.
2.  Execute o bot a partir da pasta raiz do projeto:
    ```bash
    python main.py
    ```
3.  O bot estará pronto. Pressione **F1** para iniciar/pausar e **F2** para encerrar o bot a qualquer momento.

---

## Problemas Conhecidos e Soluções

Esta seção lista problemas comuns que você pode encontrar e como resolvê-los.

### A detecção de um item (ex: vara quebrada, fisgada) para de funcionar

*   **Sintoma:** O bot para de reagir a um evento específico que antes funcionava, como não trocar a vara quebrada ou não detectar a fisgada.
*   **Causa Provável:** O jogo pode ter recebido uma pequena atualização visual, alterando a aparência do ícone ou da imagem que o bot procura.
*   **Solução:**
    1.  **Tire uma nova captura de tela** da imagem que falhou (ex: o ícone da vara quebrada).
    2.  **Substitua o arquivo de template** correspondente na pasta `src/fishbot/assets/templates/`.
    3.  Se o problema persistir, tente **ajustar o valor de `precision`** no arquivo `src/fishbot/config/detection_config.py`. Diminuir o valor (ex: de `0.8` para `0.7`) pode ajudar a compensar pequenas diferenças visuais.

---

## Configuração

O comportamento do bot pode ser ajustado através dos arquivos localizados em `src/fishbot/config/`.

#### `screen_config.py`
Define a área de captura da tela.
*   `monitor_width`, `monitor_height`: Resolução da tela do jogo (padrão: 1920x1080).
*   `monitor_x`, `monitor_y`: Coordenadas do canto superior esquerdo do monitor onde o jogo está. Para o monitor principal, mantenha `(0, 0)`.

#### `detection_config.py`
Controla a detecção de imagem.
*   `precision`: A confiança mínima (de `0.0` a `1.0`) para que um template seja considerado encontrado.
*   `templates`: Mapeia nomes de eventos para os arquivos de imagem correspondentes em `src/fishbot/assets/templates/`.
*   `rois` (Regiões de Interesse): Define retângulos `(x, y, largura, altura)` para limitar a área de busca de cada template, aumentando a performance e a precisão.

#### `bot_config.py`
Configurações gerais do bot.
*   `state_timeouts`: Tempo máximo que o bot pode permanecer em cada estado antes de resetar.
*   `target_fps`: Limite de capturas de tela por segundo (0 para ilimitado).
*   `default_delay`: Pausas padrão entre as ações.

---

## Para Desenvolvedores

### Arquitetura

O bot utiliza uma **Máquina de Estados Finitos (FSM)** para gerenciar seu fluxo de trabalho. A lógica é dividida da seguinte forma:

*   **`main.py`**: Ponto de entrada que inicializa e executa o bot.
*   **`src/fishbot/core/state/`**: Contém a lógica da máquina de estados.
    *   `state_machine.py`: Gerencia o estado atual e as transições.
    *   `impl/`: Abriga as classes para cada estado concreto (`CheckingRodState`, `PlayingMinigameState`, etc.), onde cada uma implementa uma única responsabilidade.
*   **`src/fishbot/core/game/`**: Módulos que interagem diretamente com o jogo.
    *   `detector.py`: Responsável pela captura de tela e detecção de templates usando `mss` e `OpenCV`.
    *   `controller.py`: Simula entradas de teclado e mouse.
*   **`src/fishbot/utils/`**: Utilitários, como a função de log.

### Estrutura do Projeto

```
BPSR-Fishing-Bot/
├── src/
│   └── fishbot/
│       ├── assets/         # Imagens (templates) para detecção
│       ├── config/         # Arquivos de configuração do bot
│       ├── core/
│       │   ├── game/       # Módulos de interação com o jogo (Detector, Controller)
│       │   └── state/      # Lógica da Máquina de Estados
│       ├── ui/             # (Reservado para futura interface gráfica)
│       └── utils/          # Módulos utilitários
├── .gitignore
├── main.py                 # Ponto de entrada da aplicação
├── README.md
└── requirements.txt
```

## Planos Futuros

*   [ ] Interface gráfica (GUI) para facilitar a configuração.
*   [x] Sistema de hotkeys para iniciar/parar o bot.
*   [ ] Melhorar a resiliência a eventos inesperados no jogo.

---

Sinta-se à vontade para abrir uma *issue* ou enviar uma *pull request*!