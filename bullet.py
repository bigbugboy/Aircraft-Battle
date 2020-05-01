import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, ab_settings):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen
        self.ab_settings = ab_settings
        self.speed = None
        self.active = True
        self.image = pygame.image.load('images/bullet1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top <= 0:
            self.active = False

    def reset(self, position):
        """
        绘制子弹时会启动reset,传一个时时位置参数
        :param position:
        :return:
        """
        self.active = True
        self.rect.centerx, self.rect.top = position

    def blitme(self):
        if self.active: # 子弹没有穿透功能
            self.screen.blit(self.image, self.rect)


class Bullet1(Bullet):
    def __init__(self, screen, ab_settings):
        super().__init__(screen, ab_settings)
        self.ab_settings = ab_settings
        self.image = pygame.image.load('images/bullet1.png').convert_alpha()
        self.speed = 12


class Bullet2(Bullet):
    def __init__(self, screen, ab_settings):
        super().__init__(screen, ab_settings)
        self.image = pygame.image.load('images/bullet2.png').convert_alpha()
        self.speed = 14