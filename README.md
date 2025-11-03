<p align="right">
  <a href="./README.pt-br.md.md">Português (Brasil)</a>
</p>

<p align="left">    
    <a href="#"><img alt="Project Version" src="https://img.shields.io/badge/version-1.0.0-blue"></a>
    <a href="./LICENSE"><img alt="License" src="https://img.shields.io/badge/license-GPL--3.0-brightgreen"></a>
    <a href="https://www.python.org"><img alt="Python" src="https://img.shields.io/badge/Python-3.8+-3776AB?logo=python"></a>
    <a href="https://opencv.org"><img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-4.x-5C3EE8?logo=opencv"></a>
</p>

# BPSR: Fishing Bot

An automated and open-source fishing bot built in Python. It uses image detection to identify on-screen events and interact with a game's fishing minigame, automating the entire process.

---

##  Table of Contents

*   [Features](#features)
*   [Quick Start Guide](#quick-start-guide)
    *   [Prerequisites](#1-prerequisites)
    *   [Installation](#2-installation)
    *   [How to Run](#3-how-to-run)
*   [Known Issues and Solutions](#known-issues-and-solutions)
*   [Configuration](#configuration)
*   [For Developers](#for-developers)
    *   [Architecture](#architecture)
    *   [Project Structure](#project-structure)
*   [Future Plans](#future-plans)

---

## Features

*   **Fully Automated Fishing:** Casts the line, detects a bite, and starts the minigame.
*   **Smart Minigame Player:** Autonomously plays the fishing minigame, moving left and right as needed.
*   **Automatic Rod Swapping:** Detects when the fishing rod breaks and replaces it with a new one, allowing for uninterrupted fishing sessions.
*   **Flexible Configuration:** Allows for easy adjustment of detection precision, regions of interest (ROI), and wait times through dedicated configuration files.
*   **Robust Architecture:** Built with a state machine and solid design principles, making the code easy to understand and extend.

---

## Quick Start Guide

### 1. Prerequisites

*   **Python 3.8+**
*   The game configured to run in windowed mode at **1920x1080** resolution (for now...).

### 2. Installation

1.  Clone this repository:
    ```bash
    git clone https://github.com/your-username/BPSR-Fishing-Bot.git
    cd BPSR-Fishing-Bot
    ```

2.  Install the dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### 3. How to Run

1.  Open the game and make sure it is visible on the screen.
2.  Run the bot from the project's root folder:
    ```bash
    python main.py
    ```
3.  The bot will start running. To stop it, press `Ctrl+C` in the terminal.

---

## Known Issues and Solutions

This section lists common issues you might encounter and how to solve them.

### The detection of an item (e.g., broken rod, fish bite) stops working

*   **Symptom:** The bot stops reacting to a specific event that used to work, such as not swapping a broken rod or not detecting a bite.
*   **Likely Cause:** The game may have received a minor visual update, changing the appearance of the icon or image the bot is looking for.
*   **Solution:**
    1.  **Take a new screenshot** of the failed image (e.g., the broken rod icon).
    2.  **Replace the corresponding template file** in the `src/fishbot/assets/templates/` folder.
    3.  If the problem persists, try **adjusting the `precision` value** in the `src/fishbot/config/detection_config.py` file. Lowering the value (e.g., from `0.8` to `0.7`) can help compensate for minor visual differences.

---

## Configuration

The bot's behavior can be adjusted through the files located in `src/fishbot/config/`.

#### `screen_config.py`
Defines the screen capture area.
*   `monitor_width`, `monitor_height`: The game's screen resolution (default: 1920x1080).
*   `monitor_x`, `monitor_y`: Coordinates of the top-left corner of the monitor where the game is running. For the primary monitor, keep this as `(0, 0)`.

#### `detection_config.py`
Controls image detection.
*   `precision`: The minimum confidence (from `0.0` to `1.0`) for a template to be considered a match.
*   `templates`: Maps event names to their corresponding image files in `src/fishbot/assets/templates/`.
*   `rois` (Regions of Interest): Defines rectangles `(x, y, width, height)` to limit the search area for each template, increasing performance and accuracy.

#### `bot_config.py`
General bot settings.
*   `state_timeouts`: Maximum time the bot can remain in each state before resetting.
*   `target_fps`: Target frames per second for screen captures (0 for unlimited).
*   `default_delay`: Default delays between actions.

---

## For Developers

### Architecture

The bot uses a **Finite State Machine (FSM)** to manage its workflow. The logic is divided as follows:

*   **`main.py`**: The entry point that initializes and runs the bot.
*   **`src/fishbot/core/state/`**: Contains the state machine logic.
    *   `state_machine.py`: Manages the current state and transitions.
    *   `impl/`: Houses the classes for each concrete state (`CheckingRodState`, `PlayingMinigameState`, etc.), where each implements a single responsibility.
*   **`src/fishbot/core/game/`**: Modules that interact directly with the game.
    *   `detector.py`: Responsible for screen capture and template detection using `mss` and `OpenCV`.
    *   `controller.py`: Simulates keyboard and mouse inputs.
*   **`src/fishbot/utils/`**: Utility modules, such as the logger function.

### Project Structure

```
BPSR-Fishing-Bot/
├── src/
│   └── fishbot/
│       ├── assets/         # Images (templates) for detection
│       ├── config/         # Bot configuration files
│       ├── core/
│       │   ├── game/       # Game interaction modules (Detector, Controller)
│       │   └── state/      # State Machine Logic
│       ├── ui/             # (Reserved for a future GUI)
│       └── utils/          # Utility modules
├── .gitignore
├── main.py                 # Application entry point
├── README.md
└── requirements.txt
```

## Future Plans

*   [ ] Graphical user interface (GUI) for easier configuration.
*   [ ] Hotkey system to start/stop the bot.
*   [ ] Improve resilience to unexpected in-game events.
*   [ ] Add a State to buy baits and rods.

---

Feel free to open an *issue* or submit a *pull request*!