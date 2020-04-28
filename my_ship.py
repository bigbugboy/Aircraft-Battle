import pygame


class Ship(pygame.sprite.Sprite):
    def __init__(self, screen, ab_settings):
        super().__init__()
        self.ab_settings = ab_settings
        self.image1 = pygame.image.load('images/me1.png').convert_alpha()
        self.image2 = pygame.image.load('images/me2.png').convert_alpha()
        self.rect = self.image1.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.speed = 10
        self.reset()

    def blitme(self):
        me_image = self.image1 if self.ab_settings.switch_image else self.image2
        self.screen.blit(me_image, self.rect)

    def move_up(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def move_down(self):
        if self.rect.top < self.screen_rect.height - self.rect.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.top = self.screen_rect.height - self.rect.height - 60

    def move_left(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def move_right(self):
        if self.rect.right < self.screen_rect.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.screen_rect.width

    def reset(self):
        self.rect.left = (self.screen_rect.width - self.rect.width) // 2
        self.rect.top = self.screen_rect.height - self.rect.height - 60

