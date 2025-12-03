import pygame, random, sys

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player
player = pygame.Rect(100, HEIGHT // 2, 30, 30)
gravity = 0.5
velocity = 0

# Pipes
pipes = []


def new_pipe():
    gap = 150
    top_height = random.randint(100, 400)
    pipes.append(pygame.Rect(WIDTH, 0, 50, top_height))
    pipes.append(pygame.Rect(WIDTH, top_height + gap, 50, HEIGHT - (top_height + gap)))


new_pipe()
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            velocity = -8  # jump

    # Gravity
    velocity += gravity
    player.y += int(velocity)

    # Move pipes
    for pipe in pipes:
        pipe.x -= 4
    if pipes[0].x < -60:
        pipes = []
        new_pipe()
        score += 1

    # Collisions
    for pipe in pipes:
        if player.colliderect(pipe):
            print(f"💥 Game Over! Final Score: {score}")
            pygame.quit()
            sys.exit()
    if player.y > HEIGHT or player.y < 0:
        print(f"💥 Game Over! Final Score: {score}")
        pygame.quit()
        sys.exit()

    # Draw
    screen.fill((135, 206, 250))
    pygame.draw.rect(screen, (255, 255, 0), player)
    for pipe in pipes:
        pygame.draw.rect(screen, (0, 200, 0), pipe)


    pygame.display.flip()
    clock.tick(30)
