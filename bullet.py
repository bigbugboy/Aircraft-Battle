import pygame


class Bullet1(pygame.sprite.Sprite):
    def __init__(self, screen, ab_settings, position):
        super().__init__()
        self.ab_settings = ab_settings
        self.image = pygame.image.load('images/bullet1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.top = position
        self.scree = screen
        self.scree_rect = self.scree.get_rect()
        self.speed = 12
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top <= 0:
            self.active = False

    def reset(self, position):
        self.active = True
        self.rect.centerx, self.rect.top = position

    def blitme(self):
        self.scree.blit(self.image, self.rect)


class Bullet2(pygame.sprite.Sprite):
    def __init__(self, screen, ab_settings, position):
        super().__init__()
        self.ab_settings = ab_settings
        self.image = pygame.image.load('images/bullet2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.top = position
        self.scree = screen
        self.scree_rect = self.scree.get_rect()
        self.speed = 14
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top <= 0:
            self.active = False

    def reset(self, position):
        self.active = True
        self.rect.centerx, self.rect.top = position

    def blitme(self):
        self.scree.blit(self.image, self.rect)