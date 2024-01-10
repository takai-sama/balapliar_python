import random
import pygame
pygame.init()

display_width = 800
display_height = 600

Black = (0,0,0)
Gray = (10,10,10)
White = (255,255,255)
Red = (255,0,0)
DarkRed = (120,0,0)
Green = (0,255,0)
DarkGreen = (0,120,0)
Yellow = (220,220,25)
DarkYellow = (120,120,0)
Outside_color = (92,94,91)
Transparent = (255,255,255,128)

car_width = 50
car_height = 100

road_width = 350
road_height = display_height


game_icon = pygame.image.load('Asset/Icon2.png')
pygame.display.set_icon(game_icon)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Balap liar')
clock = pygame.time.Clock()

car_1 = pygame.image.load('Asset/2.png')
car_2 = pygame.image.load('Asset/3.png')
car_3 = pygame.image.load('Asset/4.png')

car_list = [car_1,car_2,car_3]

carImg = pygame.image.load('Asset/bugattiedit.png')
carObs = pygame.image.load('Asset/3.png')
roadImg = pygame.image.load('Asset/Road_2.jpg').convert()
BOOM = pygame.image.load('Asset/explosion.png')
ScoreboardIMG = pygame.image.load('Asset/Scoreboard.jpg').convert()

Mas_life = pygame.image.load('Asset/Mas Liar - Life.png').convert()
Mas_dead = pygame.image.load('Asset/Mas Liar - Dead.png').convert()

Gedung_kanan = pygame.image.load('Asset/Gedung_kanan.jpg')
Gedung_kiri = pygame.image.load('Asset/Gedung_kiri.jpg')

start = pygame.mixer.Sound("Music/engine start.wav")
drive = pygame.mixer.Sound("Music/engine drive.wav")