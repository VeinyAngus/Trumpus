"""
This game is still a work in progress. All code here is subject to change. I welcome any and all advice/feedback.
Please fork and do a PR if you have any changes you'd like to implement.
                                -VeinyAngus (MattMuelot)
"""

import pygame
from game_classes import Trump, Declaration, Moneybag, Bill, SecretService, Heart

# ------------- Initialize Pygame, create screen and clock objects --------------#

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# -------------- Load image and audio files ------------------#

bg = pygame.image.load('Assets/background.png').convert_alpha()
bg2 = pygame.image.load('Assets/background2.png').convert_alpha()
dollarbill = pygame.image.load('Assets/dollarbill-75-35.png').convert_alpha()
heart = pygame.image.load('Assets/heart.png').convert_alpha()
mainmenu = pygame.image.load('Assets/mainmenu.png').convert_alpha()
lose = pygame.image.load('Assets/youlose.png').convert_alpha()
level2bg = pygame.image.load('Assets/level2bg.png').convert_alpha()
level3bg = pygame.image.load('Assets/level3bg.png').convert_alpha()
level3bg2 = pygame.image.load('Assets/level3bg2.png').convert_alpha()
agent_img = pygame.image.load('Assets/agent.png').convert_alpha()
pygame.mixer.set_num_channels(16)  # Set number of audio channels to 16 to avoid sound loss
pygame.mixer.music.load('Assets/level1.mp3')
moneycollect = pygame.mixer.Sound('Assets/moneycollect.ogg')
burn = pygame.mixer.Sound('Assets/burn.ogg')
wrong = pygame.mixer.Sound('Assets/wrong.ogg')
throw = pygame.mixer.Sound('Assets/throw.ogg')
shot = pygame.mixer.Sound('Assets/gunshot.ogg')
okay = pygame.mixer.Sound('Assets/okay.ogg')
scream = pygame.mixer.Sound('Assets/scream.ogg')
jump = pygame.mixer.Sound('Assets/jump.ogg')
collect_heart = pygame.mixer.Sound('Assets/collect_heart.ogg')
moneyfont = pygame.font.SysFont('comicsans', 50)  # Master font created

# -------------------------------------- MAIN MENU SCREEN ---------------------------------------- #


def menu():
    """Main menu function that is run when the game is started"""
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


# ----------------------------------------- GAME LOST SCREEN ---------------------------------------- #


