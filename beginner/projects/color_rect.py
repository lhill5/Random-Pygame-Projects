import pygame
import time

pygame.init()
window = pygame.display.set_mode((500,500))

rectange = pygame.Rect(20, 50, 50, 50)
rect_color = (0, 128, 255)

run = True
original_color = True
x, y = 250, 250
clock = pygame.time.Clock()

while run:
    #pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            original_color = not original_color
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        x -= 3
    if pressed_keys[pygame.K_RIGHT]:
        x += 3
    if pressed_keys[pygame.K_UP]:
        y -= 3
    if pressed_keys[pygame.K_DOWN]:
        y += 3

    if original_color:
        rect_color = (0, 128, 255)
    else:
        rect_color = (255, 100, 0)
    window.fill((0,0,0))

    pygame.draw.rect(window, rect_color, pygame.Rect(x, y, 50, 50))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
