import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Snake properties
snake_block = 10
snake_speed = 15

# Initialize the snake
snake = [(width // 2, height // 2)]
snake_direction = "RIGHT"

# Initialize the food
food = (random.randrange(1, (width // snake_block)) * snake_block,
        random.randrange(1, (height // snake_block)) * snake_block)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for arrow key presses to change snake direction
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    # Move the snake
    if snake_direction == "UP":
        snake.insert(0, (snake[0][0], snake[0][1] - snake_block))
    elif snake_direction == "DOWN":
        snake.insert(0, (snake[0][0], snake[0][1] + snake_block))
    elif snake_direction == "LEFT":
        snake.insert(0, (snake[0][0] - snake_block, snake[0][1]))
    elif snake_direction == "RIGHT":
        snake.insert(0, (snake[0][0] + snake_block, snake[0][1]))

    # Check for collisions with the window boundaries
    if (
        snake[0][0] < 0
        or snake[0][0] >= width
        or snake[0][1] < 0
        or snake[0][1] >= height
    ):
        pygame.quit()
        sys.exit()

    # Check for collision with the food
    if snake[0] == food:
        food = (random.randrange(1, (width // snake_block)) * snake_block,
                random.randrange(1, (height // snake_block)) * snake_block)
    else:
        # If no collision with food, remove the last segment to keep the snake the same length
        snake.pop()

    # Draw the window
    win.fill(black)
    pygame.draw.rect(win, red, [food[0], food[1], snake_block, snake_block])

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(win, white, [segment[0], segment[1], snake_block, snake_block])

    # Update the display
    pygame.display.update()

    # Control snake speed
    clock.tick(snake_speed)

# End of the game loop
