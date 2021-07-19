import pygame
from game_classes import Trump, Declaration
import random

# Initialize Pygame, create screen and clock objects

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load background and audio files

bg = pygame.image.load('Assets/background.png').convert_alpha()
pygame.mixer.set_num_channels(16)
pygame.mixer.music.load('Assets/maintheme.mp3')
pygame.mixer.music.play(-1)

# Create game objects

trump = Trump()
decs = [Declaration() for _ in range(10)]

# Main Game Loop

i = 0
running = True
while running:
    clock.tick(60)  # Set FPS To 60
    screen.blit(bg, (i, 0))
    screen.blit(bg, (3200 + i, 0))
    i -= 1
    if i == -3200:
        screen.blit(bg, (3200 + i, 0))
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
    for d in decs[:]:
        off_screen = d.move(screen)
        if off_screen:
            decs.remove(d)
    if len(decs) <= 0:
        decs = [Declaration() for _ in range(10)]
    if trump.jumping:
        trump.jump(screen)
    trump.draw(screen)
    trump.move(screen)
    pygame.display.update()
