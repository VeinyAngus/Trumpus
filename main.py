import pygame
from game_classes import Trump
import random

# Initialize Pygame, create screen and clock objects

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load background

bg = pygame.image.load('Assets/background.png').convert_alpha()

# Create game objects

trump = Trump()

# Main Game Loop

i = 0
running = True
while running:
    clock.tick(60)  # Set FPS To 60
    screen.blit(bg, (i, 0))
    screen.blit(bg, (800 + i, 0))
    i -= 1
    if i == -800:
        screen.blit(bg, (800 + i, 0))
        i = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                if trump.jumping:
                    pass
                else:
                    trump.jumping = True
    if trump.jumping:
        trump.jump(screen)
    trump.draw(screen)
    trump.move(screen)
    pygame.display.update()
