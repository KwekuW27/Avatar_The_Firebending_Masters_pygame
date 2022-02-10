print("github repository test")

import pygame
# from sqlalchemy import true #import
from Player import Player
from Player import Player
from Enemy import Enemy
from Obstacle import Obstacle


#defining WINDOW SIZE
width = 1000 
height = 1000 

#display WINDOW
window = pygame.display.set_mode((width, height))

#name the game WINDOW
pygame.display.set_caption("avatar_pyGame")

#frame rate of game
fps = 60

#player var
playerZuko = Player(100, 700)

#enemy var
enemyShip = Enemy(900, 200)

#obstacle var
enemyObstacle = Obstacle(900, 800)

def main():
# to make the game RUN at a consistent framerate
    clock = pygame.time.Clock()

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

        # if the 'd' key is pressed
        if keysPressed[pygame.K_d] == True:
            playerZuko.x += playerZuko.speed

        if keysPressed[pygame.K_d] == True:
            playerZuko.x += playerZuko.speed

        #enemy movement
        if running == True:
            enemyShip.x -= enemyShip.speed

        #obstacle movement
        if running == True:
            enemyObstacle.x -= enemyObstacle.speed

        #fills the game and adjust for color
        window.fill(( 45, 45, 45))

        playerZuko.render(window)

        enemyShip.render(window)

        enemyObstacle.render(window)


        # put code here that should be run every frame
        # of your game
        pygame.display.update()


main()

