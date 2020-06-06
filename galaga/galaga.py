import pygame, time, random
import math

black = (0,0,0)
white = (255,255,255)
pygame.init()
screen = pygame.display.set_mode((800,900))
clock = pygame.time.Clock()

class App:
    def __init__(self, spritesheet):
        self.start_game = True
        self.screen_width, self.screen_height = screen.get_width(), screen.get_height()
        self.spritesheet = spritesheet
        self.bg = pygame.surface.Surface((self.screen_width, self.screen_height))
        self.bg.fill(black)
        self.bg_y1, self.bg_y2 = 0, -self.screen_height
        self.galaga_sprites = []
        self.parse_spritesheet()
        self.enemy_explosions = []
        self.ship_explosions = []
        self.ship_missile = pygame.sprite.Sprite()
        self.get_ship_explosions()
        self.get_enemy_explosions()
        self.get_ship_missile()

    def parse_spritesheet(self):
        for row in range(12):
            row_sprites = []
            col_count = 8 if row < 6 else 7
            for col in range(col_count):
                sprite = pygame.sprite.Sprite()
                image = self.spritesheet.subsurface(15+24*col, 50+24*row, 25, 25)
                image = pygame.transform.scale(image, (75,75))
                sprite.image = image
                sprite.rect = image.get_rect()
                row_sprites.append(sprite)
            self.galaga_sprites.append(row_sprites)

    def get_ship_explosions(self):
        ship_explosions = []
        scale = (85,85)
        for i in range(4):
            x = 205+i*35 if i < 2 else 205+i*45
            y = 40 if i == 2 else 50
            sprite = pygame.sprite.Sprite()
            image = self.spritesheet.subsurface(x, y, 40, 40)
            resized_image = pygame.transform.scale(image, scale)
            sprite.image = resized_image
            sprite.rect = resized_image.get_rect()
            ship_explosions.append(sprite)
        return ship_explosions

    def get_enemy_explosions(self):
        enemy_explosions = []
        subsurface_dims = [(208, 200, 20, 20), (231, 198, 20, 20), (252, 198, 20, 20), (282, 191, 30, 30), (319, 189, 45, 45)]
        scale_dims = [(55,55), (55,55), (70,70), (75,75), (110, 110)]
        for dim, scale in zip(subsurface_dims, scale_dims):
            sprite = pygame.sprite.Sprite()
            image = self.spritesheet.subsurface(dim[0], dim[1], dim[2], dim[3])
            image = pygame.transform.scale(image, scale)
            sprite.image = image
            sprite.rect = image.get_rect()
            enemy_explosions.append(sprite)
        return enemy_explosions

    def get_ship_missile(self):
        image = self.spritesheet.subsurface(373, 50, 20, 20)
        image = pygame.transform.scale(image, (45, 45))
        self.ship_missile.image = image
        self.ship_missile.rect = image.get_rect()

    def draw_background(self):
        self.bg_y1 += 1.4
        self.bg_y2 += 1.4
        if self.bg_y1 > self.screen_height:
            self.bg_y1 = -self.screen_height
        if self.bg_y2 > self.screen_height:
            self.bg_y2 = -self.screen_height

        colors = [(255,0,0), (0,255,0), (255,255,0), (255,165,0), (138,43,226)]
        if self.start_game:
            self.start_game = False
            for _ in range(250):
                x, y = random.randint(0, self.screen_width), random.randint(0, self.screen_height)
                block = pygame.Rect(x, y, 1, 1)
                pygame.draw.rect(self.bg, random.choice(colors), block)
        screen.blit(self.bg, (0, self.bg_y1))
        screen.blit(self.bg, (0, self.bg_y2))

