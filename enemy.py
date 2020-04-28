import pygame
from random import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, ab_settings, screen):
        super().__init__()
        self.ab_settings = ab_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.active = True


class SmallEnemy(Enemy):
    def __init__(self, ab_settings, screen):
        super().__init__(ab_settings, screen)
        self.image = pygame.image.load('images/enemy1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 2
        self.reset()

    def move(self):
        if self.rect.top < self.screen_rect.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left = randint(0, self.screen_rect.width - self.rect.width)
        self.rect.top = randint(-5 * self.screen_rect.height, 0)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class MidEnemy(Enemy):
    def __init__(self, ab_settings, screen):
        super().__init__(ab_settings, screen)
        self.image = pygame.image.load('images/enemy2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 1
        self.reset()

    def move(self):
        if self.rect.top < self.screen_rect.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left = randint(0, self.screen_rect.width - self.rect.width)
        self.rect.top = randint(-8 * self.screen_rect.height, -self.screen_rect.height)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class BigEnemy(Enemy):
    def __init__(self, ab_settings, screen):
        super().__init__(ab_settings, screen)
        self.image1 = pygame.image.load('images/enemy3_n1.png').convert_alpha()
        self.image2 = pygame.image.load('images/enemy3_n2.png').convert_alpha()
        self.rect = self.image1.get_rect()
        self.speed = 1
        self.reset()

    def move(self):
        if self.rect.bottom == -50:
            self.ab_settings.enemy3_fly_sound.play()
        if not self.active:
            self.ab_settings.enemy3_fly_sound.stop()

        if self.rect.top < self.screen_rect.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left = randint(0, self.screen_rect.width - self.rect.width)
        self.rect.top = randint(-10 * self.screen_rect.height, -5 * self.screen_rect.height)

    def blitme(self):
        me_image = self.image1 if self.ab_settings.switch_image else self.image2
        self.screen.blit(me_image, self.rect)



