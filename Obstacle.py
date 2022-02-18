import pygame

class Obstacle:

    ### global call vars###
    speed = 2
    #constructor function
    #health
    #width
    #height
    #speed
    #x
    #y
    #isDead


    def __init__(self, x, y, w, h, image):
        self.width = w 
        self.height = h
        self.x = x
        self.y = y
        self.image = image
        self.obstacleHitbox = pygame.Rect(self.x, self.y, self.width, self.height)


        # render function
    def render(self, aSurface):
        self.obstacleHitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        #Drawing Rectangle
        # pygame.draw.rect(aSurface, (255,255,255), self.obstacleHitbox)

        #filling with selected image
        aSurface.blit(self.image,(self.x, self.y-5))