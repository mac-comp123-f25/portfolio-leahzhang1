import pygame, random, sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Blocks")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player
player = pygame.Rect(230, 350, 40, 40)
speed = 7

# Blocks
blocks = []
for _ in range(5):
    blocks.append(pygame.Rect(random.randint(0, WIDTH - 30), random.randint(-150, 0), 30, 30))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-speed, 0)
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.move_ip(speed, 0)

    # Move blocks
    for block in blocks:
        block.move_ip(0, 5)
        if block.top > HEIGHT:
            block.top = random.randint(-100, -40)
            block.left = random.randint(0, WIDTH - 30)

    # Check collisions
    for block in blocks:
        if player.colliderect(block):
            print("💥 Game Over!")
            pygame.quit()
            sys.exit()

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)
    for block in blocks:
        pygame.draw.rect(screen, RED, block)

    pygame.display.flip()
    clock.tick(30)
