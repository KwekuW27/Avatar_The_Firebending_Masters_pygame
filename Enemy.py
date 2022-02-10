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

    def __init__(enemyself, _x, _y):
        enemyself.x = _x
        enemyself.y = _y

        # render function
    def render(enemyself, aSurface):
        enemyShip = pygame.Rect(enemyself.x, enemyself.y, enemyself.width, enemyself.height)

        #Drawing Rectangle
        pygame.draw.rect(aSurface, (255,255,255), enemyShip)