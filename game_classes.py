import pygame
import random


class Trump:
    def __init__(self):
        self.x = 250
        self.y = 250
        self.vel = 10
        self.rect = pygame.Rect(self.x, self.y, 50, 100)