def lose_screen():
    """If the game is lost, this screen runs and then returns you to the main menu screen"""
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Assets/lose.mp3')
    pygame.mixer.music.play(-1)
    running = True
    while running:
        clock.tick(60)
        screen.blit(lose, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 'restart'
        pygame.display.update()


# ------------------------------------- LEVEL WIN SCREENS ------------------------------------ #


def level_one_win():
    """This function runs if you have completed level one"""
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Assets/yankeedoodle.mp3')
    pygame.mixer.music.play(-1)
    i = 0
    running = True
    while running:
        clock.tick(60)  # Set FPS To 60
        screen.blit(bg, (i, 0))
        screen.blit(bg, (3200 + i, 0))
        win_label = moneyfont.render(f'Level One Complete', True, (255, 255, 255))
        win_label2 = moneyfont.render(f'Press Space To Continue', True, (255, 255, 255))
        screen.blit(win_label, (250, 200))
        screen.blit(win_label2, (195, 300))
        i -= 2
        if i == -3200:
            screen.blit(bg, (3200 + i, 0))
            i = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 'next'
        pygame.display.update()


def level_two_win():
    """This function runs if you have completed level one"""
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Assets/yankeedoodle.mp3')
    pygame.mixer.music.play(-1)
    i = 0
    running = True
    while running:
        clock.tick(60)  # Set FPS To 60
        screen.blit(level2bg, (i, 0))
        screen.blit(level2bg, (3200 + i, 0))
        win_label = moneyfont.render(f'Level Two Complete', True, (255, 255, 255))
        win_label2 = moneyfont.render(f'Press Space To Continue', True, (255, 255, 255))
        screen.blit(win_label, (250, 200))
        screen.blit(win_label2, (195, 300))
        i -= 2
        if i == -3200:
            screen.blit(bg, (3200 + i, 0))
            i = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 'next'
        pygame.display.update()


# -------------------------------------------- LEVEL ONE -------------------------------------------- #


def level_one():
    pygame.mixer.music.load('Assets/level1.mp3')
    pygame.mixer.music.play(-1)
    trump = Trump()
    decs = [Declaration() for _ in range(10)]
    bags = [Moneybag() for _ in range(8)]
    obj_timer = 0
    i = 0
    running = True
    while running:
        obj_timer += 1
        clock.tick(60)  # Set FPS To 60
        screen.blit(bg, (i, 0))
        screen.blit(bg, (3200 + i, 0))
        screen.blit(dollarbill, (10, 10))
        screen.blit(heart, (750, 10))
        money_label = moneyfont.render(f'${trump.money}', True, (0, 255, 0))
        heart_label = moneyfont.render(f'{trump.lives}', True, (255, 255, 255))
        screen.blit(money_label, (95, 12))
        screen.blit(heart_label, (715, 10))
        if obj_timer < 400:
            obj_label = moneyfont.render(f'Collect $30 To Advance', True, (0, 255, 0))
            screen.blit(obj_label, (225, 12))
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
                        jump.play()
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
                    trump.lives -= 1
        for b in bags[:]:
            off_screen = b.move(screen)
            if b.rect.colliderect(trump.rect):
                bags.remove(b)
                moneycollect.play()
                trump.money += 3
                if trump.money >= 30:
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
        if trump.lives <= 0:
            return 'lost'
        trump.draw(screen)
        trump.move(screen)
        pygame.display.update()


# ------------------------------------------ LEVEL TWO -------------------------------------------- #


def level_two():
    pygame.mixer.music.load('Assets/level2.mp3')
    pygame.mixer.music.play(-1)
    trump = Trump()
    decs = [Declaration() for _ in range(11)]
    bags = [Moneybag() for _ in range(9)]
    agents = [SecretService() for _ in range(3)]
    hearts = [Heart() for _ in range(3)]
    bullets = []
    obj_timer = 0
    i = 0
    running = True
    while running:
        obj_timer += 1
        eta = clock.tick(60)  # Set FPS To 60
        screen.blit(level2bg, (i, 0))
        screen.blit(level2bg, (3200 + i, 0))
        screen.blit(dollarbill, (10, 10))
        screen.blit(heart, (750, 10))
        money_label = moneyfont.render(f'${trump.money}', True, (0, 255, 0))
        heart_label = moneyfont.render(f'{trump.lives}', True, (255, 255, 255))
        screen.blit(money_label, (95, 12))
        screen.blit(heart_label, (715, 10))
        if obj_timer < 400:
            obj_label = moneyfont.render(f'Collect $60 To Advance', True, (0, 255, 0))
            screen.blit(obj_label, (225, 12))
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
                        jump.play()
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
                    trump.lives -= 1
        for a in agents[:]:
            off_screen = a.move(screen)
            a.counter -= eta
            if a.counter <= 0:
                a.shoot_hold = False
                a.shoot(bullets)
                a.counter += 4000
                a.shoot_hold = True
            if off_screen:
                agents.remove(a)
            for m in trump.money_shot[:]:
                if m.rect.colliderect(a.rect):
                    agents.remove(a)
                    scream.play()
                    trump.money_shot.remove(m)
                else:
                    pass
        for b in bags[:]:
            off_screen = b.move(screen)
            if b.rect.colliderect(trump.rect):
                bags.remove(b)
                moneycollect.play()
                trump.money += 4
                if trump.money >= 60:
                    return 'win'
            if off_screen:
                bags.remove(b)
        for m in trump.money_shot[:]:
            off_screen = m.move(screen)
            if off_screen:
                trump.money_shot.remove(m)
        for b in bullets[:]:
            b.move(screen)
            if b.rect.colliderect(trump.rect):
                bullets.remove(b)
                okay.play()
                trump.lives -= 1
        for h in hearts[:]:
            h.move(screen)
            if h.rect.colliderect(trump.rect):
                trump.lives += 1
                hearts.remove(h)
                collect_heart.play()
        if len(decs) <= 0:
            trump.wave += 2
            decs = [Declaration() for _ in range(10 + trump.wave)]
        if len(bags) <= 0:
            bags = [Moneybag() for _ in range(9)]
        if len(agents) <= 0:
            agents = [SecretService() for _ in range(3)]
        if trump.jumping:
            trump.jump(screen)
        trump.draw(screen)
        trump.move(screen)
        if trump.lives <= 0:
            return 'lost'
        pygame.display.update()


# ---------------------------------------- LEVEL THREE ------------------------------------------- #


def level_three():
    pygame.mixer.music.load('Assets/level3.mp3')
    pygame.mixer.music.play(-1)
    trump = Trump()
    decs = [Declaration() for _ in range(5)]
    bags = [Moneybag() for _ in range(11)]
    agents = [SecretService() for _ in range(5)]
    hearts = [Heart() for _ in range(5)]
    bullets = []
    obj_timer = 0
    i = 0
    running = True
    while running:
        obj_timer += 1
        eta = clock.tick(60)  # Set FPS To 60
        screen.blit(level3bg2, (0, 0))
        screen.blit(level3bg, (i, 0))
        screen.blit(level3bg, (3200 + i, 0))
        screen.blit(dollarbill, (10, 10))
        screen.blit(heart, (750, 10))
        money_label = moneyfont.render(f'${trump.money}', True, (0, 255, 0))
        heart_label = moneyfont.render(f'{trump.lives}', True, (255, 0, 0))
        agents_label = moneyfont.render(f'Agents Left: {trump.agents_left}', True, (255, 255, 255))
        screen.blit(money_label, (95, 12))
        screen.blit(heart_label, (715, 10))
        screen.blit(agents_label, (10, 550))
        if obj_timer < 400:
            obj_label = moneyfont.render(f'Kill All Agents', True, (0, 255, 50))
            screen.blit(obj_label, (275, 12))
        i -= 2
        if i == -3200:
            screen.blit(level3bg, (3200 + i, 0))
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
                        jump.play()
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
                    trump.lives -= 1
        for a in agents[:]:
            off_screen = a.move(screen)
            a.counter -= eta
            if a.counter <= 0:
                a.shoot_hold = False
                a.shoot(bullets)
                a.counter += 4000
                a.shoot_hold = True
            if off_screen:
                agents.remove(a)
            for m in trump.money_shot[:]:
                if m.rect.colliderect(a.rect):
                    agents.remove(a)
                    scream.play()
                    trump.money_shot.remove(m)
                else:
                    pass
        for b in bags[:]:
            off_screen = b.move(screen)
            if b.rect.colliderect(trump.rect):
                bags.remove(b)
                moneycollect.play()
                trump.money += 4
            if off_screen:
                bags.remove(b)
        for m in trump.money_shot[:]:
            off_screen = m.move(screen)
            if off_screen:
                trump.money_shot.remove(m)
        for b in bullets[:]:
            b.move(screen)
            if b.rect.colliderect(trump.rect):
                bullets.remove(b)
                okay.play()
                trump.lives -= 1
        for h in hearts[:]:
            h.move(screen)
            if h.rect.colliderect(trump.rect):
                trump.lives += 1
                hearts.remove(h)
                collect_heart.play()
        if len(decs) <= 0:
            trump.wave += 2
            decs = [Declaration() for _ in range(5 + trump.wave)]
        if len(bags) <= 0:
            bags = [Moneybag() for _ in range(11)]
        if len(agents) <= 0:
            agents = [SecretService() for _ in range(5)]
        if trump.jumping:
            trump.jump(screen)
        trump.draw(screen)
        trump.move(screen)
        if trump.lives <= 0:
            return 'lost'
        pygame.display.update()


# -------------------------------------------- MAIN GAME LOOP --------------------------------------------- #

"""This code is kind-of a mess right now. The nested if/else blocks aren't exactly ideal, but for now it runs"""


while True:
    result = menu()
    if result == 'play':
        level_one_result = level_one()
        if level_one_result == 'lost':
            lose_screen_result = lose_screen()
            if lose_screen_result == 'restart':
                continue
            if lose_screen_result == 'quit':
                break
        if level_one_result == 'win':
            win_result = level_one_win()
            if win_result == 'next':
                level_two_result = level_two()
                if level_two_result == 'lost':
                    lose_screen_result = lose_screen()
                    if lose_screen_result == 'restart':
                        continue
                    if lose_screen_result == 'quit':
                        break
                if level_two_result == 'win':
                    win_result = level_two_win()
                    if win_result == 'next':
                        level_three_result = level_three()
                if level_two_result == 'quit':
                    break
            if win_result == 'quit':
                break
        if level_one_result == 'quit':
            break
    else:
        break


pygame.quit()
