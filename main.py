"""
This game is still a work in progress. All code here is subject to change. I welcome any and all advice/feedback.
Please fork and do a PR if you have any changes you'd like to implement.
                                -VeinyAngus (MattMuelot)
"""
import pygame
from level import Levels
from menu_screens import Menus


# ------------- Initialize Pygame, create screen and clock objects --------------#

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# --------------------- MAIN GAME LOOP --------------------- #
