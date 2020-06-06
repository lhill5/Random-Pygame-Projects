import pygame
red = (255,0,0)

pygame.init()

screen = pygame.display.set_mode((1000,1000))
eclipse = (0,0,100,100)
run = True 
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	pygame.draw.ellipse(screen, red, eclipse, 1)
	pygame.display.update()



pygame.quit()

