import pygame
import random
import json
# -------------------------------------- TRUMP (PLAYER) CLASS ------------------------------------------ #


class Trump:
    """Our main player object"""
    def __init__(self):
        self.x = 250
        self.y = 370
        with open('config_files/level_settings.json', 'r') as f:
            self.data = json.load(f)
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
        """Updates the objects Rect using the current x and y values"""
        self.rect = pygame.Rect(self.x, self.y, 50, 100)

    def draw(self, s):
        """Draws the img attribute to screen on the current x and y values"""
        self.update_rect()
        s.blit(self.img, (self.x, self.y))

    def move(self, s):
        """Corresponding key presses move player in multiple directions"""
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

    def reset(self):
        self.x = 250
        self.y = 370
        self.lives = 5
        self.money = 5
        self.money_shot = []
        self.wave = 0
        self.agents_left = 25


# -------------------------------------- DECLARATION CLASS ------------------------------------------- #


class Declaration:
    """One of the enemy objects. This object moves in sync with the background to give an illusion
    of being static in relation to the background"""
    def __init__(self):
        self.x = random.randint(900, 3000)
        self.y = random.randint(400, 550)
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.img = pygame.image.load('Assets/declaration.png').convert_alpha()
        self.burn_img = pygame.image.load('Assets/burnedec.png').convert_alpha()
        self.timer = False
        self.its = 0

    def update_rect(self):
        """Updates the objects Rect using the current x and y values"""
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def draw(self, s):
        """Draws the img attribute to screen on the current x and y values"""
        if self.timer is False:
            self.update_rect()
            s.blit(self.img, (self.x, self.y))
            return False
        # self.timer attribute will be true if struck by a projectile
        # and will show the burn image for 30 frames
        elif self.timer:
            self.update_rect()
            s.blit(self.burn_img, (self.x, self.y))
            self.its += 1
            if self.its >= 30:
                return True

    def move(self, s):
        """x moves -2 for each game-loop to maintain pace with game background, so object appears static"""
        self.x -= 2
        self.update_rect()
        if self.x < -50:
            return True


# ------------------------------------------ MONEYBAG CLASS ----------------------------------------------- #


class Moneybag:
    """Bag of money object. Player needs to collide with these to collect it"""
    def __init__(self):
        self.x = random.randint(900, 3000)
        self.y = random.randint(370, 550)
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.img = pygame.image.load('Assets/moneybag.png').convert_alpha()

    def update_rect(self):
        """Updates the objects Rect using the current x and y values"""
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def draw(self, s):
        """Draws the img attribute to screen on the current x and y values"""
        self.update_rect()
        s.blit(self.img, (self.x, self.y))

    def move(self, s):
        """x moves -2 for each game-loop to maintain pace with game background, so object appears static"""
        self.x -= 2
        self.draw(s)
        if self.x < -50:
            return True


# -------------------------------------------- BILL CLASS ------------------------------------------------ #


class Bill:
    """This is the projectile that is created when the player fires"""

    def __init__(self, t):
        self.x = t.x + 28
        self.y = t.y + 45
        self.vel = 10
        self.rect = pygame.Rect(self.x, self.y, 35, 15)
        self.img = pygame.image.load('Assets/bill-35-15.png')

    def update_rect(self):
        """Updates the objects Rect using the current x and y values"""
        self.rect = pygame.Rect(self.x, self.y, 35, 15)

    def draw(self, s):
        """Draws the img attribute to screen on the current x and y values"""
        self.update_rect()
        s.blit(self.img, (self.x, self.y))

    def move(self, s):
        """Moves the projectile every frame. If the projectiles x value is greater than the width of the screen
        we return True to demonstrate that the projectile has indeed gone off screen."""
        self.x += self.vel
        self.draw(s)
        if self.x > 800:
            return True


# --------------------------------------- BULLET CLASS ----------------------------------------------- #


class Bullet:
    """This is the projectile shot by the SecretService agents"""
    def __init__(self, a):
        self.x = a.x - 6
        self.y = a.y + 33
        self.vel = 6
        self.rect = pygame.Rect(self.x, self.y, 10, 5)
        self.img = pygame.image.load('Assets/bullet.png').convert_alpha()

    def update_rect(self):
        """Updates the objects Rect using the current x and y values"""
        self.rect = pygame.Rect(self.x, self.y, 10, 5)

    def draw(self, s):
        """Draws the img attribute to screen on the current x and y values"""
        self.update_rect()
        s.blit(self.img, (self.x, self.y))

    def move(self, s):
        """Moves the projectile every frame. If the projectiles x value is less than the width of the screen
                we return True to demonstrate that the projectile has indeed gone off screen."""
        self.x -= self.vel
        self.draw(s)
        if self.x < 0:
            return True


# --------------------------------------- SECRET SERVICE CLASS -------------------------------------------- #


class SecretService:
    """One of the main enemy objects. These objects shoot Bullets() at set intervals"""
    def __init__(self):
        self.x = random.randint(900, 3000)
        self.y = random.randint(400, 500)
        # self.x = 300
        # self.y = 300
        self.rect = pygame.Rect(self.x, self.y, 50, 100)
        self.img = pygame.image.load('Assets/agent.png').convert_alpha()
        self.shoot_hold = True
        self.shots = []
        self.counter = 4000

    def update_rect(self):
        """Updates the objects Rect using the current x and y values"""
        self.rect = pygame.Rect(self.x, self.y, 50, 100)

    def draw(self, s):
        """Draws the img attribute to screen on the current x and y values"""
        self.update_rect()
        s.blit(self.img, (self.x, self.y))

    def shoot(self, b):
        """If the self.shoot_hold attribute is not True (attribute is set to true in main game loop
        when bullet is fired until the self.counter attribute reaches 0) then a Bullet() object is created
        in and appended to the list (argument b)"""
        if not self.shoot_hold:
            b.append(Bullet(self))

    def move(self, s):
        """x moves -2 for each game-loop to maintain pace with game background, so object appears static"""
        self.x -= 2
        self.draw(s)
        if self.x < -50:
            return True

# ------------------------------------------ HEART CLASS ------------------------------------------- #


class Heart:
    """This appears on screen and if a player collides with it, they are granted an additional life"""
    def __init__(self):
        self.x = random.randint(900, 8000)
        self.y = random.randint(400, 550)
        self.rect = pygame.Rect(self.x, self.y, 25, 25)
        self.img = pygame.image.load('Assets/heart.png').convert_alpha()

    def update_rect(self):
        """Updates the objects Rect using the current x and y values"""
        self.rect = pygame.Rect(self.x, self.y, 25, 25)

    def draw(self, s):
        """Draws the img attribute to screen on the current x and y values"""
        self.update_rect()
        s.blit(self.img, (self.x, self.y))

    def move(self, s):
        """x moves -2 for each game-loop to maintain pace with game background, so object appears static"""
        self.x -= 2
        self.draw(s)
        if self.x < -50:
            return True
