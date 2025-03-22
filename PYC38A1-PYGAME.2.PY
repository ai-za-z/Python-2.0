import pygame
import random

# Initialize Pygame
pygame.init()

# Define custom events for color changes
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# Define colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

# Screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-2, -1, 1, 2]), random.choice([-2, -1, 1, 2])]

    def update(self):
        boundary_hit = False  # Initialize variable
        self.rect.move_ip(*self.velocity)  # Move sprite

        # Check for collision with screen boundaries
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True  # Set to True when bouncing

        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def change_color(self):
        """Change the sprite's color randomly."""
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))


def change_background_color():
    """Change the background color randomly."""
    global bg_color
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])


# Create a sprite group
all_sprites_list = pygame.sprite.Group()

# Instantiate and position the sprite
sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randint(0, SCREEN_WIDTH - sp1.rect.width)
sp1.rect.y = random.randint(0, SCREEN_HEIGHT - sp1.rect.height)

all_sprites_list.add(sp1)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Boundary Sprite")

# Initial background color
bg_color = BLUE

# Game loop control flag
running = True

# Clock to control frame rate
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    # Update sprites
    all_sprites_list.update()

    # Fill screen with background color
    screen.fill(bg_color)

    # Draw sprites
    all_sprites_list.draw(screen)

    # Refresh the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

pygame.quit()
