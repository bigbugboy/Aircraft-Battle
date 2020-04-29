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
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images/enemy1_down1.png").convert_alpha(),
            pygame.image.load("images/enemy1_down2.png").convert_alpha(),
            pygame.image.load("images/enemy1_down3.png").convert_alpha(),
            pygame.image.load("images/enemy1_down4.png").convert_alpha()
            ])
        self.rect = self.image.get_rect()
        self.speed = 2
        self.reset()
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.screen_rect.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left = randint(0, self.screen_rect.width - self.rect.width)
        self.rect.top = randint(-5 * self.screen_rect.height, 0)

    def blitme(self):
        if self.active:
            self.screen.blit(self.image, self.rect)
        else:
            if not(self.ab_settings.delay % 3):
                if self.ab_settings.e1_destroy_index == 0:
                    self.ab_settings.enemy1_down_sound.play()
                self.screen.blit(
                    self.destroy_images[self.ab_settings.e1_destroy_index], self.rect)
                self.ab_settings.e1_destroy_index = (self.ab_settings.e1_destroy_index + 1) % len(self.destroy_images)
                # 毁灭图片打印完再重置
                if self.ab_settings.e1_destroy_index == 0:
                    self.reset()


class MidEnemy(Enemy):

    energy = 8

    def __init__(self, ab_settings, screen):
        super().__init__(ab_settings, screen)
        self.image = pygame.image.load('images/enemy2.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images/enemy2_down1.png").convert_alpha(),
            pygame.image.load("images/enemy2_down2.png").convert_alpha(),
            pygame.image.load("images/enemy2_down3.png").convert_alpha(),
            pygame.image.load("images/enemy2_down4.png").convert_alpha()
            ])
        self.rect = self.image.get_rect()
        self.speed = 1
        self.reset()
        self.mask = pygame.mask.from_surface(self.image)
        self.hit = False
        self.energy = self.__class__.energy

    def move(self):
        if self.rect.top < self.screen_rect.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.hit = False
        self.energy = self.__class__.energy
        self.rect.left = randint(0, self.screen_rect.width - self.rect.width)
        self.rect.top = randint(-8 * self.screen_rect.height, -self.screen_rect.height)

    def blitme(self):
        if self.active:
            self.screen.blit(self.image, self.rect)
            self.blit_my_energy()
        else:
            if not(self.ab_settings.delay % 3):
                if self.ab_settings.e2_destroy_index == 0:
                    self.ab_settings.enemy2_down_sound.play()
                self.screen.blit(
                    self.destroy_images[self.ab_settings.e2_destroy_index], self.rect)
                self.ab_settings.e2_destroy_index = (self.ab_settings.e2_destroy_index + 1) % len(self.destroy_images)
                if self.ab_settings.e2_destroy_index == 0:
                    self.reset()

    def blit_my_energy(self):
        # 血槽基座
        color = self.ab_settings.BLACK
        start_pos = self.rect.left, self.rect.top - 5
        end_pos = self.rect.right, self.rect.top - 5
        self.ab_settings.draw_energy(self.screen, color, start_pos, end_pos, 2)
        energy_left = self.energy / self.__class__.energy
        end_pos = int(self.rect.left + self.rect.width * energy_left), self.rect.top - 5
        color = self.ab_settings.GREEN if energy_left > 0.2 else self.ab_settings.RED
        self.ab_settings.draw_energy(self.screen, color, start_pos, end_pos, 2)


class BigEnemy(Enemy):

    energy = 20

    def __init__(self, ab_settings, screen):
        super().__init__(ab_settings, screen)
        self.image1 = pygame.image.load('images/enemy3_n1.png').convert_alpha()
        self.image2 = pygame.image.load('images/enemy3_n2.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images/enemy3_down1.png").convert_alpha(),
            pygame.image.load("images/enemy3_down2.png").convert_alpha(),
            pygame.image.load("images/enemy3_down3.png").convert_alpha(),
            pygame.image.load("images/enemy3_down4.png").convert_alpha(),
            pygame.image.load("images/enemy3_down5.png").convert_alpha(),
            pygame.image.load("images/enemy3_down6.png").convert_alpha()
            ])
        self.rect = self.image1.get_rect()
        self.speed = 1
        self.reset()
        self.mask = pygame.mask.from_surface(self.image1)
        self.hit = False
        self.energy = self.__class__.energy

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
        self.hit = False
        self.energy = self.__class__.energy
        self.rect.left = randint(0, self.screen_rect.width - self.rect.width)
        self.rect.top = randint(-10 * self.screen_rect.height, -5 * self.screen_rect.height)

    def blitme(self):
        if self.active:
            me_image = self.image1 if self.ab_settings.switch_image else self.image2
            self.screen.blit(me_image, self.rect)
            self.blit_my_energy()
        else:
            if not (self.ab_settings.delay % 3):
                if self.ab_settings.e2_destroy_index == 0:
                    self.ab_settings.enemy3_down_sound.play()
                self.screen.blit(
                    self.destroy_images[self.ab_settings.e3_destroy_index], self.rect)
                self.ab_settings.e3_destroy_index = (self.ab_settings.e3_destroy_index + 1) % len(self.destroy_images)
                if self.ab_settings.e3_destroy_index == 0:
                    self.ab_settings.enemy3_fly_sound.stop()
                    self.reset()

    def blit_my_energy(self):
        # 血槽基座
        color = self.ab_settings.BLACK
        start_pos = self.rect.left, self.rect.top - 5
        end_pos = self.rect.right, self.rect.top - 5
        self.ab_settings.draw_energy(self.screen, color, start_pos, end_pos, 2)
        energy_left = self.energy / self.__class__.energy
        end_pos = int(self.rect.left + self.rect.width * energy_left), self.rect.top - 5
        color = self.ab_settings.GREEN if energy_left > 0.2 else self.ab_settings.RED
        self.ab_settings.draw_energy(self.screen, color, start_pos, end_pos, 2)


