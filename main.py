import pygame
from game_classes import Trump
import random

# Initialize Pygame, create screen and clock objects

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create game objects

trump = Trump()

# Main Game Loop

running = True
while running:
    clock.tick(60)  # Set FPS To 60
    screen.fill((0, 0, 0))  # Fill screen with black for the time being until background is created
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
