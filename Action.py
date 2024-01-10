import pygame , sys ,os
import time
from var import *
from Object import *

def OpenTopScore():
    if not os.path.exists("data/save.dat"):
        f = open("data/save.dat")
        f.write(str(0))
        f.close()
    v = open("data/save.dat",'r')
    TopScore = int(v.readline())
    v.close()
    return TopScore

def Score(count,topscore):
    font = pygame.font.Font(None,30)
    CurrentScore = font.render("Score : "+str(count),True,White)
    if count >= topscore:
        TopScore = font.render("Top Score : "+str(topscore),True,Green)
    else:
        TopScore = font.render("Top Score : " + str(topscore), True, Red)
    gameDisplay.blit(CurrentScore,(40,200))
    gameDisplay.blit(TopScore,(40,230))

def speedDisplay(count):
    font = pygame.font.Font(None, 30)
    text = font.render('Speed : ' + str(count)+' KM/H', True, White)
    gameDisplay.blit(text, (40, 260))


def final_score(count):
    largeText = pygame.font.Font('Asset/Pixellari.ttf', 25)
    Textsurf, TextRect = text_object('Your Final Score : '+str(count), largeText,White)
    TextRect.center = ((display_width / 2), (display_height / 1.7)-120)
    gameDisplay.blit(Textsurf, TextRect)


def askContinue():
    largeText = pygame.font.Font('Asset/Pixellari.ttf', 25)
    Textsurf, TextRect = text_object('Lanjut ?', largeText,White)
    TextRect.center = ((display_width / 2), (display_height / 1.5)-120)
    gameDisplay.blit(Textsurf, TextRect)

def TextCrash():
    largeText = pygame.font.Font('Asset/Pixellari.ttf', 80)
    Textsurf, TextRect = text_object('TERTABRAK !!', largeText,White)
    TextRect.center = ((display_width / 2), (display_height / 2)-120)
    pygame.draw.rect(gameDisplay, Red, (0, 80, 800, 250))
    gameDisplay.blit(Textsurf, TextRect)

def press_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            gameExit = True
            pygame.quit()
            quit()

def splashScreen():

    img = pygame.image.load('Asset/pygame_badge.png')

    pygame.mixer.music.load("Music/Snake_hiss.wav")
    pygame.mixer.music.play(0)

    gameDisplay.blit(img,(172 , 150))

    pygame.display.update()
    time.sleep(4)



def WaitingScreen():
    pygame.mixer.music.load('Music/Waiting Screen Sound.mp3')
    pygame.mixer.music.play(-1)

    largeText = pygame.font.Font('Asset/Pixellari.ttf', 20)
    wait = pygame.image.load('Asset/SplashScreen3.jpg')
    Textsurf, TextRect = text_object('Press Any key to start', largeText, White)
    TextRect.center = ((400), (300))

    gameDisplay.blit(wait,(0,0))
    pygame.display.update()
    time.sleep(2)
    gameDisplay.blit(Textsurf,TextRect)

    waiting = True
    while waiting:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                else:
                    waiting = False
            else:
                press_quit(event)


        pygame.display.update()


def level(score):
    accelerate = 0

    if score % 10 == 0:
        accelerate = 0.8
    elif score % 10 == 0 and score >= 50:
        accelerate = 1.5
    elif score % 10 == 0 and score >= 80:
        accelerate = 2.5

    return accelerate



def detectCollision(x1,y1,w1,h1,x2,y2,w2,h2):

    if x2+w2 >= x1 >=x2 and y2+h2 >= y1 >= y2:
        return True
    elif x2+w2 >= x1+w1 >=x2 and y2+h2 >= y1 >= y2:
        return True
    elif x2+w2 >= x1 >=x2 and y2+h2 >= y1+h1 >= y2:
        return True
    elif x2+w2 >= x1+w1 >=x2 and y2+h2 >= y1+h1 >= y2:
        return True
    else:
        return False



