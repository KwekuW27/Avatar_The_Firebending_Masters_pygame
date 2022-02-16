
import pygame

class Animation:

    #global class variables

    isMoving = True
    isAnimating = True
    index = 0

    animationList = []



    # This is your constructor -- put what you needed as inputs in your game, HERE!!
    def __init__(self, tempImages, tempSpeed, tempScale):
     
    
     self.images = tempImages
     self.speed = tempSpeed
     self.scale = tempScale


    #increase the index of the animation and go to the next frame
    def next(self):

        self.index += self.speed

        if (self.index >= len(self.images)):
            self.index = 0
            # isAnimating = False
    

    #display the player when it IS animating
    def display (self, aSurface, animationX, animationY):

        # if (self.isAnimating == True):
         imageIndex = int(self.index)
         img = self.images[imageIndex]
         aSurface.blit(img,(animationX, animationY))

         self.next()

        # else:
        #     img = self.images[0]
        #     aSurface.blit(img,(animationX, animationY))
