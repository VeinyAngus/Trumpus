import pygame
import random


class Trump:
    def __init__(self):
        self.x = 250
        self.y = 370
        self.x_vel = 5
        self.y_vel = 5
        self.rect = pygame.Rect(self.x, self.y, 50, 100)
        self.lives = 5
        self.money = 5
        self.money_shot = []
        self.img = pygame.image.load('Assets/trump.png').convert_alpha()
        self.jump_vel = 20
        self.jumping = False
        self.wave = 0
        self.agents_left = 25

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
            if keys[pygame.K_w] and self.y - self.y_vel > 370:
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
        self.y = random.randint(400, 550)
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.img = pygame.image.load('Assets/declaration.png').convert_alpha()
        self.burn_img = pygame.image.load('Assets/burnedec.png').convert_alpha()
        self.timer = False
        self.its = 0

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def draw(self, s):
        if self.timer is False:
            self.update_rect()
            s.blit(self.img, (self.x, self.y))
            return False
        elif self.timer:
            self.update_rect()
            s.blit(self.burn_img, (self.x, self.y))
            self.its += 1
            if self.its >= 30:
                return True

    def move(self, s):
        self.x -= 2
        self.update_rect()
        if self.x < -50:
            return True


class Moneybag:
    def __init__(self):
        self.x = random.randint(900, 3000)
        self.y = random.randint(370, 550)
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.img = pygame.image.load('Assets/moneybag.png').convert_alpha()

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def draw(self, s):
        self.update_rect()
        s.blit(self.img, (self.x, self.y))

    def move(self, s):
        self.x -= 2
        self.draw(s)
        if self.x < -50:
            return True


class Bill:
    def __init__(self, t):
        self.x = t.x + 28
        self.y = t.y + 45
        self.vel = 10
        self.rect = pygame.Rect(self.x, self.y, 35, 15)
        self.img = pygame.image.load('Assets/bill-35-15.png')

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, 35, 15)

    def draw(self, s):
        self.update_rect()
        s.blit(self.img, (self.x, self.y))

    def move(self, s):
        self.x += self.vel
        self.draw(s)
        if self.x > 800:
            return True


class Bullet:
    def __init__(self, a):
        self.x = a.x - 6
        self.y = a.y + 33
        self.vel = 6
        self.rect = pygame.Rect(self.x, self.y, 10, 5)
        self.img = pygame.image.load('Assets/bullet.png').convert_alpha()

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, 10, 5)

    def draw(self, s):
        self.update_rect()
        s.blit(self.img, (self.x, self.y))

    def move(self, s):
        self.x -= self.vel
        self.draw(s)
        if self.x < 0:
            return True


class SecretService:
    def __init__(self):
        self.x = random.randint(900, 3000)
        self.y = random.randint(400, 500)
        self.rect = pygame.Rect(self.x, self.y, 50, 100)
        self.img = pygame.image.load('Assets/agent.png').convert_alpha()
        self.shoot_hold = False
        self.shots = []
        self.counter = 4000

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, 50, 100)

    def draw(self, s):
        self.update_rect()
        s.blit(self.img, (self.x, self.y))

    def move(self, s):
        self.x -= 2
        self.draw(s)
        if self.x < -50:
            return True


class Heart:
    def __init__(self):
        self.x = random.randint(900, 8000)
        self.y = random.randint(400, 550)
        self.rect = pygame.Rect(self.x, self.y, 25, 25)
        self.img = pygame.image.load('Assets/heart.png').convert_alpha()

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, 25, 25)

    def draw(self, s):
        self.update_rect()
        s.blit(self.img, (self.x, self.y))

    def move(self, s):
        self.x -= 2
        self.draw(s)
        if self.x < -50:
            return True
