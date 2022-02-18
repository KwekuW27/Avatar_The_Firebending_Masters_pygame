print("github repository test")

from random import randrange
from random import randint
from turtle import window_width
import pygame
from sqlalchemy import false, true
from FlamingFireBall import FlamingFireBall
# from sqlalchemy import true #import
from Player import Player
from Player import Player
from Enemy import Enemy
from Obstacle import Obstacle
from Animation import Animation

pygame.font.init()

#sound mixer
from pygame import mixer 
mixer.init()

# pygame.init()

#defining WINDOW SIZE
width = 1000 
height = 800 

#display WINDOW
window = pygame.display.set_mode((width, height))

#name the game WINDOW
pygame.display.set_caption("avatar_pyGame")

#frame rate of game
fps = 60

playerZukoX = 100
playerZukoY = 640

#player var
playerZuko = Player(playerZukoX, playerZukoY)

enemyShipX = 900
enemyShipY = 200

#enemy var
enemyShip = Enemy(enemyShipX, enemyShipY)

enemyList = []

enemyList.append(Enemy(enemyShipX, enemyShipY))

enemyObstacleX = 900
enemyObstacleY = 750

# enemyObstacle = Obstacle(enemyObstacleX, enemyObstacleY)

obstacleList = []

#enemyObstacle = Obstacle(900, 800)
# obstacleList.append(Obstacle(enemyObstacleX, enemyObstacleY))

flamingFireBallX = enemyShip.x/2
flamingFireBallY = enemyShip.y

flamingFireBallList = []

# color
white = (255,255,255)
            
# position
tscoredisplayposX = 0
tscoredisplayposy = 550

# rendering
font = pygame.font.SysFont('timesnewroman', 10)


# load the image for the start screen
startScreenImg = pygame.image.load("Assets/startScreen.jpeg")

# load the image for the instruction screen
instructionImg = pygame.image.load("Assets/instructions.jpeg")

# load the image for the background
backgroundImg = pygame.image.load("Assets/gameBackground.jpeg")

#load in image for the end screen
endImg = pygame.image.load("Assets/endScreen.jpeg")

#player Animation images
zukoImg0 = pygame.image.load("Assets/run0.png")
zukoImg1 = pygame.image.load("Assets/run1.png")
zukoImg2 = pygame.image.load("Assets/run2.png")
zukoImg3 = pygame.image.load("Assets/run3.png")
zukoImg4 = pygame.image.load("Assets/run4.png")

#loading object images
objectImg0 = pygame.image.load("Assets/barrel.png")
objectImg1 = pygame.image.load("Assets/fireNationGuy.png")
objectImg2 = pygame.image.load("Assets/cabbageGuy.png")

#loading enemy images
enemyImg0 = pygame.image.load("Assets/balloon.png")

#loading bullet images
fireballImg = pygame.image.load("Assets/fireball.png")

#assigning the zuko images to the list
animationList = []

#place the animation images into the list
animationList.append(zukoImg0)
animationList.append(zukoImg1)
animationList.append(zukoImg2)
animationList.append(zukoImg3)
animationList.append(zukoImg4)

#start an animation
zukoRun = Animation(animationList, 0.3, 6)


#starting X positions for background
BackgroundXstart = 0
BackgroundX2start = 5000

#switch case starting number
startval = 0

# flamingFireBallList.append(FlamingFireBall(aEnemy.x, aEnemy.y))


