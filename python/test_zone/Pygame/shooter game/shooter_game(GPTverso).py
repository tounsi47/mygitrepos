from pygame import *
import random

# Initialize Pygame


# Set up the display
win_width = 700
win_height = 500
pywin = display.set_mode((win_width, win_height))
display.set_caption('pygame window')

# Load resources
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))
fire_sound = mixer.Sound('fire.ogg')

# Define the player and enemy classes
class GameSprite(sprite.Sprite):
    def __init__(self, image, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image), (65, 65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        pywin.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_SPACE]:
            self.fire()

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top)
        bullets.add(bullet)
        fire_sound.play()

class Enemy(GameSprite):
    def __init__(self, image, x, y, speed):
        super().__init__(image, x, y, speed)
        self.direction = random.choice(['up', 'down'])

    def update(self):
        if self.rect.y <= 0:
            self.direction = "down"
        if self.rect.y >= win_height - 65:
            self.direction = "up"

        if self.direction == "up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Bullet(GameSprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y, -10)

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

clock = time.Clock()
FPS = 60

# Create sprite groups
all_sprites = sprite.Group()
bullets = sprite.Group()

# Create player and enemy instances
player = Player('rocket.png', 5, win_height - 80, 4)
enemy = Enemy('ufo.png', 5, win_height - 400, 4)

# Add sprites to sprite groups
all_sprites.add(player, enemy)

# Main game loop
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    # Update
    all_sprites.update()

    # Check for collisions
    hits = sprite.groupcollide(bullets, all_sprites, True, True)
    for hit in hits:
        enemy = Enemy('ufo.png', random.randint(0, win_width - 65), win_height, 4)
        all_sprites.add(enemy)

    # Render
    pywin.blit(background, (0, 0))
    all_sprites.draw(pywin)

    display.update()
    clock.tick(FPS)

