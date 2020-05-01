import pygame


class GameStatus:
    def __init__(self, ab_settings):
        self.ab_settings = ab_settings
        self.game_active = True
        self.game_paused = False
        self.game_start = False  # 默认未开始游戏，让玩家确定开始
        self.game_level = 1
        self.score_level_2 = 50000
        self.score_level_3 = 300000
        self.score_level_4 = 600000
        self.score_level_5 = 1000000






