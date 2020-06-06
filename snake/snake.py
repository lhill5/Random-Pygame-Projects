import pygame
import time
from random import randrange

display_width, display_height = 800, 600
block_size = 10
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 255)

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('slither')
clock = pygame.time.Clock()
FPS = 30

def snake(snake_list):
    for coordinate in snake_list:
        pygame.draw.rect(gameDisplay, green, [coordinate[0], coordinate[1], block_size, block_size])

font = pygame.font.SysFont(None, 25)
def display_message(text, color):
    screen_text = font.render(text, True, color)
    gameDisplay.blit(screen_text, [display_width/2 - screen_text.get_width() / 2, display_height/2 - screen_text.get_height() / 2])

def game_loop():
    snake_list = []
    snake_length = 1
    snake_x = display_width/2
    snake_y = display_height/2
    food_x = round(randrange(0, display_width - block_size)/10.0) * 10.0
    food_y = round(randrange(0, display_height - block_size)/10.0) * 10.0

    right, left, down, up = False, False, False, False
    play_game = True
    game_over = False

    while play_game:

        while game_over:
            gameDisplay.fill(white)
            display_message("Press C to play again or Q to quit", blue)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        play_game = False
                        game_over = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not right:
                    right, left, down, up = False, True, False, False
                elif event.key == pygame.K_RIGHT and not left:
                    right, left, down, up = True, False, False, False
                elif event.key == pygame.K_UP and not down:
                    right, left, down, up = False, False, False, True
                elif event.key == pygame.K_DOWN and not up:
                    right, left, down, up = False, False, True, False

        if left:
            snake_x -= block_size
        elif right:
            snake_x += block_size
        elif up:
            snake_y -= block_size
        elif down:
            snake_y += block_size

        if snake_x < 0 or snake_x > display_width - block_size or snake_y < 0 or snake_y > display_height - block_size:
            game_over = True
        if snake_x == food_x and snake_y == food_y:
            snake_length += 4
            food_x = round(randrange(0, display_width - block_size)/10.0) * 10.0
            food_y = round(randrange(0, display_height - block_size)/10.0) * 10.0

        snake_list.append((snake_x, snake_y))
        if len(snake_list) > snake_length:
            del snake_list[0]

        snake_head = snake_list[-1]
        if snake_head in snake_list[0:-1]:
            game_over = True

        clock.tick(FPS)
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [food_x, food_y, block_size, block_size])
        snake(snake_list)
        pygame.display.update()

    gameDisplay.fill(white)
    display_message("you lose", red)
    pygame.display.update()
    pygame.quit()
    quit()

game_loop()
