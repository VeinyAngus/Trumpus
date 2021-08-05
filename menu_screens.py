import pygame


class Menus:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.main_menu_bg = pygame.image.load('Assets/mainmenu.png').convert_alpha()
        self.font = pygame.font.SysFont('arial', 50)
        self.running = True
        self.FPS = 60

    def main_menu(self):
        pygame.mixer.music.load('Assets/starspangled.mp3')
        pygame.mixer.music.play(-1)
        while self.running:
            self.clock.tick(self.FPS)
            self.screen.blit(self.main_menu_bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pass
            pygame.display.update()
