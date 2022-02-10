print("github repository test")

import pygame
from sqlalchemy import true #import

#import the player class
from Player import Player
from Obstacle import Obstacle

#defining WINDOW SIZE
width = 1000 
height = 1000 

#display WINDOW
window = pygame.display.set_mode((width, height))

#name the game WINDOW
pygame.display.set_caption("Avatar: The Firebender Master")

#frame rate of game
fps = 60

#player located at a temporary X and Y location
player1 = Player(200, 100)

#Obstacle located at Temporary X and Y loacation
obstacle1 = Obstacle(500,250)

def main():
# to make the game RUN at a consistent framerate
    clock = pygame.time.Clock()

    running = True #capitalized T = boolean

    while running:

       #this makes it so this function can run at most FPS
        clock.tick(fps)

        #fills the game and adjust for color
        window.fill((150,40,30))

        #show the player in the game screen based on the render function in Player Class
        player1.render(window)

        #Display Obstacle in the render function
        obstacle1.render(window)

        # put code here that should be run every frame
        # of your game
        pygame.display.update()


main()

