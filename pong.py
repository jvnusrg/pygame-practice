import pygame

pygame.init()
font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()

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

paddle2_x = 605
paddle2_y = 200
paddle2_width = 15
paddle2_height = 100
paddle2_speed = 5

left_score = 0
right_score = 0

pause = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause

    if not pause:
        x = x + speed_x
        y = y + speed_y

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle_y = paddle_y - paddle_speed
        if keys[pygame.K_s]:
            paddle_y = paddle_y + paddle_speed

        if paddle_y < 0:
            paddle_y = 0
        if paddle_y + paddle_height > 480:
            paddle_y = 480 - paddle_height

        if keys[pygame.K_UP]:
            paddle2_y = paddle2_y - paddle2_speed
        if keys[pygame.K_DOWN]:
            paddle2_y = paddle2_y + paddle2_speed

        if paddle2_y < 0:
            paddle2_y =0
        if paddle2_y + paddle2_height > 480:
            paddle2_y = 480 - paddle2_height
        
        #if x <= 0 or x + width >= 640:
            #speed_x = speed_x * -1
        if y <=0 or y + height >= 480:
            speed_y = speed_y * -1

        ball_rect = pygame.Rect(x, y, width, height)
        paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
        paddle2_rect = pygame.Rect(paddle2_x, paddle2_y, paddle2_width, paddle2_height)

        if ball_rect.colliderect(paddle_rect) or ball_rect.colliderect(paddle2_rect):
            speed_x = speed_x * -1

        if x < 0:
            right_score = right_score + 1
            print("Right player scores!")
            x = 320
            y = 200
            speed_x = speed_x * -1

        if x > 640:
            print("Left player scores!")
            left_score = left_score + 1
            x = 320
            y = 200
            speed_x = speed_x * -1   

        screen.fill((20, 60, 30))

        left_text = font.render(str(left_score), True,(255,255,255))
        right_text = font.render(str(right_score),True, (255,255,255))

        screen.blit(left_text,(270, 20))
        screen.blit(right_text,(350,20))

        for dash_y in range (0, 480, 20):
            pygame.draw.rect(screen, (255,255,255), (320-2, dash_y, 4, 10))
    
        pygame.draw.circle(screen, (200,200,60), (int(x + width // 2), int(y + height // 2)), width // 2)

        pygame.draw.rect(screen, (255,255,255),(paddle_x, paddle_y, paddle_width, paddle_height))

        pygame.draw.rect(screen, (100,200,255),(paddle2_x, paddle2_y, paddle2_width, paddle2_height))
        pygame.display.flip()

        clock.tick(60)

pygame.quit()