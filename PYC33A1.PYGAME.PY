import pygame

# initialize the game
pygame.init()

# Creating a game window
screen = pygame.display.set_mode((800,600))

# Caption And Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("images.jpeg")
pygame.display.set_icon(icon)


# insert a spacecraft image
playerImg = pygame.image.load("images.jpeg")
playerX = 300
playerY = 400

def player():
    screen.blit(playerImg,(playerX, playerY))



# Running
running = True
while running:
    # RGB - (0,0,0) to (255,255,255)
    screen.fill((68, 193, 242))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    player()
    pygame.display.update()

