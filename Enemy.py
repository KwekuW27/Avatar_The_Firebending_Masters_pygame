import pygame

class Enemy:

    ### global call vars###
    width = 70
    height = 40
    speed = 2
    #constructor function
    #health
    #width
    #height
    #speed
    #x
    #y
    #isDead

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.enemyHitbox = pygame.Rect(self.x, self.y, self.width, self.height)


        # render function
    def render(self, aSurface):
        self.enemyHitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        #Drawing Rectangle
        pygame.draw.rect(aSurface, (255,255,255), self.enemyHitbox)