import pygame
from random import randint
width, height = 900, 700
screen = pygame.display.set_mode((width, height)) #flags=pygame.NOFRAME
pygame.display.set_caption('My game')
icon = pygame.image.load('images\\donout.png')
pygame.display.set_icon(icon)


pygame.mixer.init()
# подгрузим музыку
# Sound = pygame.mixer.Sound('woke.mp3')
# Sound.play()



# загрузим картинку для фона
background_image = pygame.image.load('images\\background.png')
# трансвормируем ее под размеры окна
background = pygame.transform.scale(background_image, (width, height))

# герой
player_img = pygame.image.load('images\\pacman-png-9.png')
player_img = pygame.transform.rotate(player_img, 90)


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_image, (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and self.rect.x > 5:
                self.rect.x -= self.speed
            if keys[pygame.K_d] and self.rect.x < width - 80:
                self.rect.x += self.speed



player_img = pygame.image.load('images\\pacman-png-9.png')
player = Player(player_img, 500, 600, 100, 100, 5)

class Enemy(GameSprite):
   #движение врага
   def update(self):
       self.rect.y += self.speed
       global lost
       #исчезает, если дойдет до края экрана
       if self.rect.y > height:
           self.rect.x = randint(80, width - 80)
           self.rect.y = 0
        #    lost = lost + 1
img_enemy = pygame.image.load('images\\donout.png')
player = Player(player_img, 500, 600, 100, 100, 5)
monsters = pygame.sprite.Group()
for i in range(1, 6):
   monster = Enemy(img_enemy, randint(80, width - 80), -40, 80, 50, randint(1, 5))
   monsters.add(monster)

bg_x = 0

running = True
while running is True:
    
    pygame.display.update()
    screen.blit(background, dest=(bg_x,0))
    screen.blit(background, dest=(bg_x+900,0))
    bg_x -= 1
    if bg_x == -900:
        bg_x = 0
    player.reset()
    player.update()

    monsters.update()
    monsters.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
