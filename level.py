from game_classes import Trump, Declaration, Moneybag, Bill, SecretService, Heart
import pygame
import json


class Levels:
    """Game level class. Pass as an argument the level number and the level will play out according to
    the level specified. """
    def __init__(self, screen, clock, fps):
        with open('config_files/level_settings.json', 'r') as f:
            self.data = json.load(f)
        self.screen = screen
        self.clock = clock
        self.FPS = fps
        self.trump = Trump()
        self.decs = []
        self.bags = []
        self.hearts = []
        self.agents = []
        self.bullets = []
        # if self.lev == 2:
        #     self.bg = pygame.image.load('Assets/level2bg.png').convert_alpha()
        #     self.decs = [Declaration() for _ in range(11)]
        #     self.bags = [Moneybag() for _ in range(9)]
        #     self.agents = [SecretService() for _ in range(3)]
        #     self.hearts = [Heart() for _ in range(3)]
        #     self.bullets = []
        # if self.lev == 3:
        #     self.bg = pygame.image.load('Assets/level3bg.png').convert_alpha()
        #     self.bg2 = pygame.image.load('Assets/level3bg2.png').convert_alpha()
        #     self.decs = [Declaration() for _ in range(5)]
        #     self.bags = [Moneybag() for _ in range(11)]
        #     self.agents = [SecretService() for _ in range(5)]
        #     self.hearts = [Heart() for _ in range(5)]
        #     self.bullets = []

        # ------------------ LOAD IN GLOBAL AUDIO FILES ---------------- #

        pygame.mixer.set_num_channels(16)
        self.moneycollect = pygame.mixer.Sound('Assets/moneycollect.ogg')
        self.burn = pygame.mixer.Sound('Assets/burn.ogg')
        self.wrong = pygame.mixer.Sound('Assets/wrong.ogg')
        self.throw = pygame.mixer.Sound('Assets/throw.ogg')
        self.shot = pygame.mixer.Sound('Assets/gunshot.ogg')
        self.okay = pygame.mixer.Sound('Assets/okay.ogg')
        self.scream = pygame.mixer.Sound('Assets/scream.ogg')
        self.jump = pygame.mixer.Sound('Assets/jump.ogg')
        self.collect_heart = pygame.mixer.Sound('Assets/collect_heart.ogg')

        # ------------------ LOAD IN GLOBAL IMAGES ----------------- #

        self.heart = pygame.image.load('Assets/heart.png').convert_alpha()
        self.bill = pygame.image.load('Assets/dollarbill-75-35.png').convert_alpha()
        self.bg1 = pygame.image.load('Assets/level1bg.png').convert_alpha()
        self.bg2 = pygame.image.load('Assets/level2bg.png').convert_alpha()
        self.bg3a = pygame.image.load('Assets/level3bg.png').convert_alpha()
        self.bg3b = pygame.image.load('Assets/level3bg2.png').convert_alpha()

        # ------------------ LOAD IN GLOBAL FONTS ----------------- #

        self.main_font = pygame.font.SysFont('comicsans', 50)

        # ------------------- RENAME ------------------- #

        self.obj_timer = 0
        self.i = 0
        self.running = True

    def level_one(self):
        """Level One method"""
        self.decs = [Declaration() for _ in range(self.data['level_one']['declarations_per_wave'])]
        self.bags = [Moneybag() for _ in range(self.data['level_one']['money_bags_per_wave'])]
        pygame.mixer.music.load('Assets/level1.mp3')
        pygame.mixer.music.play(-1)
        while self.running:
            self.obj_timer += 1
            self.clock.tick(60)  # Set FPS To 60
            self.screen.blit(self.bg1, (self.i, 0))
            self.screen.blit(self.bg1, (3200 + self.i, 0))
            self.screen.blit(self.bill, (10, 10))
            self.screen.blit(self.heart, (750, 10))
            money_label = self.main_font.render(f'${self.trump.money}', True, (0, 255, 0))
            heart_label = self.main_font.render(f'{self.trump.lives}', True, (255, 255, 255))
            self.screen.blit(money_label, (95, 12))
            self.screen.blit(heart_label, (715, 10))
            if self.obj_timer < 400:
                obj_label = self.main_font.render(f'Collect $30 To Advance', True, (0, 255, 0))
                self.screen.blit(obj_label, (225, 12))
            self.i -= 2
            if self.i == -3200:
                self.screen.blit(self.bg1, (3200 + self.i, 0))
                self.i = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    return 'quit'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:
                        if self.trump.jumping:
                            pass
                        else:
                            self.trump.jumping = True
                            self.jump.play()
                    if event.key == pygame.K_SPACE:
                        if self.trump.money > 0:
                            self.trump.money_shot.append(Bill(self.trump))
                            self.throw.play()
                            self.trump.money -= 1
            for d in self.decs[:]:
                off_screen = d.move(self.screen)
                burn_result = d.draw(self.screen)
                if burn_result:
                    self.decs.remove(d)
                if off_screen:
                    self.decs.remove(d)
                for m in self.trump.money_shot[:]:
                    if m.rect.colliderect(d.rect):
                        if not d.timer:
                            d.timer = True
                            self.burn.play()
                            self.trump.money_shot.remove(m)
                        else:
                            pass
                if d.rect.colliderect(self.trump.rect):
                    if d.timer:
                        pass
                    else:
                        self.decs.remove(d)
                        self.wrong.play()
                        self.trump.lives -= 1
            for b in self.bags[:]:
                off_screen = b.move(self.screen)
                if b.rect.colliderect(self.trump.rect):
                    self.bags.remove(b)
                    self.moneycollect.play()
                    self.trump.money += 3
                    if self.trump.money >= 30:
                        pygame.mixer.music.stop()
                        return 'win'
                if off_screen:
                    self.bags.remove(b)
            for m in self.trump.money_shot[:]:
                off_screen = m.move(self.screen)
                if off_screen:
                    self.trump.money_shot.remove(m)
            if len(self.decs) <= 0:
                self.trump.wave += 2
                self.decs = [Declaration() for _ in range(self.data['level_one']['declarations_per_wave'])]
            if len(self.bags) <= 0:
                self.bags = [Moneybag() for _ in range(self.data['level_one']['money_bags_per_wave'])]
            if self.trump.jumping:
                self.trump.jump(self.screen)
            if self.trump.lives <= 0:
                pygame.mixer.music.stop()
                return 'lost'
            self.trump.draw(self.screen)
            self.trump.move(self.screen)
            pygame.display.update()

    def level_two(self):
        self.trump.reset()
        self.decs = [Declaration() for _ in range(self.data['level_two']['declarations_per_wave'])]
        self.bags = [Moneybag() for _ in range(self.data['level_two']['money_bags_per_wave'])]
        self.agents = [SecretService() for _ in range(self.data['level_two']['secret_service_per_wave'])]
        pygame.mixer.music.load('Assets/level2.mp3')
        pygame.mixer.music.play(-1)
        while self.running:
            self.obj_timer += 1
            eta = self.clock.tick(60)  # Set FPS To 60
            self.screen.blit(self.bg2, (self.i, 0))
            self.screen.blit(self.bg2, (3200 + self.i, 0))
            self.screen.blit(self.bill, (10, 10))
            self.screen.blit(self.heart, (750, 10))
            money_label = self.main_font.render(f'${self.trump.money}', True, (0, 255, 0))
            heart_label = self.main_font.render(f'{self.trump.lives}', True, (255, 255, 255))
            self.screen.blit(money_label, (95, 12))
            self.screen.blit(heart_label, (715, 10))
            if self.obj_timer < 400:
                obj_label = self.main_font.render(f'Collect $30 To Advance', True, (0, 255, 0))
                self.screen.blit(obj_label, (225, 12))
            self.i -= 2
            if self.i == -3200:
                self.screen.blit(self.bg1, (3200 + self.i, 0))
                self.i = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    return 'quit'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:
                        if self.trump.jumping:
                            pass
                        else:
                            self.trump.jumping = True
                            self.jump.play()
                    if event.key == pygame.K_SPACE:
                        if self.trump.money > 0:
                            self.trump.money_shot.append(Bill(self.trump))
                            self.throw.play()
                            self.trump.money -= 1
            for d in self.decs[:]:
                off_screen = d.move(self.screen)
                burn_result = d.draw(self.screen)
                if burn_result:
                    self.decs.remove(d)
                if off_screen:
                    self.decs.remove(d)
                for m in self.trump.money_shot[:]:
                    if m.rect.colliderect(d.rect):
                        if not d.timer:
                            d.timer = True
                            self.burn.play()
                            self.trump.money_shot.remove(m)
                        else:
                            pass
                if d.rect.colliderect(self.trump.rect):
                    if d.timer:
                        pass
                    else:
                        self.decs.remove(d)
                        self.wrong.play()
                        self.trump.lives -= 1
            for b in self.bags[:]:
                off_screen = b.move(self.screen)
                if b.rect.colliderect(self.trump.rect):
                    self.bags.remove(b)
                    self.moneycollect.play()
                    self.trump.money += 3
                    if self.trump.money >= 30:
                        pygame.mixer.music.stop()
                        return 'win'
                if off_screen:
                    self.bags.remove(b)
            for a in self.agents[:]:
                off_screen = a.move(self.screen)
                a.counter -= eta
                if a.counter <= 0:
                    a.shoot_hold = False
                    a.shoot(self.bullets)
                    a.counter += 4000
                    a.shoot_hold = True
                    self.shot.play()
                if off_screen:
                    self.agents.remove(a)
                for m in self.trump.money_shot[:]:
                    if m.rect.colliderect(a.rect):
                        self.agents.remove(a)
                        self.scream.play()
                        self.trump.money_shot.remove(m)
                    else:
                        pass
            for b in self.bullets[:]:
                b.move(self.screen)
                if b.rect.colliderect(self.trump.rect):
                    self.bullets.remove(b)
                    self.okay.play()
                    self.trump.lives -= 1
            for m in self.trump.money_shot[:]:
                off_screen = m.move(self.screen)
                if off_screen:
                    self.trump.money_shot.remove(m)
            if len(self.decs) <= 0:
                self.trump.wave += 2
                self.decs = [Declaration() for _ in range(self.data['level_two']['declarations_per_wave'])]
            if len(self.bags) <= 0:
                self.bags = [Moneybag() for _ in range(self.data['level_two']['money_bags_per_wave'])]
            if len(self.agents) <= 0:
                self.agents = [SecretService() for _ in range(self.data['level_two']['secret_service_per_wave'])]
            if self.trump.jumping:
                self.trump.jump(self.screen)
            if self.trump.lives <= 0:
                pygame.mixer.music.stop()
                return 'lost'
            self.trump.draw(self.screen)
            self.trump.move(self.screen)
            pygame.display.update()

    def level_three(self):
        self.trump.reset()
        self.decs = [Declaration() for _ in range(self.data['level_two']['declarations_per_wave'])]
        self.bags = [Moneybag() for _ in range(self.data['level_two']['money_bags_per_wave'])]
        self.agents = [SecretService() for _ in range(self.data['level_two']['secret_service_per_wave'])]
        pygame.mixer.music.load('Assets/level3.mp3')
        pygame.mixer.music.play(-1)
        while self.running:
            self.obj_timer += 1
            eta = self.clock.tick(60)  # Set FPS To 60
            self.screen.blit(self.bg3a, (self.i, 0))
            self.screen.blit(self.bg3a, (3200 + self.i, 0))
            self.screen.blit(self.bill, (10, 10))
            self.screen.blit(self.heart, (750, 10))
            money_label = self.main_font.render(f'${self.trump.money}', True, (0, 255, 0))
            heart_label = self.main_font.render(f'{self.trump.lives}', True, (255, 255, 255))
            self.screen.blit(money_label, (95, 12))
            self.screen.blit(heart_label, (715, 10))
            if self.obj_timer < 400:
                obj_label = self.main_font.render(f'Collect $30 To Advance', True, (0, 255, 0))
                self.screen.blit(obj_label, (225, 12))
            self.i -= 2
            if self.i == -3200:
                self.screen.blit(self.bg1, (3200 + self.i, 0))
                self.i = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    return 'quit'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:
                        if self.trump.jumping:
                            pass
                        else:
                            self.trump.jumping = True
                            self.jump.play()
                    if event.key == pygame.K_SPACE:
                        if self.trump.money > 0:
                            self.trump.money_shot.append(Bill(self.trump))
                            self.throw.play()
                            self.trump.money -= 1
            for d in self.decs[:]:
                off_screen = d.move(self.screen)
                burn_result = d.draw(self.screen)
                if burn_result:
                    self.decs.remove(d)
                if off_screen:
                    self.decs.remove(d)
                for m in self.trump.money_shot[:]:
                    if m.rect.colliderect(d.rect):
                        if not d.timer:
                            d.timer = True
                            self.burn.play()
                            self.trump.money_shot.remove(m)
                        else:
                            pass
                if d.rect.colliderect(self.trump.rect):
                    if d.timer:
                        pass
                    else:
                        self.decs.remove(d)
                        self.wrong.play()
                        self.trump.lives -= 1
            for b in self.bags[:]:
                off_screen = b.move(self.screen)
                if b.rect.colliderect(self.trump.rect):
                    self.bags.remove(b)
                    self.moneycollect.play()
                    self.trump.money += 3
                    if self.trump.money >= 30:
                        pygame.mixer.music.stop()
                        return 'win'
                if off_screen:
                    self.bags.remove(b)
            for a in self.agents[:]:
                off_screen = a.move(self.screen)
                a.counter -= eta
                if a.counter <= 0:
                    a.shoot_hold = False
                    a.shoot(self.bullets)
                    a.counter += 4000
                    a.shoot_hold = True
                    self.shot.play()
                if off_screen:
                    self.agents.remove(a)
                for m in self.trump.money_shot[:]:
                    if m.rect.colliderect(a.rect):
                        self.agents.remove(a)
                        self.scream.play()
                        self.trump.money_shot.remove(m)
                    else:
                        pass
            for b in self.bullets[:]:
                b.move(self.screen)
                if b.rect.colliderect(self.trump.rect):
                    self.bullets.remove(b)
                    self.okay.play()
                    self.trump.lives -= 1
            for m in self.trump.money_shot[:]:
                off_screen = m.move(self.screen)
                if off_screen:
                    self.trump.money_shot.remove(m)
            if len(self.decs) <= 0:
                self.trump.wave += 2
                self.decs = [Declaration() for _ in range(self.data['level_two']['declarations_per_wave'])]
            if len(self.bags) <= 0:
                self.bags = [Moneybag() for _ in range(self.data['level_two']['money_bags_per_wave'])]
            if len(self.agents) <= 0:
                self.agents = [SecretService() for _ in range(self.data['level_two']['secret_service_per_wave'])]
            if self.trump.jumping:
                self.trump.jump(self.screen)
            if self.trump.lives <= 0:
                pygame.mixer.music.stop()
                return 'lost'
            self.trump.draw(self.screen)
            self.trump.move(self.screen)
            pygame.display.update()
