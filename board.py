import pygame


class Board:
    def __init__(self, ab_settings, screen, ab_state):
        self.ab_settings = ab_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ab_state = ab_state
        self.score_font = pygame.font.Font('fonts/font.ttf', 36)
        self.me_life = pygame.image.load('images/life.png').convert_alpha()
        self.me_life_rect = self.me_life.get_rect()
        self.final_score_font = pygame.font.Font("fonts/font.ttf", 48)
        self.final_score_surface = self.final_score_font.render('Your Score:', True, self.ab_settings.WHITE)
        self.final_score_rect = self.final_score_surface.get_rect()
        self.final_score_rect.center = self.screen_rect.center

        self.again_image = pygame.image.load("images/again.png").convert_alpha()
        self.again_rect = self.again_image.get_rect()
        self.game_over_image = pygame.image.load("images/gameover.png").convert_alpha()
        self.game_over_rect = self.game_over_image.get_rect()

        self.pause_nor_image = pygame.image.load('images/pause_nor.png').convert_alpha()
        self.pause_pressed_image = pygame.image.load('images/pause_pressed.png').convert_alpha()
        self.pause_rect = self.pause_nor_image.get_rect()
        self.resume_nor_image = pygame.image.load('images/resume_nor.png').convert_alpha()
        self.resume_pressed_image = pygame.image.load('images/resume_pressed.png').convert_alpha()
        self.resume_rect = self.resume_nor_image.get_rect()
        self.pause_rect.left = self.screen_rect.width - self.pause_rect.width - 10
        self.pause_rect.top = 10
        self.resume_rect.left = self.screen_rect.width - self.resume_rect.width - 10
        self.resume_rect.top = 10
        self.pause_resume_image = self.pause_nor_image

        self.bomb_image = pygame.image.load('images/bomb.png').convert_alpha()
        self.bomb_rect = self.bomb_image.get_rect()
        self.bomb_font = self.final_score_font
        self.is_confirm = False
        self.mouse_image = pygame.image.load('images/check.png').convert_alpha()
        self.game_desc_image = pygame.image.load('images/desc.png').convert_alpha()
        self.game_desc_rect = self.game_desc_image.get_rect()


    def draw_bomb_board(self):
        bomb_text = f'x{self.ab_settings.bomb_left}'
        bomb_text_surface = self.bomb_font.render(bomb_text, True, self.ab_settings.WHITE)
        bomb_text_rect = bomb_text_surface.get_rect()
        self.screen.blit(self.bomb_image, (10, self.screen_rect.height - self.bomb_rect.height - 10))
        self.screen.blit(bomb_text_surface, (20 + self.bomb_rect.width, self.screen_rect.height - 5 - bomb_text_rect.height))

    def draw_score_board(self):
        score_text = f'Scores : {format(self.ab_settings.score, ",")}'
        score_surface = self.score_font.render(score_text, True, self.ab_settings.WHITE)
        self.screen.blit(score_surface, (10, 5))

    def draw_me_life(self):
        if self.ab_settings.me_life_left:
            for i in range(self.ab_settings.me_life_left):
                life_pos = (self.screen_rect.width - 10- (i+1) * self.me_life_rect.width,
                            self.screen_rect.height - self.me_life_rect.height - 10)
                self.screen.blit(self.me_life, life_pos)

    def draw_recorded(self):
        recorded_text = f'Best : {format(self.ab_settings.recorded, ",")}'
        recorded_surface = self.score_font.render(recorded_text, True, self.ab_settings.WHITE)
        self.screen.blit(recorded_surface, (50,50))

    def draw_final_score(self):
        if self.ab_settings.new_recorded:
            # 新纪录时，加粗
            self.final_score_font.set_bold(True)
            self.final_score_surface = self.final_score_font.render('New record:', True, self.ab_settings.WHITE)
        final_value_surface = self.final_score_font.render(format(self.ab_settings.score, ","), True, self.ab_settings.WHITE)
        self.final_value_rect = final_value_surface.get_rect()
        self.final_value_rect.centerx = self.screen_rect.centerx
        self.final_value_rect.centery = self.screen_rect.centery + self.final_value_rect.height
        self.screen.blit(self.final_score_surface, self.final_score_rect)
        self.screen.blit(final_value_surface, self.final_value_rect)

    def draw_game_over_or_again(self):
        self.again_rect.centerx = self.screen_rect.centerx
        self.again_rect.top = self.final_value_rect.bottom + 50
        self.game_over_rect.centerx = self.screen_rect.centerx
        self.game_over_rect.top = self.again_rect.bottom + 10
        self.screen.blit(self.again_image, self.again_rect)
        self.screen.blit(self.game_over_image, self.game_over_rect)

    def draw_confirm_mouse(self):
        if self.is_confirm:
            pygame.mouse.set_visible(False)
            self.mouse_rect = self.mouse_image.get_rect()
            self.mouse_rect = pygame.mouse.get_pos()
            self.screen.blit(self.mouse_image, self.mouse_rect)

    def draw_pause_board(self):
        # 默认显示暂停按钮
        self.screen.blit(self.pause_resume_image, self.pause_rect)

    def draw_game_start(self):
        start_text1 = 'Welcome to Aircraft-Battle'
        start_text2 = 'Press any key to start the game'
        game_start_font = pygame.font.SysFont('arial', 30, True)
        for i in range(2):
            game_start_surface = game_start_font.render(eval(f'start_text{i+1}'), False, self.ab_settings.WHITE)
            game_start_rect = game_start_surface.get_rect()
            game_start_rect.centerx = self.screen_rect.centerx
            game_start_rect.centery = self.screen_rect.centery - 40 + i * 40
            self.screen.blit(game_start_surface, game_start_rect)
        self.game_desc_rect.centerx = self.screen_rect.centerx
        self.game_desc_rect.bottom = self.screen_rect.bottom - 100
        self.screen.blit(self.game_desc_image, self.game_desc_rect)