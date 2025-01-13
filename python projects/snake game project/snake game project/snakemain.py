import pygame
from snake import Snake
from snake_food import Food

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Set up game variables
snake = Snake(width // 20, height // 20)
food = Food(width // 20, height // 20)
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")

    # Move the snake
    snake.move()

    # Check for collisions with the food
    head = snake.get_head()
    if head[0] == food.position[0] and head[1] == food.position[1]:
        snake.snake_segments.append(snake.snake_segments[-1])  # Extend snake
        food.respawn_food()  # Respawn food in a new position

    # Check for collisions with the walls or itself
    if snake.is_collision():
        running = False

    # Draw the snake and food, and update the display
    screen.fill(black)
    for segment in snake.snake_segments:
        pygame.draw.rect(screen, white, (segment[0] * 20, segment[1] * 20, 20, 20))

    if food.color == "red":
        pygame.draw.rect(screen, red, (food.position[0] * 20, food.position[1] * 20, 20, 20))
    elif food.color == "blue":
        pygame.draw.rect(screen, blue, (food.position[0] * 20, food.position[1] * 20, 20, 20))
    elif food.color == "green":
        pygame.draw.rect(screen, green, (food.position[0] * 20, food.position[1] * 20, 20, 20))

    pygame.display.flip()

    # Set the frame rate
    clock.tick(10)

# Quit pygame
pygame.quit()
