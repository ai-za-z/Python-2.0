import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Color Change")

# Colors
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]

# Custom event
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)  # Change color every 2 seconds

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(random.choice(COLORS))
        self.rect = self.image.get_rect(topleft=(x, y))

    def change_color(self):
        self.image.fill(random.choice(COLORS))

# Create two sprites
sprite1 = Sprite(150, 150)
sprite2 = Sprite(300, 150)

# Grouping sprites
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CHANGE_COLOR:
            sprite1.change_color()
            sprite2.change_color()

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
