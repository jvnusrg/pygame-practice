import pygame

pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("My first Pygame Window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 60, 30))
    pygame.display.flip()

pygame.quit()