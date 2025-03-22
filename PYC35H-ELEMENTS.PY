import pygame

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Game Elements")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Font settings
font = pygame.font.Font(None, 36)  # Default font, size 36
text = font.render("Hello, Pygame!", True, BLACK)  # Render text
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center the text

# Game loop
running = True
while running:
    screen.fill(WHITE)  # Fill the screen with white

    # Draw a blue rectangle
    pygame.draw.rect(screen, BLUE, (150, 100, 200, 100))  # (x, y, width, height)

    # Draw text
    screen.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Update the display
    pygame.time.delay(30)  # Delay to control frame rate

pygame.quit()
