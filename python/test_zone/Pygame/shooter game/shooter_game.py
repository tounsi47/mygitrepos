#Create your own shooter

from pygame import *
pywin = display.set_mode((700 , 500))
display.set_caption('pygame window')
background = transform.scale(image.load('galaxy.jpg'), (700 , 500))
mixer.init()
mixer.music.load('fire.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
player = 'rocket.png'
enemy = 'ufo.png'
class GameSprite(sprite.Sprite):
   #class constructor
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       #every sprite must store the image property
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       #every sprite must have the rect property – the rectangle it is fitted in
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       pywin.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
   def fire():
       pass
class Enemy(GameSprite):
    direction = "up"
    def update(self):
       if self.rect.y <= 470:
           self.direction = "down"
       if self.rect.y >= win_height - 85:
           self.direction = "up"


       if self.direction == "up":
           self.rect.y -= self.speed
       else:
           self.rect.y += self.speed
   
        
        

       



win_width = 700
win_height = 500
clock = time.Clock()
FPS = 60
finish = False
game = True
player = Player(player, 5, win_height - 80, 4)
hacker = Enemy(enemy, 8 , win_height - 400 , 4)
while game :
    for e in event.get():
        if e.type == QUIT:
            game  = False
    if finish != True :
        pywin.blit(background, (0 , 0))
        player.update()
        hacker.update()
        player.reset()
        hacker.reset()
       
    
    display.update()
    clock.tick(FPS)



