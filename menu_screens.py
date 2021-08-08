import pygame


class Menus:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.main_menu_bg = pygame.image.load('Assets/mainmenu.png').convert_alpha()
        self.settings_bg = pygame.image.load('Assets/settings.png').convert_alpha()
        self.click_sound = pygame.mixer.Sound('Assets/click.ogg')
        self.font = pygame.font.SysFont('arial', 50)
        self.start_rect = pygame.Rect(58, 485, 210, 78)
        self.settings_rect = pygame.Rect(523, 485, 210, 78)
        self.menu_rect = pygame.Rect(300, 485, 190, 66)
        self.mouse_rect = pygame.Rect(50, 50, 5, 5)
        self.running = True
        self.FPS = 60
        pygame.mixer.music.load('Assets/starspangled.mp3')
        pygame.mixer.music.play(-1)

    def main_menu(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.screen.blit(self.main_menu_bg, (0, 0))
            mouse = pygame.mouse.get_pos()
            self.mouse_rect.x, self.mouse_rect.y = mouse[0], mouse[1]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
                if event.type == pygame.MOUSEBUTTONUP:
                    self.click_sound.play()
                    if self.mouse_rect.colliderect(self.start_rect):
                        print('start click')
                        pygame.draw.rect(self.screen, (255, 255, 255), self.start_rect, 2)
                        return 'start'
                    if self.mouse_rect.colliderect(self.settings_rect):
                        pygame.draw.rect(self.screen, (255, 255, 255), self.settings_rect, 2)
                        return 'settings'
            # pygame.draw.rect(self.screen, (255, 0, 0), self.mouse_rect)
            pygame.display.update()

    def settings(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.screen.blit(self.settings_bg, (0, 0))
            mouse = pygame.mouse.get_pos()
            self.mouse_rect.x, self.mouse_rect.y = mouse[0], mouse[1]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
                if event.type == pygame.MOUSEBUTTONUP:
                    self.click_sound.play()
                    if self.mouse_rect.colliderect(self.menu_rect):
                        pygame.draw.rect(self.screen, (255, 255, 255), self.menu_rect, 2)
                        return 'menu'
            pygame.draw.rect(self.screen, (255, 0, 0), self.menu_rect, 2)
            pygame.display.update()
