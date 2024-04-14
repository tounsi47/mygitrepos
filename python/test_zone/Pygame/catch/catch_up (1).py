from pygame import *

#create game window
init()
pywin = display.set_mode((700 , 500))
display.set_caption("Catch")
clock = time.Clock()
FPS = 60
x1 = 100
y1 = 300
x2 = 300
y2 = 300
#set scene background
background  = transform.scale(image.load('background.png') , (700 , 500))
#creat 2 sprites and place them on the scene
sprite1 = transform.scale(image.load('sprite1.png'), (100 , 80))
sprite2 = transform.scale(image.load('sprite2.png'), (100 , 80))
#handle "click on the "Close the window"" event 
game = True
while game : 
    pywin.blit(background, (0 , 0))
    
    for e in event.get():
        if e.type == QUIT :
            game = False
    keys_pressed = key.get_pressed()

    if keys_pressed[K_DOWN]:
        y1 += 10
    if keys_pressed[K_UP]:
        y1 -= 10
    if keys_pressed[K_LEFT]:
        x1 -= 10
    if keys_pressed[K_RIGHT]:
        x1 += 10

    if keys_pressed[K_d]:
        y2 += 10
    if keys_pressed[K_u]:
        y2 -= 10
    if keys_pressed[K_l]:
        x2 -= 10
    if keys_pressed[K_r]:
        x2 += 10    

    pywin.blit(sprite1 , (x1, y1))
    pywin.blit(sprite2 , (x2 , y2))


    clock.tick(FPS)
    display.update()