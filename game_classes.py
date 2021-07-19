import pygame
import random


class Trump:
    def __init__(self):
        self.x = 250
        self.y = 425
        self.vel = 10
        self.rect = pygame.Rect(self.x, self.y, 50, 100)
        self.lives = 3
        self.img = pygame.image.load('Assets/trump.png').convert_alpha()
        self.jump_vel = 20
        self.jumping = False

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, 50, 100)

    def draw(self, s):
        self.update_rect()
        s.blit(self.img, (self.x, self.y))

    def move(self, s):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.x + self.vel <= 750:
            self.x += self.vel
            self.draw(s)
        if keys[pygame.K_a] and self.x - self.vel > 0:
            self.x -= self.vel
            self.draw(s)

    def jump(self, s):
        if self.jumping:
            self.y -= self.jump_vel
            self.jump_vel -= 1
            self.draw(s)
            if self.jump_vel == -21:
                self.jump_vel = 20
                self.jumping = False
