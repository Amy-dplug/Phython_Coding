#-----------------------------------------------------------------------------
# Name:        Basic Pygame code to try (Basic_Pygame_code_to_try.py)
# Purpose:     To understand how Pygame works on a simple code on this
#			   work in Github and Pycharm
#
# Author:      Amy Egwumba
# Created:     27-May-2025
# Updated:     27-May-2025
#-----------------------------------------------------------------------------
import pygame
# import os

# Initialize pygame
pygame.init()

# Set up the game window
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game")

# Set up clock
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player setup
x = screen_width // 2 - 25
y = screen_height // 2 - 25
speed = 5
player_width = 50
player_height = 50

# Try to load image
try:
    player_image = pygame.image.load("assets/player.png")
    use_image = True
except:
    print("⚠️ Couldn't load image. Using red square.")
    use_image = False

# Try to load sound
try:
    jump_sound = pygame.mixer.Sound("assets/jump.wav")
    sound_loaded = True
except:
    print("⚠️ Couldn't load sound.")
    sound_loaded = False

# Game loop
running = True
while running:
    clock.tick(60)  # 60 FPS

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_SPACE] and sound_loaded:
        jump_sound.play()

    # Prevent player from going off-screen
    if x < 0:
        x = 0
    if x + player_width > screen_width:
        x = screen_width - player_width
    if y < 0:
        y = 0
    if y + player_height > screen_height:
        y = screen_height - player_height

    # Draw background
    screen.fill(BLACK)

    # Draw player
    if use_image:
        screen.blit(player_image, (x, y))
    else:
        pygame.draw.rect(screen, RED, (x, y, player_width, player_height))

    # Update the display
    pygame.display.flip()

# Quit pygame when done
pygame.quit()

