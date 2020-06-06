import pygame
import time

pygame.init()

white = (255,255,255)

screen_width = 500
screen_height = 500
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('player movement')

clock = pygame.time.Clock()
character = pygame.image.load('standing.png')
walkLeft = [
    pygame.image.load('L_1.png'),
    pygame.image.load('L_standing.png'),
    pygame.image.load('L_2.png'),
    pygame.image.load('L_standing.png')
]
walkRight = [
    pygame.image.load('R_1.png'),
    pygame.image.load('R_standing.png'),
    pygame.image.load('R_2.png'),
    pygame.image.load('R_standing.png')
]
x, y = screen_width/2, screen_height-70
jumping = False
jumpCount = 8
left, right = False, False
walkCount = 0
gameLoop = True

def draw_character(left, right):
    global x, y, walkCount
    if walkCount >= 4:
        walkCount = 0
    if left:
        window.blit(walkLeft[walkCount], (x,y))
    elif right:
        window.blit(walkRight[walkCount], (x,y))
    else:
        window.blit(character, (x,y))

while gameLoop:
    clock.tick(30)
    pygame.time.delay(75)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
                right = False
            elif event.key == pygame.K_RIGHT:
                left = False
                right = True
            if event.key == pygame.K_SPACE:
                jumping = True
        elif event.type == pygame.KEYUP:
            keys = pygame.key.get_pressed()
            if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                left, right = False, False
                walkCount = 0

    if left:
        walkCount += 1
        x -= 10
    elif right:
        walkCount += 1
        x += 10
    if jumping:
        if jumpCount >= -8:
            y -= 1/2 * (jumpCount * abs(jumpCount))
            jumpCount -= 1
        else:
            jumpCount = 8
            jumping = False



    window.fill(white)
    draw_character(left, right)
    pygame.display.update()

pygame.quit()
quit()
