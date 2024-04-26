from pygame import *
from random import randint

# Initialize Pygame
init()

# Set up display
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter")

# Load images
img_back = "galaxy.jpg"
img_hero = "rocket.png"
img_enemy = "ufo.png"
img_bullet = "bullet.png"

background = transform.scale(image.load(img_back), (win_width, win_height))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

# Load fonts
font.init()
font2 = font.Font(None, 36)

# Initialize game variables
score = 0
lost = 0

# Define game classes
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

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
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

# Create sprites
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
monsters = sprite.Group()
bullets = sprite.Group()

# Create monsters
for _ in range(randint(6 , 15)):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

# Main game loop
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    keys = key.get_pressed()
    if keys[K_SPACE]:
        bullet = Bullet(img_bullet, ship.rect.x + 30, ship.rect.y, 10, 20, 15)
        bullets.add(bullet)
        fire_sound.play()

    window.blit(background, (0, 0))
    ship.update()
    ship.reset()

    for monster in monsters:
        monster.update()
        monster.reset()

    for bullet in bullets:
        bullet.update()
        bullet.reset()

    # Collisions
    collisions = sprite.groupcollide(bullets, monsters, True, True)
    for bullet, monsters_hit in collisions.items():
        score += len(monsters_hit)

    # Draw texts
    text = font2.render("Score: " + str(score), 1, (255, 255, 255))
    window.blit(text, (10, 20))

    text_lose = font2.render("Missed: " + str(lost), 1, (255, 255, 255))
    window.blit(text_lose, (10, 60))

    # Inside the main game loop:

# Check for collisions between player and monsters
    if sprite.spritecollide(ship, monsters, False):
        text = font2.render("Defeat", 1, (255, 255, 255))
        window.blit(text, (60, 90))
        run = False  # End the game if player collides with a monster

# Check for defeat condition
    if lost == 3:
        text = font2.render("Defeat", 1, (255, 255, 255))
        window.blit(text, (60, 90))
        run = False  # End the game if player loses 3 monsters

# Check for victory condition
    if score == 10:
        text = font2.render("Victory", 1, (255, 255, 255))
        window.blit(text, (60, 90))
        run = False  # End the game if player scores 10 points




    display.update()
    time.delay(50)
