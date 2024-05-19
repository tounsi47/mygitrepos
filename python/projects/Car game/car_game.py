from pygame import *
win_width = 1274
win_height = 1139
init()
pywin = display.set_mode((win_width, win_height))
display.set_caption('Car game')

background = transform.scale(image.load('Background.jpg'), (win_width , win_height))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        pywin.blit(self.image, (self.rect.x, self.rect.y))
class main_car(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
my_car = GameSprite('main_car.png' , 680 , 600 , 150 , 300, 10)
finish = False

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        pywin.blit(background, (0 , 0))
        my_car.update()
        my_car.reset()
        display.update()
        time.delay(50)


