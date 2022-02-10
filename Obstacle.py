#Obstacle class
import pygame

class Obstacle:
    

    #__________________________________________________________________________
    #  Unchanging CLASS VARIABLES
    #__________________________________________________________________________

    damage = 1
    w = 50
    h = 50

    #Update Obstacle position to front of player Character
    OffScreen = False

#__________________________________________________________________________
# CONSTRUCTOR
#__________________________________________________________________________

    def __init__(self, tempX, tempY):

        #give different starting values for each of your obstacles
        self.x = tempX
        self.y = tempY

#Render Function
    def render(self, aSurface):

        #make a rectangle and then render it at a location
        ObstacleRect = pygame.Rect(self.x, self.y, self.w, self.h,)

        # surface = WINDOW, color(RGB spect), playerRect
        pygame.draw.rect(aSurface, (253, 94, 83), ObstacleRect)
