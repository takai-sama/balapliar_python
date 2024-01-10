import time
from var import *


def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def boom(x,y):
    gameDisplay.blit(BOOM,(x-50,y-40))

def road(roadX,roadY):
    road_width = 350
    road_height = 600
    pygame.draw.rect(gameDisplay, Transparent, [roadX, roadY, road_width, road_height])
    gameDisplay.blit(roadImg, (roadX-100, roadY))

def Scoreboard():
    gameDisplay.blit(ScoreboardIMG,(0,0))

def PlayerLife():
    gameDisplay.blit(Mas_life,(21,330))

def PlayerDead():
    gameDisplay.blit(Mas_dead,(21,330))

def obstacle(obstaclex,obstacley):
    gameDisplay.blit(car_1, (obstaclex, obstacley))


def obstacle2(obstaclex,obstacley):
    gameDisplay.blit(car_2, (obstaclex, obstacley))


def obstacle3(obstaclex,obstacley):
    gameDisplay.blit(car_3, (obstaclex, obstacley))

def text_object(text,font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def CreditButton(msg,x, y, w, h,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(mouse)

    smallText = pygame.font.Font("Asset/Pixellari.ttf", 24)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        textSurf, textRect = text_object(msg, smallText, White)
        # pygame.draw.ellipse(gameDisplay, ic,(x-10, y-10,w+20,h+20))
        if click[0] == 1 and action != None:
            action()

    else:
        textSurf, textRect = text_object(msg, smallText, Black)

    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def button(msg, x, y, w, h, ic, ac, action=None):
    """message, dimension, active/inactive color"""

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(mouse)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ic,(x, y,w,h))
        #pygame.draw.ellipse(gameDisplay, ic,(x-10, y-10,w+20,h+20))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ac,(x, y,w,h))

    smallText = pygame.font.Font("Asset/Pixellari.ttf",20)
    textSurf, textRect = text_object(msg, smallText,White)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)




