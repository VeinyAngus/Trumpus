import pygame
from game_classes import Trump, Declaration, Moneybag, Bill
import random

# Initialize Pygame, create screen and clock objects

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load background and audio files

bg = pygame.image.load('Assets/background.png').convert_alpha()
bg2 = pygame.image.load('Assets/background2.png').convert_alpha()
dollarbill = pygame.image.load('Assets/dollarbill-75-35.png').convert_alpha()
mainmenu = pygame.image.load('Assets/mainmenu.png').convert_alpha()
lose = pygame.image.load('Assets/youlose.png').convert_alpha()
level2bg = pygame.image.load('Assets/level2bg.png').convert_alpha()
pygame.mixer.set_num_channels(16)
pygame.mixer.music.load('Assets/level1.mp3')
moneycollect = pygame.mixer.Sound('Assets/moneycollect.ogg')
burn = pygame.mixer.Sound('Assets/burn.ogg')
wrong = pygame.mixer.Sound('Assets/wrong.ogg')
throw = pygame.mixer.Sound('Assets/throw.ogg')
moneyfont = pygame.font.SysFont('comicsans', 50)


def menu():
    i2 = 0
    pygame.mixer.music.load('Assets/starspangled.mp3')
    pygame.mixer.music.play(-1)
    running = True
    while running:
        clock.tick(60)
        screen.blit(mainmenu, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 'play'
        pygame.display.update()


def level_one():
    pygame.mixer.music.load('Assets/level1.mp3')
    pygame.mixer.music.play(-1)
    trump = Trump()
    decs = [Declaration() for _ in range(10)]
    bags = [Moneybag() for _ in range(8)]
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
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    if trump.jumping:
                        pass
                    else:
                        trump.jumping = True
                if event.key == pygame.K_SPACE:
                    if trump.money > 0:
                        trump.money_shot.append(Bill(trump))
                        throw.play()
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
                    wrong.play()
                    trump.money -= 3
                    if trump.money < 0:
                        screen.blit(lose, (0, 0))
                        pygame.display.update()
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('Assets/lose.mp3')
                        pygame.mixer.music.play(-1)
                        pygame.time.delay(4000)
                        return 'lost'
        for b in bags[:]:
            off_screen = b.move(screen)
            if b.rect.colliderect(trump.rect):
                bags.remove(b)
                moneycollect.play()
                trump.money += 3
                if trump.money >= 10:
                    return 'win'
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
            bags = [Moneybag() for _ in range(8)]
        if trump.jumping:
            trump.jump(screen)
        trump.draw(screen)
        trump.move(screen)
        pygame.display.update()


def level_two():
    pygame.mixer.music.load('Assets/level2.mp3')
    pygame.mixer.music.play(-1)
    trump = Trump()
    decs = [Declaration() for _ in range(10)]
    bags = [Moneybag() for _ in range(8)]
    i = 0
    running = True
    while running:
        clock.tick(60)  # Set FPS To 60
        screen.blit(level2bg, (i, 0))
        screen.blit(level2bg, (3200 + i, 0))
        screen.blit(dollarbill, (10, 10))
        money_label = moneyfont.render(f'{trump.money}', True, (0, 255, 0))
        screen.blit(money_label, (95, 12))
        i -= 2
        if i == -3200:
            screen.blit(level2bg, (3200 + i, 0))
            i = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    if trump.jumping:
                        pass
                    else:
                        trump.jumping = True
                if event.key == pygame.K_SPACE:
                    if trump.money > 0:
                        trump.money_shot.append(Bill(trump))
                        throw.play()
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
                    wrong.play()
                    trump.money -= 3
                    if trump.money < 0:
                        screen.blit(lose, (0, 0))
                        pygame.display.update()
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('Assets/lose.mp3')
                        pygame.mixer.music.play(-1)
                        pygame.time.delay(4000)
                        return 'lost'
        for b in bags[:]:
            off_screen = b.move(screen)
            if b.rect.colliderect(trump.rect):
                bags.remove(b)
                moneycollect.play()
                trump.money += 3
                if trump.money >= 75:
                    return 'win'
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
            bags = [Moneybag() for _ in range(8)]
        if trump.jumping:
            trump.jump(screen)
        trump.draw(screen)
        trump.move(screen)
        pygame.display.update()


while True:
    result = menu()
    if result == 'play':
        level_one_result = level_one()
        if level_one_result == 'lost':
            continue
        if level_one_result == 'win':
            level_two_result = level_two()
            if level_two_result == 'lost':
                continue
            if level_two_result == 'win':
                continue
            if level_two_result == 'quit':
                break
        if level_one_result == 'quit':
            break
    else:
        break
