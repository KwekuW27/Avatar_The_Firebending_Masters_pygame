print("github repository test")

import pygame
from sqlalchemy import true #import

#defining WINDOW SIZE
width = 1000 
height = 1000 

#display WINDOW
window = pygame.display.set_mode((width, height))

#name the game WINDOW
pygame.display.set_caption("avatar_pyGame")

#frame rate of game
fps = 60

def main():
# to make the game RUN at a consistent framerate
    clock = pygame.time.Clock()

    running = True #capitalized T = boolean

    while running:

       #this makes it so this function can run at most FPS
        clock.tick(fps)

        #fills the game and adjust for color
        window.fill((150,40,30))

        # put code here that should be run every frame
        # of your game
        pygame.display.update()


main()

