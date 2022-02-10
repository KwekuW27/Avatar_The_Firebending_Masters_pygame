import pygame

class Obstacle:

    ### global call vars###
    width = 40
    height = 40
    speed = 1
    #constructor function
    #health
    #width
    #height
    #speed
    #x
    #y
    #isDead

    def __init__(obtacleself, _x, _y):
        obtacleself.x = _x
        obtacleself.y = _y

        # render function
    def render(obstacleself, aSurface):
        enemyObstacle = pygame.Rect(obstacleself.x, obstacleself.y, obstacleself.width, obstacleself.height)

        #Drawing Rectangle
        pygame.draw.rect(aSurface, (255,255,255), enemyObstacle)