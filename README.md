# snakeGame
Snake Game Project
A classic Snake game built with Python and Pygame, featuring a green snake with a distinct head (white eyes, red tongue) and tail, a brown background with a sienna grid, red food balls, and dynamic speed that increases with score.
Features

Visuals: Green snake with a detailed head (white eyes, red tongue) and smaller tail, red food balls, brown background (#8B4513), and sienna grid (#A0522D) for alignment.
Gameplay: Control the snake with arrow keys to collect food, grow, and score points. The snake starts stationary and moves only after a key press.
Dynamic Speed: Starts at 8 FPS, increases by 1 FPS every 5 points, up to 15 FPS.
UI: Displays score in-game, with a game-over screen offering "Retry" and "Quit" buttons (olive drab, with olive green hover).
Debugging: Includes console prints to diagnose issues like immediate game-over.

Prerequisites

Python 3.12: Install via python.org or Homebrew (brew install python@3.12).
Pygame: Install with python3.12 -m pip install pygame.
Git: Required to clone the repository.

Installation

Clone the Repository:
git clone https://github.com/nikkisusername/snake-game-project.git
cd snake-game-project


Replace nikkisusername with your GitHub username.
Use a Personal Access Token (PAT) for authentication (see GitHub PAT Guide).


Install Dependencies:
python3.12 -m pip install pygame



Running the Game
python3.12 snake_game.py

Gameplay

Start: The snake (green, with head and tail) appears stationary at the center of a brown grid.
Controls: Press arrow keys (left, right, up, down) to move.
Objective: Collect red food balls to grow and score. Speed increases every 5 points (8 to 15 FPS).
Game Over: Triggered by hitting walls or the snake’s body. Click "Retry" to restart or "Quit" to exit.

Troubleshooting

Immediate Game-Over: If the game shows the game-over screen instantly:

Check console output for debug prints (e.g., Boundary collision: Head=[x, y] or Self-collision: Head=[x, y]).

Ensure the snake starts at [400, 300] and remains stationary until a key press.

Run a Pygame test:
import pygame
pygame.init()
dis = pygame.display.set_mode((800, 600))
dis.fill((139, 69, 19))
pygame.display.update()
pygame.time.wait(2000)
pygame.quit()

Save as test.py and run: python3.12 test.py. If no brown window appears, reinstall Pygame.



Authentication Issues: If cloning/pushing fails, generate a PAT:

Go to github.com/settings/tokens.
Create a token with repo scope.
Use it as the password when prompted.



Authentication
GitHub requires a Personal Access Token (PAT) for HTTPS Git operations:

Go to github.com/settings/tokens > Generate new token (classic).
Select repo scope, generate, and copy the token.
Use it when prompted for a password during git clone or git push.

Development

Commits: The project was developed in stages:
Initial .gitignore and README.
Pygame setup and colors.
Grid and drawing functions (snake, food).
Score and game-over UI.
Main game loop with fixes for immediate game-over.
Debug prints for troubleshooting.


Contributing: Fork the repo, make changes, and submit a pull request.

License
MIT License (or specify your preferred license).