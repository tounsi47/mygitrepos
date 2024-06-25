#This is the other part of our project : the game part
from pygame import * 
from time import time as timer
from random import *
'''The pygame, time and random module will be used for the game only'''

#1-creating and setting up the display variable
win_lenght = 1100
win_width = 550
gamewin = display.set_mode((win_lenght , win_width))
display.set_caption('Super mario python edition')
#2-importing needed files (pictures and sounds)
img_background = "environnement\normal\background.png"
img_player = "sprites\hero\mario.png"
img_goomba = "sprites\enemies\Goomba.png"
img_koopa = "sprites\enemies\koopa.png"
'''They are other pictures and sounds we'll import them, but not now'''
#3-creating the game classes
#4-creating the game objects
background = transform.scale(image.load(img_background) , (win_lenght , win_lenght))
#5-creating the game loop
'''creating the loop parameters'''
run = True#this parameter is to run the game or not
finish = False#this parameter is to finsih (stop) the game or keep it
while run : #with run = True
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish :
        gamewin.blit(background , (0,0))
        display.update()
