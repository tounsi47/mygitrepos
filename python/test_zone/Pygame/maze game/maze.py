from pygame import *

font.init()

# Parent class for sprites
class GameSprite(sprite.Sprite):
    # Class constructor
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        # Every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        # Every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Child class for the player sprite (controlled by arrows)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

# Child class for the enemy sprite (moves by itself)
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

# Wall class for obstacles
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Game scene dimensions
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

# Game characters
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
w1 = Wall(34, 139, 34, 100, 20, 10, 380)
w2 = Wall(34, 139, 34, 100, 480, 350, 10)
w3 = Wall(34, 139, 34, 100, 20, 10, 380)

# Text font objects
font_win = font.Font(None, 50)
font_lose = font.Font(None, 50)

# Game variables
game = True
finish = False
clock = time.Clock()
FPS = 60

# Music
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish == False:
        window.blit(background, (0, 0))
        player.update()
        monster.update()
        w1.draw()
        w2.draw()
        w3.draw()
        final.reset()

        # Check collision with treasure
        if sprite.collide_rect(player, final):
            mixer.init()
            mixer.music.load('money.ogg')
            mixer.music.play()

            text_win = font_win.render("YOU WIN!", True, (255, 255, 255))
            window.blit(text_win, (win_width // 2 - 100, win_height // 2))
            finish = True

        # Check collision with walls or enemy
        if sprite.spritecollide(player, [w1, w2, w3], False) or sprite.collide_rect(player, monster):
            mixer.init()
            mixer.music.load('kick.ogg')
            mixer.music.play()
    
            text_lose = font_lose.render("YOU LOSE!", True, (255, 255, 255))
            window.blit(text_lose, (win_width // 2 - 120, win_height // 2))
            finish = True

        player.reset()
        monster.reset()

    display.update()
    clock.tick(FPS)

