# BPSR Fishing Bot

Um bot de pesca automatizado construído em Python que utiliza detecção de imagem para jogar o minigame de pesca em um jogo.

## Funcionalidades

*   **Pesca Automatizada:** Lança a isca e espera por uma fisgada.
*   **Minigame Player:** Joga o minigame de pesca movendo para a esquerda e para a direita.
*   **Troca de Vara:** Detecta quando a vara de pescar quebra e a substitui por uma nova.
*   **Altamente Configurável:** Permite ajustar a precisão da detecção, as regiões de interesse (ROI) e os tempos de espera.

## Guia de Início Rápido

### 1. Pré-requisitos e Instalação

1.  **Python:** Certifique-se de ter o [Python 3](https://www.python.org/downloads/) instalado.
2.  **Dependências:** Instale as bibliotecas necessárias executando o seguinte comando no seu terminal:
    ```bash
    pip install opencv-python pyautogui mss
    ```

### 2. Como Executar

1.  Abra o jogo.
2.  Navegue até a pasta raiz do projeto no seu terminal.
3.  Execute o seguinte comando:
    ```bash
    python main.py
    ```
4.  Você terá 5 segundos para clicar na janela do jogo e deixá-la em foco antes que o bot comece a operar.
5.  Para parar o bot, pressione `Ctrl+C` no terminal.

## Configuração Essencial

Antes de executar, você **precisa** verificar as configurações de tela no arquivo `fishbot/config.py`.


*   **`monitor_width`, `monitor_height`**: Defina a resolução da tela do seu jogo (ex: 1920, 1080).
*   **`monitor_x`, `monitor_y`**: Define em qual monitor o jogo está.
    *   **Monitor Principal:** Mantenha `monitor_x = 0` e `monitor_y = 0`.
    *   **Monitor à Direita:** Se seu monitor principal tem 1920px de largura, use `monitor_x = 1920`.
    *   **Monitor à Esquerda:** Se o monitor do jogo tem 1920px de largura, use `monitor_x = -1920`.

---

## Para Desenvolvedores e Contribuintes

Esta seção contém informações técnicas sobre o funcionamento interno do bot.

### Arquitetura e Detalhes Técnicos

O bot foi projetado com uma arquitetura modular para facilitar a manutenção e a extensão. Os componentes principais são:

*   **Máquina de Estados (State Machine):** O núcleo do bot é uma máquina de estados finitos. A classe `FishingBot` (`fishbot/bot.py`) atua como o "Contexto", gerenciando o estado atual (ex: "pescando", "jogando minigame"). As classes no diretório `fishbot/states/` implementam a lógica para cada estado.

*   **Detector (`detector.py`):** Este componente é responsável por "ver" a tela do jogo. Ele usa `mss` para capturas de tela de alta performance e `opencv-python` para detecção de imagem, comparando templates da pasta `assets/` com a captura de tela.

*   **Controlador (`controller.py`):** Este módulo simula a entrada do usuário (teclado e mouse) usando `pyautogui` para executar ações no jogo.

### Estrutura do Projeto

```
BPSR Fishing Bot/
├── assets/                 # Contém as imagens (templates) para detecção
├── fishbot/                # Código fonte principal do bot
│   ├── states/             # Lógica para cada estado do bot
│   ├── bot.py              # Classe principal (Contexto da Máquina de Estados)
│   ├── config.py           # Arquivo de configuração principal
│   ├── controller.py       # Simulação de teclado e mouse
│   └── detector.py         # Captura de tela e detecção de imagem
├── main.py                 # Ponto de entrada para executar o bot
└── README.md               # Esta documentação
```

### Configuração Avançada

O arquivo `fishbot/config.py` contém mais opções para otimizar o bot:

*   **`precision`**: A confiança mínima (`0.0` a `1.0`) para a detecção de imagem. O padrão é `0.7`.
*   **`rois` (Regiões de Interesse)**: Define uma área retangular `(x, y, largura, altura)` para otimizar a busca por uma imagem, aumentando a performance e a precisão.
*   **`templates`**: Dicionário que mapeia nomes de templates aos seus arquivos na pasta `assets/`.

## Planos Futuros

*(Esta seção está reservada para futuras ideias e melhorias. Sinta-se à vontade para adicionar suas sugestões!)*

*   [ ] Hotkeys
*   [ ] GUI
*   [ ] Refinamentos
