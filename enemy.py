import pygame
from random import *


class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()
        self.image = pygame.image.load('images/enemy1.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load('images/enemy1_down1.png').convert_alpha(),
            pygame.image.load('images/enemy1_down2.png').convert_alpha(),
            pygame.image.load('images/enemy1_down3.png').convert_alpha(),
            pygame.image.load('images/enemy1_down4.png').convert_alpha(),
        ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size
        self.speed = 2
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        self.reset()

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-5 * self.height, 0)


class MidEnemy(pygame.sprite.Sprite):

    energy = 8

    def __init__(self, bg_size):
        super().__init__()
        self.image = pygame.image.load('images/enemy2.png').convert_alpha()
        self.hit_image = pygame.image.load('images/enemy2_hit.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load('images/enemy2_down1.png').convert_alpha(),
            pygame.image.load('images/enemy2_down2.png').convert_alpha(),
            pygame.image.load('images/enemy2_down3.png').convert_alpha(),
            pygame.image.load('images/enemy2_down4.png').convert_alpha(),
        ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size
        self.speed = 1
        self.active = True
        self.hit = False
        self.mask = pygame.mask.from_surface(self.image)
        self.reset()

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.hit = False
        self.active = True
        self.energy = self.__class__.energy
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-10 * self.height, -self.height)


class BigEnemy(pygame.sprite.Sprite):

    energy = 20

    def __init__(self, bg_size):
        super().__init__()
        self.hit = False
        self.active = True
        self.image1 = pygame.image.load('images/enemy3_n1.png').convert_alpha()
        self.image2 = pygame.image.load('images/enemy3_n2.png').convert_alpha()
        self.hit_image = pygame.image.load('images/enemy3_hit.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load('images/enemy3_down1.png').convert_alpha(),
            pygame.image.load('images/enemy3_down2.png').convert_alpha(),
            pygame.image.load('images/enemy3_down3.png').convert_alpha(),
            pygame.image.load('images/enemy3_down4.png').convert_alpha(),
            pygame.image.load('images/enemy3_down5.png').convert_alpha(),
            pygame.image.load('images/enemy3_down6.png').convert_alpha(),
        ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size
        self.speed = 1
        self.mask = pygame.mask.from_surface(self.image1)
        self.reset()

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.energy = self.__class__.energy
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-15 * self.height, -5 * self.height)
