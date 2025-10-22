import pygame, sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Paddle
paddle = pygame.Rect(250, 350, 100, 10)
ball = pygame.Rect(300, 200, 10, 10)
speed_x, speed_y = 4, -4

# Bricks
bricks = [pygame.Rect(x * 60 + 10, y * 20 + 10, 50, 10) for y in range(5) for x in range(10)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-6, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(6, 0)

    ball.x += speed_x
    ball.y += speed_y

    # Wall collisions
    if ball.left <= 0 or ball.right >= WIDTH:
        speed_x = -speed_x
    if ball.top <= 0:
        speed_y = -speed_y
    if ball.bottom >= HEIGHT:
        print("💥 Game Over!")
        pygame.quit()
        sys.exit()

    # Paddle bounce
    if ball.colliderect(paddle):
        speed_y = -speed_y

    # Brick collisions
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            speed_y = -speed_y
            break

    # Draw
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.draw.ellipse(screen, (255, 0, 0), ball)
    for brick in bricks:
        pygame.draw.rect(screen, (0, 255, 0), brick)

    pygame.display.flip()
    clock.tick(60)
