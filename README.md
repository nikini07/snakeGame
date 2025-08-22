# Snake Game

A classic Snake game built with Python and Pygame, featuring a green snake with a distinct head (white eyes, red tongue) and tail, a brown background with a sienna grid, red food balls, and dynamic speed that increases with score.

## Features

Visuals: Green snake with a detailed head (white eyes, red tongue) and smaller tail, red food balls, brown background (#8B4513), and sienna grid (#A0522D) for alignment.
Gameplay: Control the snake with arrow keys to collect food, grow, and score points. The snake starts stationary and moves only after a key press.
Dynamic Speed: Starts at 8 FPS, increases by 1 FPS every 5 points, up to 15 FPS.
UI: Displays score in-game, with a game-over screen offering "Retry" and "Quit" buttons (olive drab, with olive green hover).
Debugging: Includes console prints to diagnose issues like immediate game-over.

## Prerequisites

Python 3.12: Install via python.org or Homebrew (brew install python@3.12).
Pygame: Install with python3.12 -m pip install pygame.
Git: Required to clone the repository.

## Gameplay

Start: The snake (green, with head and tail) appears stationary at the center of a brown grid.
Controls: Press arrow keys (left, right, up, down) to move.
Objective: Collect red food balls to grow and score. Speed increases every 5 points (8 to 15 FPS).
Game Over: Triggered by hitting walls or the snake’s body. Click "Retry" to restart or "Quit" to exit.

