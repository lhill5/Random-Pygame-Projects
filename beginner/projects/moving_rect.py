import pygame
import time

pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

x, y = 50, 50
width, height = 40, 60
velocity = 5
clock = pygame.time.Clock()
jumpCount = 10
jump = False

run = True
while run:
    #pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x > velocity:
            x -= velocity
    if keys[pygame.K_RIGHT]:
        if x < 500 - width - velocity:
            x += velocity
    if not jump:
        if keys[pygame.K_UP]:
            if y > velocity:
                y -= velocity
        if keys[pygame.K_DOWN]:
            if y < 500 - height - velocity:
                y += velocity
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            jump = False



    window.fill((0,0,0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
