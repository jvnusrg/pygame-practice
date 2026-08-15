import pygame

pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("My first Pygame Window")

x = 50
y = 200
width = 60
height = 60
speed_x = 3
speed_y = 3

paddle_x = 20
paddle_y = 200
paddle_width = 15
paddle_height = 100
paddle_speed =5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x = x + speed_x
    y = y + speed_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_y = paddle_y - paddle_speed
    if keys[pygame.K_s]:
        paddle_y = paddle_y + paddle_speed
    #if x <= 0 or x + width >= 640:
        #speed_x = speed_x * -1
    if y <=0 or y + height >= 480:
        speed_y = speed_y * -1

    screen.fill((20, 60, 30))

    pygame.draw.rect(screen, (200,200,60), (x, y, width, height))

    pygame.draw.rect(screen, (255,255,255),(paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.display.flip()

pygame.quit()