def main():
# to make the game RUN at a consistent framerate
    clock = pygame.time.Clock()

    # makes the music not overlap
    playOnce = True

    obstacleSpawnClock = pygame.time.Clock()
    enemySpawnClock = pygame.time.Clock()
    flamingFireBallSpawnClock = pygame.time.Clock()
    #obstacle Time vars
    timeSince = 0
    timeBetween = randrange(2000, 7000)
    #enemyShip Time vars
    timeSince2 = 0
    timeBetween2 = randrange(3000, 15000)
    #flamingFireBall Time vars
    timeSince3 = 0
    timeBetween3 = 1000

    #scoring system initializers
    sscore = 0
    tscore = 0
    vscore = 0
    iscore = 5
    finalScore = 0

    lives = 3


    #sets display positions
    BackgroundX2refresh = 1000000
    BackgroundXrefresh = 1000000

    jump = False

    swval = startval
    
    vel_y = 18

    running = True #capitalized T = boolean

    while running:

       #this makes it so this function can run at most FPS
        clock.tick(fps)

        # for all the game events
        for event in pygame.event.get():
            # if the game is exited out of, then stop running the game
            if event.type == pygame.QUIT:
                running = False

        # this gets a list of booleans showing which keys are currently pressed
        keysPressed = pygame.key.get_pressed()
    
        if(swval == 0):

            #loading game sounds and music
            if playOnce == True:
                mixer.music.load('Assets/introMusic.wav')
                #this will make the background music play on a loop
                mixer.music.play(-1)
                playOnce = False

            #title

            window.blit(startScreenImg,(0, 0))
            
            # if the 'w' key is pressed, change screens and reset song boolean
            if keysPressed[pygame.K_w] == True:
                swval = 1
                playOnce = True

        elif(swval == 1):

            window.blit(instructionImg,(0, 0))

            #loading instruction sounds and music
            if playOnce == True:
                mixer.music.load('Assets/blueSpiritMusic.wav')    
                
                #this will make the background music play on a loop
                mixer.music.play(-1)
                playOnce = False

            #instruction
            two = 2
            # if the 's" key is pressed, switch screens and reset sound boolean
            if keysPressed[pygame.K_s] == True:
                swval = 2
                playOnce = True

        elif(swval == 2):
            
            #Game

            #sets the starting X positions for the backgrounds
            if (BackgroundXrefresh == 1000000):
                BackgroundX2refresh = BackgroundX2start
                BackgroundXrefresh = BackgroundXstart

            #Enables background display
            window.blit(backgroundImg, (BackgroundXrefresh, 0))
            window.blit(backgroundImg, (BackgroundX2refresh, 0))
            #updates starting position once
            BackgroundXrefresh = BackgroundXrefresh - 5
            BackgroundX2refresh = BackgroundX2refresh - 5
            #Resets background position
            if (BackgroundXrefresh <= -5000):
                BackgroundXrefresh = 5000
            if (BackgroundX2refresh <= -5000):
                BackgroundX2refresh = 5000

            #loading game sounds and music
            if playOnce == True:
                mixer.music.load('Assets/agniKaiMusic.wav')
                
                #this will make the background music play on a loop
                mixer.music.play(-1)
                playOnce = False

            #obstacle spawning
            dt = obstacleSpawnClock.tick()
            timeSince += dt
            if timeSince > timeBetween :
                #enemyObstacle = Obstacle(900, 800)
                
                #based on this randomly generated number, generate 1 of 3 obs
                randObstacleNum = randint(0,10)

                if randObstacleNum <= 5:
                    obstacleList.append(Obstacle(enemyObstacleX, enemyObstacleY, 75, 56, objectImg0))

                elif randObstacleNum >= 7:
                    obstacleList.append(Obstacle(enemyObstacleX, enemyObstacleY-130, 107, 197, objectImg1))
                    
                else:
                    obstacleList.append(Obstacle(enemyObstacleX, enemyObstacleY-150, 216, 197, objectImg2))

                
                timeSince = 0
                timeBetween = randrange(1000, 6000)

            #shipspawning
            dt = enemySpawnClock.tick()
            timeSince2 += dt
            if timeSince2 > timeBetween2 :
                enemyList.append(Enemy(enemyShipX, enemyShipY))
                timeSince2 = 0
                timeBetween2 = randrange(3000, 15000)


                    #flamingForeBallspawning
            dt = flamingFireBallSpawnClock.tick()
            timeSince3 += dt
            if timeSince3 > timeBetween3 :
                if len(enemyList) > 0 :
                    enemyIndex = randint(0, len(enemyList   ) - 1)
                    spawnenemy = enemyList[enemyIndex]
                    flamingFireBallList.append(FlamingFireBall(spawnenemy.x, spawnenemy.y))
                #flamingFireBallList.append(FlamingFireBall(aEnemy.x, aEnemy.y))
                timeSince3 = 0
        
            #print(len(obstacleList))
            for aObstacle in obstacleList :


                # print(aObstacle.x)
                #obstacle movement
                if running == True:
                    aObstacle.x -= aObstacle.speed

                    aObstacle.render(window)
            
                if aObstacle.obstacleHitbox.right < 0:
                    obstacleList.remove(aObstacle)
                    print("right side detected")
            
                #collision detect between obstacle and player
                collide = pygame.Rect.colliderect(playerZuko.hitBox, aObstacle.obstacleHitbox)

                    # If the objects are colliding
                    # then changing the y coordinate
                if collide:
                        playerZuko.hitBox.right = aObstacle.obstacleHitbox.left
                        playerZuko.hitBox.bottom = aObstacle.obstacleHitbox.top
                        obstacleList.remove(aObstacle)

                        print("colliding")
                        vscore = 0
                        sscore = 0
                        iscore = 5
                        lives += -1

            #Score coding
            if sscore >= 100-vscore:
                tscore += iscore
                sscore = 0
                print("Score: "+str(tscore))
                vscore += 3
                if vscore > 90:
                    vscore = 90
                    iscore += 1
                if iscore > 100:
                    iscore = 100

            #tiskcpeed increase
            sscore += 1

            

            # print(len(enemyList))
            for aEnemy in enemyList :
            
                window.blit(enemyImg0,(aEnemy.x-120, aEnemy.y-175))

                #enemy movement
                if running == True:
                    aEnemy.x -= aEnemy.speed

                if aEnemy.enemyHitbox.right < 0:
                    enemyList.remove(aEnemy)
                    print("right side detected")

            # print(len(flamingFireBallList))
            for aFlamingFireBall in flamingFireBallList :

                aFlamingFireBall.render(window)
                window.blit(fireballImg,(aFlamingFireBall.x, aFlamingFireBall.y))

                 #flamingFireBall movement
                if running == True:
                    aFlamingFireBall.y += aFlamingFireBall.speed

                if aFlamingFireBall.flamingFireBallHitbox.top > height:
                    flamingFireBallList.remove(aFlamingFireBall)
                    print("top side detected")

            text = font.render('Score: '+str(tscore), True, white, None)
            window.blit(text, (tscoredisplayposX // 2, tscoredisplayposy// 2))

            # DONT USE
            #collision between flamingFireBall and player
            # collide2 = pygame.Rect.colliderect(playerZuko.hitBox, aFlamingFireBall.flamingFireBallHitbox)

            # if collide2:
            #     playerZuko.hitBox.top = aFlamingFireBall.flamingFireBallHitbox.bottom
            #     flamingFireBallList.remove(aFlamingFireBall)
            #     print("fire colliding")


            # print("end of for loop")

            

            # if the 'w' key is pressed
            if keysPressed[pygame.K_a] == True:
                playerZuko.x -= playerZuko.speed

            if keysPressed[pygame.K_a] == True:
                playerZuko.x -= playerZuko.speed

            # if the 'd' key is pressed
            if keysPressed[pygame.K_d] == True:
                playerZuko.x += playerZuko.speed

            if keysPressed[pygame.K_d] == True:
                playerZuko.x += playerZuko.speed
        
            if jump is False and keysPressed[pygame.K_SPACE] :
                jump = True

            if jump is True :
                playerZuko.y -= vel_y
                vel_y -= 1
                if vel_y < -18 :
                    jump = False
                    vel_y = 18

            playerZuko.render(window)

            #display the animation overtop of the zuko's hitbox
            zukoRun.display(window, playerZuko.x-50, playerZuko.y-25)

            if lives <= 0:
                Player.isDead = true

            if Player.isDead == true:
                finalScore = tscore
                tscore= 0
                sscore= 0 
                vscore= 0
                iscore= 5
                lives = 3
                swval = 4



        elif (swval == 3):
            #bad end + score
            print ("Bad")

            #loading dead sounds and music
            if playOnce == True:
                mixer.music.load('Assets/deathMusic.wav')
                
                #this will make the background music play on a loop
                mixer.music.play(-1)
                playOnce = False

        elif (swval == 4):
            #good end + score

            window.blit(endImg,(0, 0))


            # if the 'w' key is pressed, change screens and reset song boolean
            if keysPressed[pygame.K_q] == True:
                swval = 1
                playOnce = True


            #loading instruction sounds and music
            if playOnce == True:
                mixer.music.load('Assets/winScreen.wav')
                
                #this will make the background music play on a loop
                mixer.music.play(-1)
                playOnce = False

        # aObstacle.render(window)

        # put code here that should be run every frame
        # of your game
        pygame.display.update()
        
main()
