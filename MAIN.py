import pygame, random,time
from var import *
from Object import *
from Action import *


def cara_bermain():
    background = pygame.image.load("Asset/cara main.jpg")
    gameDisplay.blit(background, [0, 0])

    caraMain = True

    while caraMain:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("KEMBALI", 340,470,140,50, Yellow,DarkYellow, game_intro)

        pygame.display.update()
        clock.tick(15)

def CreditScreen():
    background = pygame.image.load("Asset/Credit.jpg")
    gameDisplay.blit(background, [0, 0])

    CreditScreen = True

    while CreditScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        CreditButton("KEMBALI", 24,270,100,50, game_intro)
        pygame.display.update()



def mulai():
    pygame.mixer.music.fadeout(5)
    pygame.mixer.music.load("Music/gameplay deja vu.mp3")
    pygame.mixer.music.play(-1)
    game_loop()

def intro():
    pygame.mixer.music.load("Music/intro deja vu.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    game_intro()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        background = pygame.image.load("Asset/background1fix.jpg")
        gameDisplay.blit(background ,[0,0])

        button("MULAI", 340,290,140,50, Green,DarkGreen, mulai)
        button("CARA MAIN", 340,360,140,50, Yellow,DarkYellow, cara_bermain)
        button("KELUAR", 340,430,140,50, Red,DarkRed, quit)
        CreditButton('CREDIT',658,250,100,50,CreditScreen)


        pygame.display.update()
        clock.tick(15)


def crash(x,y,score):
    drive.stop()
    boom(x, y)
    TextCrash()
    final_score(score)
    askContinue()
    PlayerDead()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("YA", 160, 260, 140, 50, Green, DarkGreen, game_loop)
        button("TIDAK", 490, 260, 140, 50, Yellow, DarkYellow, intro)

        pygame.display.update()


def game_loop():

    pygame.mixer.Sound.play(start)
    drive.play(loops=-1)
    pygame.mixer.music.set_volume(10)

    # INISIALISAIS NILAI
    car_x = 500
    car_y = (display_height * 0.8)

    road_left = 350
    road_right = 700
    road_long = 600
    road_speed = 4

    x_change = 0
    y_change = 0

    road_startX = 350
    road_startY = -600

    obstacle_startx = random.randrange(road_left,road_right,50)
    obstacle_starty = -300

    obstacle_startx2 = random.randrange(road_left, road_right, 50)
    obstacle_starty2 = -450

    obstacle_startx3 = random.randrange(road_left, road_right, 50)
    obstacle_starty3 = -600

    obstacle_speed = road_speed - 1
    obstacle_move = obstacle_speed /2
    obstacle_width = car_width
    obstacle_height = car_height

    scoreCount = 0
    TopScore = OpenTopScore()
    gameExit = False
    Carmove = False
    PlayerDead = False

    #EVENT HANDLING
    while not gameExit:

        for event in pygame.event.get():
            press_quit(event)
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -5
                    Carmove = True
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                    Carmove = True
                elif event.key == pygame.K_UP:
                    y_change = -2
                elif event.key == pygame.K_DOWN:
                    y_change = 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                   y_change = 0

        car_x += x_change
        car_y += y_change


        #MEMBUAT DISPLAY
        gameDisplay.fill(Outside_color)


        #Munculkan Jalan
        road(road_startX,(road_startY + road_long))
        road(road_startX,road_startY)
        road(road_startX,(road_startY - road_long))
        road_startY += road_speed

        # Memunculkan Mobil Player
        car(car_x,car_y)
        Scoreboard()

        #Memunculkan Obstacle
        obstacle(obstacle_startx,obstacle_starty)
        obstacle2(obstacle_startx2,obstacle_starty2)
        obstacle3(obstacle_startx3,obstacle_starty3)

        #MENGGERAKAN OBSTACLE
        obstacle_starty += obstacle_speed
        obstacle_starty2 += obstacle_speed
        obstacle_starty3 += obstacle_speed


        #Mobil Polisi mengikuti gerak player
        if Carmove == True:
            obstacle_startx += x_change / 2.5
            if obstacle_startx >= road_right - obstacle_width:
                obstacle_startx = road_right - obstacle_width
            elif obstacle_startx <= road_left:
                obstacle_startx = road_left

        #Mobil taxi akan bergerak jika score diatas 80
        if scoreCount >= 80 :
            obstacle_startx2 += obstacle_move
            if obstacle_startx2 + obstacle_width >= road_right:
                obstacle_startx2 = road_right - obstacle_width
                obstacle_move = -(obstacle_speed/2)
            elif obstacle_startx2 <= road_left:
                obstacle_startx2 = road_left
                obstacle_move = obstacle_speed/2

        #dapat point
        if obstacle_starty == car_y:
            scoreCount += 5
            road_speed += level(scoreCount)
        if obstacle_starty2 == car_y:
            scoreCount += 5
            road_speed += level(scoreCount)
        if obstacle_starty3 == car_y:
            scoreCount += 5
            road_speed += level(scoreCount)


        #boundary untuk mobil x
        if car_x > road_right - car_width:
            car_x = road_right - car_width
        elif  car_x < road_left:
            car_x = road_left

        #boundary mobil y
        if car_y  >= display_height - car_width:
            car_y = display_height - car_width
        elif car_y < 0:
            car_y = 0

        #ulang jalan
        if road_startY > display_height:
            road_startY = 0 - road_long


        # crashed saat nabrak
        Collision = detectCollision(car_x,car_y,car_width,car_height,obstacle_startx,obstacle_starty,obstacle_width,obstacle_height)
        Collision2 = detectCollision(car_x,car_y,car_width,car_height,obstacle_startx2,obstacle_starty2,obstacle_width,obstacle_height)
        Collision3 = detectCollision(car_x,car_y,car_width,car_height,obstacle_startx3,obstacle_starty3,obstacle_width,obstacle_height)
        if Collision == True or Collision2 == True or Collision3 == True:
            crash(car_x,car_y,scoreCount)

        #munculin kembali Obstacle
        if obstacle_starty > display_height:
            obstacle_starty = 0 - obstacle_height
            obstacle_startx = random.randrange(road_left,road_right-obstacle_width)

        if obstacle_starty2 > display_height:
            obstacle_starty2 = 0 - obstacle_height
            obstacle_startx2 = random.randrange(road_left, road_right - obstacle_width)

        if obstacle_starty3 > display_height:
            obstacle_starty3 = 0 - obstacle_height
            obstacle_startx3 = random.randrange(road_left, road_right - obstacle_width)

        #menghitung topscore
        Score(scoreCount,TopScore)
        if scoreCount > TopScore:
            g = open("data/save.dat", 'w')
            g.write(str(scoreCount))
            g.close()
            TopScore = scoreCount
        speedDisplay(round(road_speed,2))
        PlayerLife()
        pygame.display.update()
        clock.tick(60)

splashScreen()
WaitingScreen()
intro()
game_loop()
pygame.quit()
quit()

