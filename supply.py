import pygame
from random import randint


class Supply(pygame.sprite.Sprite):
    def __init__(self, ab_settings, screen):
        super().__init__()
        self.ab_settings = ab_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.active = False
        self.speed = 5
        self.image = pygame.image.load('images/bomb_supply.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = randint(0, self.screen_rect.width - self.rect.width)
        self.rect.top = - self.screen_rect.height // 2
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.active:
            self.rect.top += self.speed
            if self.rect.top >= self.screen_rect.height:
                self.active = False

    def reset(self):
        self.active = True
        self.rect.left = randint(0, self.screen_rect.width - self.rect.width)
        self.rect.top = - self.screen_rect.height // 2

    def blitme(self):
        if self.active:
            self.screen.blit(self.image, self.rect)


class BombSupply(Supply):
    def __init__(self, ab_settings, screen):
        super().__init__(ab_settings, screen)
        self.name = 'bomb_supply'
        self.image = pygame.image.load('images/bomb_supply.png').convert_alpha()


class BulletSupply(Supply):
    def __init__(self, ab_settings, screen):
        super().__init__(ab_settings, screen)
        self.name = 'bullet_supply'
        self.image = pygame.image.load('images/bullet_supply.png').convert_alpha()



