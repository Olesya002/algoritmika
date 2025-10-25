import pygame
import time
# инициализация игры
pygame.init()

# создание окна
width, height = 900, 700
screen = pygame.display.set_mode((width, height)) #flags=pygame.NOFRAME
pygame.display.set_caption('My game')
icon = pygame.image.load('images\\donat.png')
pygame.display.set_icon(icon)

# загрузим картинку для фона
background_image = pygame.image.load('images\\background.png')
# трансвормируем ее под размеры окна
background = pygame.transform.scale(background_image, (width, height))

# можем создавать различные объекты (фигуры )
square = pygame.Surface((50, 170))
square.fill('Blue')

# герой
player = pygame.image.load('images\\pacman-png-9.png')
player_trans = pygame.transform.flip(player, 90)
# текст
myfont = pygame.font.Font('fonts\\BitcountPropSingleInk-VariableFont_CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght.ttf', 40)
text_surface = myfont.render('Hello my player', True, 'Purple')

running = True
while running is True:
    pygame.display.update()
    screen.blit(background, dest=(0,0))
    screen.blit(square, (100,0))
    # установим фон
    # screen.fill((100, 25, 100)) # заливка цветом
    pygame.draw.circle(square, (44, 32, 90), (10, 10), 10)
    screen.blit(text_surface, (300, 400))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_b:
        #         screen.fill((70, 44, 133))
        #         pygame.display.update()
        #         time.sleep(5)
