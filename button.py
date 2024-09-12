import pygame,math
from pygame import*
from math import*


clock = time.Clock()

#button class
class Button():
    def __init__(self,x,y,image,image2, scale) -> None:
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale),int(height * scale)))
        self.image2 = pygame.transform.scale(image2, (int(width * scale),int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    #draw button 
    def draw(self,surface):
        action = False
        mouse_over = False

        #mouse position
        pos = mouse.get_pos()

        #check mouse over and clicked conditions
        if self.rect.collidepoint(pos):
            mouse_over = True
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #display button
        if mouse_over == False:
            surface.blit(self.image, (self.rect.x, self.rect.y))
        elif mouse_over == True:
            surface.blit(self.image2, (self.rect.x, self.rect.y))

        return action
    
    