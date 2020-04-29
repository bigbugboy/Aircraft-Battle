import pygame


class Ship(pygame.sprite.Sprite):
    def __init__(self, screen, ab_settings):
        super().__init__()
        self.ab_settings = ab_settings
        self.image1 = pygame.image.load('images/me1.png').convert_alpha()
        self.image2 = pygame.image.load('images/me2.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images/me_destroy_1.png").convert_alpha(),
            pygame.image.load("images/me_destroy_2.png").convert_alpha(),
            pygame.image.load("images/me_destroy_3.png").convert_alpha(),
            pygame.image.load("images/me_destroy_4.png").convert_alpha()
            ])
        self.rect = self.image1.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.speed = 10
        self.active = True
        self.invincible = False
        self.reset()
        self.mask = pygame.mask.from_surface(self.image1)

    def blitme(self):
        if self.active:
            me_image = self.image1 if self.ab_settings.switch_image else self.image2
            self.screen.blit(me_image, self.rect)
        else:
            if not(self.ab_settings.delay % 3):
                if self.ab_settings.me_destroy_index == 0:
                    self.ab_settings.me_down_sound.play()
                self.screen.blit(self.destroy_images[self.ab_settings.me_destroy_index], self.rect)
                self.ab_settings.me_destroy_index = (self.ab_settings.me_destroy_index + 1) % len(self.destroy_images)
                if self.ab_settings.me_destroy_index == 0:
                    print('Game over')
                    self.reset()


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
        self.active = True
        self.rect.left = (self.screen_rect.width - self.rect.width) // 2
        self.rect.top = self.screen_rect.height - self.rect.height - 60

