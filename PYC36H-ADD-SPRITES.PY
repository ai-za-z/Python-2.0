import pygame

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Sprite")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Sprite settings
player_speed = 5

# Define sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= player_speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += player_speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= player_speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += player_speed

# Create two sprites
player = Sprite(150, 150, BLUE)  # Movable sprite
static_sprite = Sprite(300, 150, RED)  # Static sprite

# Group sprites
all_sprites = pygame.sprite.Group(player, static_sprite)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move(keys)

    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
