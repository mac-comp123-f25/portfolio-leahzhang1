import pygame, sys, random

pygame.init()

# Screen setup
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Colors
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# Snake and food setup
snake = [(100, 50), (90, 50), (80, 50)]
snake_dir = "RIGHT"
food = (random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10)


def move_snake(snake, direction):
    x, y = snake[0]
    if direction == "UP":
        y -= 10
    elif direction == "DOWN":
        y += 10
    elif direction == "LEFT":
        x -= 10
    elif direction == "RIGHT":
        x += 10
    new_head = (x, y)
    snake.insert(0, new_head)
    return snake


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != "DOWN":
                snake_dir = "UP"
            elif event.key == pygame.K_DOWN and snake_dir != "UP":
                snake_dir = "DOWN"
            elif event.key == pygame.K_LEFT and snake_dir != "RIGHT":
                snake_dir = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_dir != "LEFT":
                snake_dir = "RIGHT"

    snake = move_snake(snake, snake_dir)

    # Check for collisions
    if snake[0] == food:
        food = (random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10)
    else:
        snake.pop()

    if (snake[0][0] < 0 or snake[0][0] >= width or
            snake[0][1] < 0 or snake[0][1] >= height or
            len(snake) != len(set(snake))):
        pygame.quit()
        sys.exit()

    # Draw
    screen.fill(black)
    for s in snake:
        pygame.draw.rect(screen, green, pygame.Rect(s[0], s[1], 10, 10))
    pygame.draw.rect(screen, red, pygame.Rect(food[0], food[1], 10, 10))

    pygame.display.flip()
    clock.tick(15)
