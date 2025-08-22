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

# Function to draw the grid
def draw_grid():
    for x in range(0, width, snake_block):
        pygame.draw.line(dis, grid_color, (x, 0), (x, height))
    for y in range(0, height, snake_block):
        pygame.draw.line(dis, grid_color, (0, y), (width, y))

# Function to draw the snake with head, eyes, tongue, and tail
def draw_snake(snake_list, direction):
    for i, segment in enumerate(snake_list):
        x, y = segment
        center = (x + snake_block // 2, y + snake_block // 2)
        if i == len(snake_list) - 1:  # Head
            pygame.draw.circle(dis, green, center, snake_block // 2)
            # Draw eyes (two small white circles)
            eye_offset = snake_block // 4
            if direction == "RIGHT":
                pygame.draw.circle(dis, white, (x + snake_block // 2 + eye_offset, y + snake_block // 4), 3)
                pygame.draw.circle(dis, white, (x + snake_block // 2 + eye_offset, y + 3 * snake_block // 4), 3)
                pygame.draw.line(dis, red, (x + snake_block, y + snake_block // 2), (x + snake_block + 10, y + snake_block // 2), 2)
            elif direction == "LEFT":
                pygame.draw.circle(dis, white, (x + snake_block // 2 - eye_offset, y + snake_block // 4), 3)
                pygame.draw.circle(dis, white, (x + snake_block // 2 - eye_offset, y + 3 * snake_block // 4), 3)
                pygame.draw.line(dis, red, (x, y + snake_block // 2), (x - 10, y + snake_block // 2), 2)
            elif direction == "UP":
                pygame.draw.circle(dis, white, (x + snake_block // 4, y + snake_block // 2 - eye_offset), 3)
                pygame.draw.circle(dis, white, (x + 3 * snake_block // 4, y + snake_block // 2 - eye_offset), 3)
                pygame.draw.line(dis, red, (x + snake_block // 2, y), (x + snake_block // 2, y - 10), 2)
            elif direction == "DOWN":
                pygame.draw.circle(dis, white, (x + snake_block // 4, y + snake_block // 2 + eye_offset), 3)
                pygame.draw.circle(dis, white, (x + 3 * snake_block // 4, y + snake_block // 2 + eye_offset), 3)
                pygame.draw.line(dis, red, (x + snake_block // 2, y + snake_block), (x + snake_block // 2, y + snake_block + 10), 2)
        elif i == 0:  # Tail
            pygame.draw.circle(dis, green, center, snake_block // 3)
        else:  # Body
            pygame.draw.circle(dis, green, center, snake_block // 2)

# Function to draw food (larger red ball)
def draw_food(food_x, food_y):
    pygame.draw.circle(dis, red, (food_x + snake_block // 2, food_y + snake_block // 2), snake_block // 2)