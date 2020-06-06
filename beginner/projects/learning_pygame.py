import pygame
from car import Car

pygame.init()

black = (0,0,0)
white = (255,255,255)
green = (0,155,0)
red = (255, 0, 0)
gray = (192, 192, 192)

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('first pygame game')

all_sprites_list = pygame.sprite.Group()
playerCar = Car(red, 20, 30)
playerCar.rect.x = 150
playerCar.rect.y = 300

all_sprites_list.add(playerCar)

clock = pygame.time.Clock()
gameLoop = True

while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

    all_sprites_list.update()
    screen.fill(black)
    pygame.draw.rect(screen, green, [0, 0, 700/6, 500], 0)
    pygame.draw.rect(screen, gray, [700/6,0,700/6,500], 0)
    pygame.draw.rect(screen, gray, [(700/6)*2,0,(700/6)*2,500], 0)
    pygame.draw.rect(screen, gray, [(700/6)*3,0,(700/6)*3,500], 0)
    pygame.draw.rect(screen, gray, [(700/6)*4,0,(700/6)*4,500], 0)
    pygame.draw.rect(screen, green, [(700/6)*5,0,(700/6)*5,500], 0)

    pygame.draw.line(screen, white, [700/6,0], [700/6,500], 3)
    pygame.draw.line(screen, white, [(700/6)*2,0], [(700/6)*2,500], 3)
    pygame.draw.line(screen, white, [(700/6)*3,0], [(700/6)*3,500], 3)
    pygame.draw.line(screen, white, [(700/6)*4,0], [(700/6)*4,500], 3)
    pygame.draw.line(screen, white, [(700/6)*5,0], [(700/6)*5,500], 3)

    all_sprites_list.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
