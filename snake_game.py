import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors (RGB)
white = (255, 255, 255)
black = (0, 0, 0)
green = (34, 139, 34)  # Forest green for snake
red = (200, 0, 0)      # Dark red for food and tongue
brown = (139, 69, 19)  # Saddle brown for background
grid_color = (160, 82, 45)  # Sienna for grid lines
text_color = (255, 255, 255)  # White for text
button_color = (85, 107, 47)   # Olive drab for buttons
button_hover = (107, 142, 35)  # Olive green for button hover

# Set display dimensions
width = 800
height = 600
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Game settings
snake_block = 20  # Size of snake segments and food
base_speed = 8    # Starting speed (slower for beginners)
max_speed = 15    # Maximum speed as score increases
font = pygame.font.SysFont("arial", 30, bold=True)
score_font = pygame.font.SysFont("arial", 35, bold=True)