class Ship:
    def __init__(self):
        self.rotate_ship = game.galaga_sprites[0]
        self.captured_ship = game.galaga_sprites[1]
        self.ship_explosions = game.get_ship_explosions()
        self.ship = self.rotate_ship[-1]
        self.x, self.y = game.screen_width//2, game.screen_height - 75
        self.missile = game.ship_missile
        self.missiles = []
        self.left = self.right = self.shoot = False
        self.timestamps = []
        self.shipCount = 0

    def draw(self):
        screen.blit(self.ship.image, (self.x, self.y))

    def new_missile(self):
        self.timestamps.append(time.time())
        if len(self.timestamps) == 2:
            if self.timestamps[1] - self.timestamps[0] > 0.3:
                self.timestamps.clear()
                self.timestamps.append(time.time())
                new_missile = Missile()
                self.missiles.append(new_missile)
            else:
                del self.timestamps[1]

    def shoot_enemies(self):
        for missile in self.missiles:
            screen.blit(missile.sprite.image, (missile.x, missile.y))
            missile.y -= 10
            if missile.y < 0:
                self.missiles.remove(missile)

class Missile:
    def __init__(self):
        self.sprite = game.ship_missile
        self.ship_missiles = []
        self.x = starship.x+starship.ship.image.get_width()//2-17
        self.y = starship.y-10
        # screen.blit(image, (20,20))
        # screen.blit(image, (15,14))
        # screen.blit(image, (7,6))
        # screen.blit(image, (6,3))
        # screen.blit(image, (1,3))

class Enemy:
    def __init__(self, enemy_list):
        self.enemies = enemy_list
        self.degrees = 0
        self.a, self.b = 300, 500
        self.center_x, self.center_y = game.screen_width//2, game.screen_height//2
        self.x, self.y = self.center_x, -50

    def move_down(self):
        y = math.sqrt((1 - math.pow(self.x-self.center_x,2)/math.pow(self.a,2))*pow(self.b,2))
        y_values = [self.center_y + y, self.center_y - y]
        self.x += 4
        self.y = min(y_values)
        screen.blit(self.enemies[0].image, (self.x,self.y))
        print(self.x, self.y)

    def move_circle(self):
        radius = 50
        print(self.x, self.y, radius*math.cos(math.radians(self.degrees)))
        x = self.x + radius*math.cos(math.radians(self.degrees)) - radius
        y = self.y + radius*math.sin(math.radians(self.degrees))
        screen.blit(self.enemies[0].image, (x,y))
        self.degrees += 5

spritesheet = pygame.image.load('galaga/galaga_transparent.png').convert_alpha()
game = App(spritesheet)
starship = Ship()

green_alien = Enemy(game.galaga_sprites[2])
# self.green_alien_x, self.green_alien_y = game.screen_width//2, game.screen_height-20
# self.purple_alien = game.galaga_sprites[3]
# self.red_bug = game.galaga_sprites[4]
# self.yellow_bug = game.galaga_sprites[5]
# self.yellow_alien = game.galaga_sprites[6]
# self.orange_bug = game.galaga_sprites[7]
# self.green_alienship = game.galaga_sprites[8]
# self.blue_bug = game.galaga_sprites[9]
# self.red_alien = game.galaga_sprites[10]
# self.blue_robot = game.galaga_sprites[11]

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    # keys = pygame.key.get_pressed()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                starship.left = True
                starship.right = False
            elif event.key == pygame.K_RIGHT:
                starship.left = False
                starship.right = True
            elif event.key == pygame.K_SPACE:
                starship.shoot = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                starship.left = starship.right = False
            elif event.key == pygame.K_SPACE:
                starship.shoot = False

    if starship.left:
        starship.x -= 4
    elif starship.right:
        starship.x += 4
    if starship.shoot:
        starship.new_missile()

    game.draw_background()
    starship.draw()
    if len(starship.missiles) > 0:
        starship.shoot_enemies()
    if not green_alien.x == green_alien.center_x + green_alien.a:
        green_alien.move_down()
    else:
        if green_alien.degrees <= 540:
            green_alien.move_circle()
        # else:


    clock.tick(60)
    pygame.display.update()


pygame.quit()
