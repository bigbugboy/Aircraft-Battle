import pygame

from settings import Settings
from my_ship import Ship
from bullet import Bullet1
from board import Board
from game_status import GameStatus
import enemy
import game_functions as gf


def main():
    ab_settings = Settings()
    screen = pygame.display.set_mode(ab_settings.bg_size)
    ab_settings.bg_image = pygame.image.load('images/background.png').convert_alpha()
    ab_state = GameStatus(ab_settings)
    ab_board = Board(ab_settings, screen, ab_state)
    me = Ship(screen, ab_settings)
    bullet1s = gf.generate_bullet(Bullet1, screen, ab_settings, me)
    gf.generate_small_enemy(enemy, 15, ab_settings, screen)
    gf.generate_mid_enemy(enemy, 5, ab_settings, screen)
    gf.generate_big_enemy(enemy, 1, ab_settings, screen)

    while 1:
        gf.check_event(me, ab_settings, ab_state, ab_board, enemy, screen)
        gf.is_switch_image(ab_settings)
        gf.update_delay(ab_settings)
        gf.update_screen(ab_settings, screen, me, bullet1s, ab_board, ab_state)

        pygame.display.flip()
        ab_settings.clock.tick(60)



if __name__ == '__main__':
    main()