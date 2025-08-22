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
    
    # Function to display score
def show_score(score):
    score_text = score_font.render(f"Score: {score}", True, text_color)
    dis.blit(score_text, [10, 10])

# Function to display game over screen
def game_over_screen(score):
    dis.fill(brown)
    draw_grid()
    game_over_text = font.render("Game Over!", True, text_color)
    score_text = font.render(f"Final Score: {score}", True, text_color)
    retry_text = font.render("Retry", True, white)
    quit_text = font.render("Quit", True, white)
    
    retry_rect = pygame.Rect(width // 2 - 100, height // 2, 80, 40)
    quit_rect = pygame.Rect(width // 2 + 20, height // 2, 80, 40)
    
    mouse_pos = pygame.mouse.get_pos()
    retry_color = button_hover if retry_rect.collidepoint(mouse_pos) else button_color
    quit_color = button_hover if quit_rect.collidepoint(mouse_pos) else button_color
    
    dis.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 3))
    dis.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 3 + 50))
    pygame.draw.rect(dis, retry_color, retry_rect)
    pygame.draw.rect(dis, quit_color, quit_rect)
    dis.blit(retry_text, (retry_rect.x + 15, retry_rect.y + 5))
    dis.blit(quit_text, (quit_rect.x + 15, quit_rect.y + 5))
    
    pygame.display.update()
    return retry_rect, quit_rect

# Main game loop
def game_loop():
    game_over = False
    game_close = False
    first_frame = True  # Skip collision check on first frame
    
    # Initialize snake position and direction
    x1 = (width // snake_block // 2) * snake_block  # 400
    y1 = (height // snake_block // 2) * snake_block  # 300
    x1_change = 0
    y1_change = 0
    direction = "RIGHT"
    
    snake_list = []
    snake_length = 2  # Start with head and tail
    snake_list.append([x1 - snake_block, y1])  # Tail at [380, 300]
    snake_list.append([x1, y1])               # Head at [400, 300]
    
    food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
    
    # Ensure food doesn't spawn on snake
    while [food_x, food_y] in snake_list:
        food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
        food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
    
    clock = pygame.time.Clock()
    
    while not game_over:
        while game_close:
            retry_rect, quit_rect = game_over_screen(snake_length - 2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if retry_rect.collidepoint(event.pos):
                        return True  # Restart game
                    if quit_rect.collidepoint(event.pos):
                        return False  # Quit game
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                    direction = "RIGHT"
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                    direction = "UP"
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0
                    direction = "DOWN"
        
        # Only update position if movement has started
        if x1_change != 0 or y1_change != 0:
            x1 += x1_change
            y1 += y1_change
            snake_head = [x1, y1]
            snake_list.append(snake_head)
            if len(snake_list) > snake_length:
                del snake_list[0]
        
        # Check boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        
        # Check self-collision (skip on first frame)
        if not first_frame and (x1_change != 0 or y1_change != 0):
            for segment in snake_list[:-1]:
                if segment == snake_head:
                    game_close = True
        
        # Update display
        dis.fill(brown)
        draw_grid()
        draw_food(food_x, food_y)
        draw_snake(snake_list, direction)
        show_score(snake_length - 2)
        pygame.display.update()
        
        # Check if food is eaten
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
            while [food_x, food_y] in snake_list:
                food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
                food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
            snake_length += 1
        
        # Adjust speed based on score
        score = snake_length - 2
        speed = base_speed + (score // 5)  # Increase speed every 5 points
        if speed > max_speed:
            speed = max_speed
        clock.tick(speed)
        
        first_frame = False
        
        # Debug: Print state after each update
        print(f"Frame: Head=[{x1}, {y1}], Snake={snake_list}, Moving={direction}")
    
    pygame.quit()
    return False

# Run the game
while True:
    if not game_loop():
        break
    
