#Player class
import pygame

class Player:
    

    #__________________________________________________________________________
    #  Unchanging CLASS VARIABLES
    #__________________________________________________________________________

    health = 10
    w = 100
    h = 100
    speed = 10
    isDead = False

#__________________________________________________________________________
# CONSTRUCTOR
#__________________________________________________________________________

    def __init__(self, tempX, tempY):

        #give different starting values for each of your players
        self.x = tempX
        self.y = tempY

#Render Function
    def render(self, aSurface):

        #make a rectangle and then render it at a location
        playerRect = pygame.Rect(self.x, self.y, self.w, self.h,)

        # surface = WINDOW, color(RGB spect), playerRect
        pygame.draw.rect(aSurface, (255, 0, 255), playerRect)
