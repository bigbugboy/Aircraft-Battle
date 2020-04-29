import pygame


class GameStatus:
    def __init__(self, ab_settings):
        self.ab_settings = ab_settings
        self.game_active = True
        self.game_paused = False

    def restart_game(self):
        self.ab_settings.score = 0
        self.ab_settings.me_life_left = 3




