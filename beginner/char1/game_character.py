import pygame
import os

pygame.init()
win = pygame.display.set_mode((500,480))

walkRight = [
    pygame.image.load('R1.png'),
    pygame.image.load('R2.png'),
    pygame.image.load('R3.png'),
    pygame.image.load('R4.png'),
    pygame.image.load('R5.png'),
    pygame.image.load('R6.png'),
    pygame.image.load('R7.png'),
    pygame.image.load('R8.png'),
    pygame.image.load('R9.png')
]

walkLeft = [
pygame.image.load('L1.png'),
pygame.image.load('L2.png'),
pygame.image.load('L3.png'),
pygame.image.load('L4.png'),
pygame.image.load('L5.png'),
pygame.image.load('L6.png'),
pygame.image.load('L7.png'),
pygame.image.load('L8.png'),
pygame.image.load('L9.png')]

bg = pygame.image.load('bg.jpg')
character = pygame.image.load('standing.png')

clock = pygame.time.Clock()
width = 64
height = 64
x = 50
y = 480 - height
vel = 5
jump = False
jumpCount = 8
left = False
right = False
walkCount = 0

def drawGameWindow():
    global walkCount
    win.blit(bg, (0,0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3],(x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(character, (x,y))

    pygame.display.update()

run = True
while run:
    clock.tick(27)
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0
    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -8:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 8
            jump = False

    drawGameWindow()


pygame.quit()
