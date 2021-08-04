"""
This game is still a work in progress. All code here is subject to change. I welcome any and all advice/feedback.
Please fork and do a PR if you have any changes you'd like to implement.
                                -VeinyAngus (MattMuelot)
"""
import pygame
from level import Level

# ------------- Initialize Pygame, create screen and clock objects --------------#

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# --------------------- MAIN GAME LOOP --------------------- #

levels = [Level(1, screen, clock, 60), Level(2, screen, clock, 60), Level(3, screen, clock, 60)]

for l in levels:
    if l.lev == 1:
        pygame.mixer.music.load('Assets/level1.mp3')
        pygame.mixer.music.play(-1)
        l.game_level()
    if l.lev == 2:
        pygame.mixer.music.load('Assets/level2.mp3')
        pygame.mixer.music.play(-1)
        l.game_level()
    if l.lev == 3:
        pygame.mixer.music.load('Assets/level3.mp3')
        pygame.mixer.music.play(-1)
        l.game_level()
