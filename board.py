import pygame


class Board:
    def __init__(self, ab_settings, screen):
        self.ab_settings = ab_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.score_font = pygame.font.Font('fonts/font.ttf', 36)
        self.me_life = pygame.image.load('images/life.png').convert_alpha()
        self.me_life_rect = self.me_life.get_rect()
        self.game_over_score_font = pygame.font.Font("fonts/font.ttf", 48)
        self.game_over_text1_surface = self.game_over_score_font.render('Your Score:', True, self.ab_settings.WHITE)
        self.game_over_text1_rect = self.game_over_text1_surface.get_rect()

        self.again_image = pygame.image.load("images/again.png").convert_alpha()
        self.again_rect = self.again_image.get_rect()
        self.game_over_image = pygame.image.load("images/gameover.png").convert_alpha()
        self.game_over_rect = self.game_over_image.get_rect()



    def draw_score_board(self):
        score_text = f'Scores : {self.ab_settings.score}'
        score_surface = self.score_font.render(score_text, True, self.ab_settings.WHITE)
        self.screen.blit(score_surface, (10, 5))

    def draw_me_life(self):
        if self.ab_settings.me_life_left:
            for i in range(self.ab_settings.me_life_left):
                life_pos = (self.screen_rect.width - 10- (i+1) * self.me_life_rect.width,
                            self.screen_rect.height - self.me_life_rect.height - 10)
                self.screen.blit(self.me_life, life_pos)

    def draw_recorded(self):
        recorded_text = f'Best : {self.ab_settings.recorded}'
        recorded_surface = self.score_font.render(recorded_text, True, self.ab_settings.WHITE)
        self.screen.blit(recorded_surface, (50,50))

    def draw_final_score(self):
        self.game_over_text1_rect.left = (self.screen_rect.width - self.game_over_text1_rect.width) // 2
        self.game_over_text1_rect.top = self.screen_rect.height // 2
        self.screen.blit(self.game_over_text1_surface, self.game_over_text1_rect)
        self.game_over_text2_surface = self.game_over_score_font.render(str(self.ab_settings.score), True, self.ab_settings.WHITE)
        self.game_over_text2_rect = self.game_over_text2_surface.get_rect()
        self.game_over_text2_rect.left = (self.screen_rect.width - self.game_over_text2_rect.width) // 2
        self.game_over_text2_rect.top = self.game_over_text1_rect.bottom + 10
        self.screen.blit(self.game_over_text2_surface, self.game_over_text2_rect)

    def draw_game_over_or_again(self):
        self.again_rect.left = (self.screen_rect.width - self.again_rect.width) // 2
        self.again_rect.top = self.game_over_text2_rect.bottom + 50
        self.game_over_rect.left = (self.screen_rect.width - self.again_rect.width) // 2
        self.game_over_rect.top = self.again_rect.bottom + 10
        self.screen.blit(self.again_image, self.again_rect)
        self.screen.blit(self.game_over_image, self.game_over_rect)




