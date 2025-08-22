import pygame
import random

# Initialize Pygame
pygame.init()

Set display width and height
dis_width = 800
dis_height = 600

# Create the display surface
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Clock to control the speed of the game
clock = pygame.time.Clock()

# Snake block size and speed
snake_block = 10
snake_speed = 15

