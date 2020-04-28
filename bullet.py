import pygame


class Bullet1(pygame.sprite.Sprite):
    def __init__(self, screen, ab_settings, me):
        super().__init__()
        self.ab_settings = ab_settings
        self.me = me
        self.image = pygame.image.load('images/bullet1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.scree = screen
        self.scree_rect = self.scree.get_rect()
        self.speed = 12
        self.active = True
        self.reset()

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top <= 0:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.centerx, self.rect.top = self.me.rect.centerx, self.me.rect.top - 5

    def blitme(self):
        self.scree.blit(self.image, self.rect)

