import pygame

class FlamingFireBall:

###global vars###
    width = 5
    height = 5
    speed = 10

#constructor function
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.flamingFireBallHitbox = pygame.Rect(self.x, self.y, self.width, self.height)

         # render function
    def render(self, aSurface):
        self.flamingFireBallHitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        #Drawing Rectangle
        pygame.draw.rect(aSurface, (255,255,255), self.flamingFireBallHitbox)