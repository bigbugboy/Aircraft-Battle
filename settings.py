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
        self.bullet1_index = 0      # 绘制是切换索引
        self.e1_destroy_index = 0  # 小型敌机击中时绘制切换索引
        self.e2_destroy_index = 0
        self.e3_destroy_index = 0
        self.me_destroy_index = 0
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.score = 0
        self.recorded = self.get_recorded()
        self.me_life_left = 3
        self.INVINCIBLE_TIME = pygame.USEREVENT

    def init_game(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(self.caption)
        self.init_load_music_sound()
        self.init_play_music()
        self.generate_enemy_groups()

    def init_play_music(self):
        if self.is_start_music:
            pygame.mixer.music.play(-1)

    def stop_all_music(self):
        pygame.mixer.music.stop()
        self.enemy3_fly_sound.stop()

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
        self.enemy3_down_sound.set_volume(0.3)
        self.me_down_sound = pygame.mixer.Sound("sounds/me_down.wav")
        self.me_down_sound.set_volume(0.2)

    def generate_enemy_groups(self):
        self.enemys = pygame.sprite.Group()
        self.small_enemys = pygame.sprite.Group()
        self.mid_enemys = pygame.sprite.Group()
        self.big_enemys = pygame.sprite.Group()
        self.blit_enemy_order = [self.big_enemys, self.mid_enemys, self.small_enemys]

    def draw_energy(self, screen, color, start, end, width):
        pygame.draw.line(screen, color, start, end, width)

    def get_recorded(self):
        if not os.path.exists('recorded.txt'):
            return 0
        else:
            with open('recorded.txt', 'r', encoding='utf-8') as f:
                return int(f.read().strip())

    def update_recorded(self):
        if self.score > self.recorded:
            self.recorded = self.score
            with open('recorded.txt', 'w', encoding='utf-8') as f:
                f.write(str(self.score))