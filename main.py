import pygame,math,button,background
from pygame import *
from math import*
from button import*
from background import*



pygame.init()
pygame.display.set_caption("Made in Heaven")
screen = pygame.display.set_mode((0,0))
screen_width , screen_height = screen.get_size() 

git 
screen_state = "main"   #main, game, options

background = Background('background_img.png', [0,0])

clicked = False

#title image
title_img = image.load('titre_image.png').convert_alpha()

#button image
exit_img = image.load('quit_button.png').convert_alpha()
exit_img2 = image.load('quit_button_2.png').convert_alpha()
play_img = image.load('play_button.png').convert_alpha()
play_img2 = image.load('play_button_2.png').convert_alpha()
options_img = image.load('options_button.png').convert_alpha()
options_img2 = image.load('options_button_2.png').convert_alpha()
back_img = image.load('back_button.png').convert_alpha()
back_img2 = image.load('back_button_2.png').convert_alpha()



#create button
exit_button = Button(screen_width/2-200,screen_height-300,exit_img,exit_img2,1)
options_button = Button(screen_width/2-200,screen_height-550,options_img,options_img2,1)
play_button = Button(screen_width/2-200,screen_height-800,play_img,play_img2,1)
back_button = Button(screen_width/2-200,screen_height-300,back_img,back_img2,1)

#game loop
running = True
while running:

    screen.fill([255, 255, 255])
    screen.blit(background.ground, background.rect)

    #main screen
    if screen_state == "main":
        screen.blit(title_img,(screen_width/2-750,screen_height-1900))
        if exit_button.draw(screen) and not clicked:
            running = False
        if play_button.draw(screen) and not clicked:
            screen_state = "game"
            clicked = True
        if options_button.draw(screen) and not clicked:
            screen_state = "options"
            clicked = True

    #game screen
    if screen_state == "game":
        pass

    #options screen
    if screen_state == "options":
        screen.blit(title_img,(screen_width/2-750,screen_height-1900))
        if back_button.draw(screen) and not clicked:
            screen_state = "main"
            clicked = True

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            running = False
        #quit when escape is pressed
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE and screen_state == "game":
                screen_state = "main"
        #to don't click two button simultaneously
        if event.type == pygame.MOUSEBUTTONUP:
                clicked = False


    
    #refresh window
    pygame.display.flip()

pygame.quit()

