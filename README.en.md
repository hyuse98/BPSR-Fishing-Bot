# BPSR Fishing Bot

An automated fishing bot built in Python that uses image detection to play the fishing minigame in a game.

## Features

*   **Automated Fishing:** Casts the line and waits for a bite.
*   **Minigame Player:** Plays the fishing minigame by moving left and right.
*   **Rod Switching:** Detects when the fishing rod breaks and replaces it with a new one.
*   **Highly Configurable:** Allows adjusting detection precision, regions of interest (ROI), and wait times.

## Quick Start Guide

### 1. Prerequisites and Installation

1.  **Python:** Make sure you have [Python 3](https://www.python.org/downloads/) installed.
2.  **Dependencies:** Install the required libraries by running the following command in your terminal:
    ```bash
    pip install opencv-python pyautogui mss
    ```

### 2. How to Run

1.  Open the game.
2.  Navigate to the project's root folder in your terminal.
3.  Run the following command:
    ```bash
    python main.py
    ```
4.  You will have 5 seconds to click on the game window and bring it into focus before the bot starts operating.
5.  To stop the bot, press `Ctrl+C` in the terminal.

## Essential Configuration

Before running, you **must** check the screen settings in the `fishbot/config.py` file.

*   **`monitor_width`, `monitor_height`**: Set your game's screen resolution (e.g., 1920, 1080).
*   **`monitor_x`, `monitor_y`**: Defines which monitor the game is on.
    *   **Main Monitor:** Keep `monitor_x = 0` and `monitor_y = 0`.
    *   **Monitor to the Right:** If your main monitor is 1920px wide, use `monitor_x = 1920`.
    *   **Monitor to the Left:** If the game monitor is 1920px wide, use `monitor_x = -1920`.

---

## For Developers and Contributors

This section contains technical information about the bot's internal workings.

### Architecture and Technical Details

The bot is designed with a modular architecture for easy maintenance and extension. The main components are:

*   **State Machine:** The core of the bot is a finite state machine. The `FishingBot` class (`fishbot/bot.py`) acts as the "Context," managing the current state (e.g., "fishing," "playing minigame"). The classes in the `fishbot/states/` directory implement the logic for each state.

*   **Detector (`detector.py`):** This component is responsible for "seeing" the game screen. It uses `mss` for high-performance screenshots and `opencv-python` for image detection, comparing templates from the `assets/` folder with the screen capture.

*   **Controller (`controller.py`):** This module simulates user input (keyboard and mouse) using `pyautogui` to perform actions in the game.

### Project Structure

```
BPSR Fishing Bot/
├── assets/                 # Contains the images (templates) for detection
├── fishbot/                # Main source code for the bot
│   ├── states/             # Logic for each bot state
│   ├── bot.py              # Main class (State Machine Context)
│   ├── config.py           # Main configuration file
│   ├── controller.py       # Keyboard and mouse simulation
│   └── detector.py         # Screen capture and image detection
├── main.py                 # Entry point to run the bot
└── README.md               # This documentation
```

### Advanced Configuration

The `fishbot/config.py` file contains more options to optimize the bot:

*   **`precision`**: The minimum confidence (`0.0` to `1.0`) for image detection. The default is `0.7`.
*   **`rois` (Regions of Interest)**: Defines a rectangular area `(x, y, width, height)` to optimize the search for an image, increasing performance and accuracy.
*   **`templates`**: A dictionary that maps template names to their files in the `assets/` folder.

## Future Plans

*(This section is reserved for future ideas and improvements. Feel free to add your suggestions!)*

*   [ ] Hotkeys
*   [ ] GUI
*   [ ] Refinements
