import pygame, random, sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x, y = WIDTH // 2, HEIGHT // 2
speed_x, speed_y = 5, 3
color = (255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x += speed_x
    y += speed_y

    # Bounce logic
    if x <= 0 or x >= WIDTH:
        speed_x = -speed_x
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if y <= 0 or y >= HEIGHT:
        speed_y = -speed_y
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, color, (x, y), 20)
    pygame.display.flip()
    clock.tick(60)
