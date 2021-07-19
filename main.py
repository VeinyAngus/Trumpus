import pygame
from game_classes import Trump, Declaration, Moneybag, Bill
import random

# Initialize Pygame, create screen and clock objects

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load background and audio files

bg = pygame.image.load('Assets/background.png').convert_alpha()
dollarbill = pygame.image.load('Assets/dollarbill-75-35.png').convert_alpha()
pygame.mixer.set_num_channels(16)
pygame.mixer.music.load('Assets/maintheme.mp3')
pygame.mixer.music.play(-1)
moneycollect = pygame.mixer.Sound('Assets/moneycollect.ogg')
burn = pygame.mixer.Sound('Assets/burn.ogg')
moneyfont = pygame.font.SysFont('comicsans', 50)

# Create game objects

trump = Trump()
decs = [Declaration() for _ in range(10)]
bags = [Moneybag() for _ in range(5)]

# Main Game Loop

i = 0
running = True
while running:
    clock.tick(60)  # Set FPS To 60
    screen.blit(bg, (i, 0))
    screen.blit(bg, (3200 + i, 0))
    screen.blit(dollarbill, (10, 10))
    money_label = moneyfont.render(f'{trump.money}', True, (0, 255, 0))
    screen.blit(money_label, (95, 12))
    i -= 2
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
            if event.key == pygame.K_SPACE:
                if trump.money > 0:
                    trump.money_shot.append(Bill(trump))
                    trump.money -= 1
    for d in decs[:]:
        off_screen = d.move(screen)
        burn_result = d.draw(screen)
        if burn_result:
            decs.remove(d)
        if off_screen:
            decs.remove(d)
        for m in trump.money_shot[:]:
            if m.rect.colliderect(d.rect):
                if not d.timer:
                    d.timer = True
                    burn.play()
                    trump.money_shot.remove(m)
                else:
                    pass
        if d.rect.colliderect(trump.rect):
            if d.timer:
                pass
            else:
                decs.remove(d)
                trump.money -= 3
    for b in bags[:]:
        off_screen = b.move(screen)
        if b.rect.colliderect(trump.rect):
            bags.remove(b)
            moneycollect.play()
            trump.money += 3
        if off_screen:
            bags.remove(b)
    for m in trump.money_shot[:]:
        off_screen = m.move(screen)
        if off_screen:
            trump.money_shot.remove(m)
    if len(decs) <= 0:
        trump.wave += 2
        decs = [Declaration() for _ in range(10 + trump.wave)]
    if len(bags) <= 0:
        bags = [Moneybag() for _ in range(5)]
    if trump.jumping:
        trump.jump(screen)
    trump.draw(screen)
    trump.move(screen)
    pygame.display.update()
