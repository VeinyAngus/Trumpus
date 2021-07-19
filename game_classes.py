import pygame
import random


class Trump:
    def __init__(self):
        self.x = 250
        self.y = 415
        self.x_vel = 10
        self.y_vel = 5
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
        if keys[pygame.K_d] and self.x + self.x_vel <= 750:
            self.x += self.x_vel
            self.draw(s)
        if keys[pygame.K_a] and self.x - self.x_vel > 0:
            self.x -= self.x_vel
            self.draw(s)
        if self.jumping:
            pass
        else:
            if keys[pygame.K_w] and self.y - self.y_vel > 415:
                self.y -= self.y_vel
                self.draw(s)
            if keys[pygame.K_s] and self.y + self.y_vel < 500:
                self.y += self.y_vel
                self.draw(s)

    def jump(self, s):
        """During main game loop, if the player jumping attribute is true, it will run"""
        if self.jumping:
            self.y -= self.jump_vel
            self.jump_vel -= 1  # For realistic jumping, velocity slows down as player reaches apex of jump
            self.draw(s)  # Draw character to screen based upon current x and y coordinates
            if self.jump_vel == -21:  # If we have reached our starting position, reset jump velocity/set to false
                self.jump_vel = 20
                self.jumping = False


class Declaration:
    def __init__(self):
        self.x = random.randint(900, 3000)
        self.y = random.randint(415, 550)
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.img = pygame.image.load('Assets/declaration.png').convert_alpha()

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, 50, 100)

    def draw(self, s):
        self.update_rect()
        s.blit(self.img, (self.x, self.y))

    def move(self, s):
        self.x -= 1
        self.update_rect()
        self.draw(s)
        if self.x < -50:
            return True
