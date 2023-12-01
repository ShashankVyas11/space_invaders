import pygame
import sys
import random

space_ship = "?"
rocket = "?"

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Shooter")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 5

# Alien settings
alien_size = 50
alien_speed = 2
aliens = []

# Bullet settings
bullet_speed = 7
bullets = []

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to draw the player
def draw_player(x, y):
    win.blit(pygame.font.Font(None, 36).render(rocket, True, WHITE), (x, y))

# Function to draw an alien
def draw_alien(x, y):
    win.blit(pygame.font.Font(None, 36).render(space_ship, True, WHITE), (x, y))

# Function to draw a bullet
def draw_bullet(x, y):
    pygame.draw.rect(win, WHITE, [x, y, 5, 10])

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move the player
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Shoot bullets
    if keys[pygame.K_SPACE]:
        bullets.append([player_x + player_size // 2 - 2, player_y])

    # Move bullets
    for bullet in bullets:
        bullet[1] -= bullet_speed

    # Spawn aliens
    if random.randint(0, 100) < 2:
        aliens.append([random.randint(0, WIDTH - alien_size), 0])

    # Move aliens
    for alien in aliens:
        alien[1] += alien_speed

    # Check for collisions
    for bullet in bullets[:]:
        for alien in aliens[:]:
            if (
                alien[0] < bullet[0] < alien[0] + alien_size
                and alien[1] < bullet[1] < alien[1] + alien_size
            ):
                aliens.remove(alien)
                bullets.remove(bullet)

    # Draw everything
    win.fill((0, 0, 0))  # Black background
    draw_player(player_x, player_y)
    for alien in aliens:
        draw_alien(alien[0], alien[1])
    for bullet in bullets:
        draw_bullet(bullet[0], bullet[1])

    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)