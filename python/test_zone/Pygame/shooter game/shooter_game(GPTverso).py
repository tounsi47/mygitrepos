from pygame import *
from random import randint

# Initialize Pygame
init()

# Set up display
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))

# Load images and sounds
img_back = "galaxy.jpg"
img_hero = "rocket.png"
img_enemy = "ufo.png"
img_bullet = "bullet.png"
mixer.init()
mixer.music.load('space.ogg')
fire_sound = mixer.Sound('fire.ogg')

# Fonts
font.init()
font2 = font.Font(None, 36)

# Game variables
score = 0
lost = 0

# Background music
mixer.music.play(-1)  # Loop indefinitely

# Game classes
class GameSprite(sprite.Sprite):
    def __init__(self, image, x, y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(img_bullet, self.rect.x + 20, self.rect.y, 10, 20, -10)
        bullets.add(bullet)
        fire_sound.play()

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            global lost
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()  # Remove bullet if it goes off-screen


# Load images
background = transform.scale(image.load(img_back), (win_width, win_height))
player = Player(image.load(img_hero), 5, win_height - 100, 80, 100, 10)  # Corrected line
enemies = sprite.Group()
bullets = sprite.Group()

# Create enemies
for _ in range(5):
    enemy = Enemy(image.load(img_enemy), randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    enemies.add(enemy)

# Main game loop
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not lost:
        window.blit(background, (0, 0))

        for bullet in bullets:
            bullet.update()

        player.update()
        player.reset()

        enemies.update()
        enemies.draw(window)

        bullets.draw(window)

        # Collision detection between bullets and enemies
        hits = sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            score += 1
            enemy = Enemy(image.load(img_enemy), randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            enemies.add(enemy)

        # Display score
        text = font2.render("Score: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        display.update()
        time.delay(50)
