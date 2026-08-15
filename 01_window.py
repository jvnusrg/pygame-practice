import pygame

pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("My first Pygame Window")

x = 50
y = 200
width = 60
height = 60
speed = 3


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x = x + speed

    if x <= 0 or x + width >= 640:
        speed = speed * -1
    screen.fill((20, 60, 30))

    pygame.draw.rect(screen, (200,200,60), (x, y, width, height))

    pygame.display.flip()

pygame.quit()