import os
import pygame


class Settings:
    def __init__(self):
        self.caption = '飞机大战 - by xliu'
        self.width = 400
        self.height = 650
        self.bg_size = self.width, self.height
        self.clock = pygame.time.Clock()
        self.is_start_music = True
        self.init_game()    # 初始启动pygame配置
        self.delay = 100    # 延迟操作的变量，每帧减一
        self.switch_image = True
        self.bullet1_num = 4
        self.bullet1_index = 0

    def init_game(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(self.caption)
        self.init_load_music_sound()
        self.init_play_music()

    def init_play_music(self):
        if self.is_start_music:
            pygame.mixer.music.play(-1)

    def init_load_music_sound(self):
        pygame.mixer.music.load("sounds/game_music.ogg")
        pygame.mixer.music.set_volume(0.2)
        self.bullet_sound = pygame.mixer.Sound("sounds/bullet.wav")
        self.bullet_sound.set_volume(0.2)
        self.bomb_sound = pygame.mixer.Sound("sounds/use_bomb.wav")
        self.bomb_sound.set_volume(0.2)
        self.supply_sound = pygame.mixer.Sound("sounds/supply.wav")
        self.supply_sound.set_volume(0.2)
        self.get_bomb_sound = pygame.mixer.Sound("sounds/get_bomb.wav")
        self.get_bomb_sound.set_volume(0.2)
        self.get_bullet_sound = pygame.mixer.Sound("sounds/get_bullet.wav")
        self.get_bullet_sound.set_volume(0.2)
        self.upgrade_sound = pygame.mixer.Sound("sounds/upgrade.wav")
        self.upgrade_sound.set_volume(0.2)
        self.enemy3_fly_sound = pygame.mixer.Sound("sounds/enemy3_flying.wav")
        self.enemy3_fly_sound.set_volume(0.3)
        self.enemy1_down_sound = pygame.mixer.Sound("sounds/enemy1_down.wav")
        self.enemy1_down_sound.set_volume(0.2)
        self.enemy2_down_sound = pygame.mixer.Sound("sounds/enemy2_down.wav")
        self.enemy2_down_sound.set_volume(0.2)
        self.enemy3_down_sound = pygame.mixer.Sound("sounds/enemy3_down.wav")
        self.enemy3_down_sound.set_volume(0.5)
        self.me_down_sound = pygame.mixer.Sound("sounds/me_down.wav")
        self.me_down_sound.set_volume(0.2)


