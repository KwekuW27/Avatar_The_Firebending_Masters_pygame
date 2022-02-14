print("github repository test")

from random import randrange
from turtle import window_width
import pygame
from sqlalchemy import false
from FlamingFireBall import FlamingFireBall
# from sqlalchemy import true #import
from Player import Player
from Player import Player
from Enemy import Enemy
from Obstacle import Obstacle

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
playerZukoY = 750

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

enemyObstacle = Obstacle(enemyObstacleX, enemyObstacleY)

obstacleList = []

#enemyObstacle = Obstacle(900, 800)
obstacleList.append(Obstacle(enemyObstacleX, enemyObstacleY))

flamingFireBallX = enemyShip.x/2
flamingFireBallY = enemyShip.y

flamingFireBallList = []

# flamingFireBallList.append(FlamingFireBall(aEnemy.x, aEnemy.y))


def main():
# to make the game RUN at a consistent framerate
    clock = pygame.time.Clock()

    obstacleSpawnClock = pygame.time.Clock()
    enemySpawnClock = pygame.time.Clock()
    flamingFireBallSpawnClock = pygame.time.Clock()
    #obstacle Time vars
    timeSince = 0
    timeBetween = 3000
    #enemyShip Time vars
    timeSince2 = 0
    timeBetween2 = 3000
    #flamingFireBall Time vars
    timeSince3 = 0
    timeBetween3 = 1000

    jump = False

    vel_y = 13

    running = True #capitalized T = boolean

    while running:

        #fills the game and adjust for color
        window.fill((45, 45, 45))

       #this makes it so this function can run at most FPS
        clock.tick(fps)

        # for all the game events
        for event in pygame.event.get():
            # if the game is exited out of, then stop running the game
            if event.type == pygame.QUIT:
                running = False

        #obstacle spawning
        dt = obstacleSpawnClock.tick()
        timeSince += dt
        if timeSince > timeBetween :
            #enemyObstacle = Obstacle(900, 800)
            obstacleList.append(Obstacle(enemyObstacleX, enemyObstacleY))
            timeSince = 0

        #shipspawning
        dt = enemySpawnClock.tick()
        timeSince2 += dt
        if timeSince2 > timeBetween2 :
            enemyList.append(Enemy(enemyShipX, enemyShipY))
            timeSince2 = 0
        
        
        #print(len(obstacleList))
        for aObstacle in obstacleList :

            aObstacle.render(window)
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

        # print(len(enemyList))
        for aEnemy in enemyList :
            
            aEnemy.render(window)

                 #flamingForeBallspawning
            dt = flamingFireBallSpawnClock.tick()
            timeSince3 += dt
            if timeSince3 > timeBetween3 :
                flamingFireBallList.append(FlamingFireBall(aEnemy.x, aEnemy.y))
                timeSince3 = 0

            #enemy movement
            if running == True:
                aEnemy.x -= aEnemy.speed

            if aEnemy.enemyHitbox.right < 0:
                enemyList.remove(aEnemy)
                print("right side detected")

        # print(len(flamingFireBallList))
        for aFlamingFireBall in flamingFireBallList :

            aFlamingFireBall.render(window)

             #flamingFireBall movement
            if running == True:
                aFlamingFireBall.y += aFlamingFireBall.speed

            if aFlamingFireBall.flamingFireBallHitbox.top > height:
                flamingFireBallList.remove(aFlamingFireBall)
                print("top side detected")


            

        # DONT USE
        #collision between flamingFireBall and player
        # collide2 = pygame.Rect.colliderect(playerZuko.hitBox, aFlamingFireBall.flamingFireBallHitbox)

        # if collide2:
        #     playerZuko.hitBox.top = aFlamingFireBall.flamingFireBallHitbox.bottom
        #     flamingFireBallList.remove(aFlamingFireBall)
        #     print("fire colliding")


        # print("end of for loop")

        # this gets a list of booleans showing which keys are currently pressed
        keysPressed = pygame.key.get_pressed()

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
            if vel_y < -13 :
                jump = False
                vel_y = 13

        playerZuko.render(window)

        # aObstacle.render(window)


        # put code here that should be run every frame
        # of your game
        pygame.display.update()

main()

