import pygame

from settings import Settings
from my_ship import Ship
from bullet import Bullet1, Bullet2
from board import Board
from game_status import GameStatus
import enemy, supply
import game_functions as gf


def main():
    ab_settings = Settings()
    screen = pygame.display.set_mode(ab_settings.bg_size)
    ab_settings.bg_image = pygame.image.load('images/background.png').convert_alpha()
    ab_state = GameStatus(ab_settings)
    ab_board = Board(ab_settings, screen, ab_state)
    me = Ship(screen, ab_settings)
    ab_supply = gf.generate_supply(ab_settings, screen, supply)
    bullet1s = gf.generate_bullet(Bullet1, screen, ab_settings)
    bullet2s = gf.generate_bullet(Bullet2, screen, ab_settings)
    gf.generate_small_enemy(enemy, 15, ab_settings, screen)
    gf.generate_mid_enemy(enemy, 5, ab_settings, screen)
    gf.generate_big_enemy(enemy, 1, ab_settings, screen)

    while 1:
        gf.check_event(me, ab_settings, ab_state, ab_board, enemy, screen, ab_supply)
        gf.is_switch_image(ab_settings)
        gf.update_delay(ab_settings)
        bullets = gf.check_bullet_type(ab_settings, bullet1s, bullet2s)
        gf.update_screen(ab_settings, screen, me, bullets, ab_board, ab_state, ab_supply)

        pygame.display.flip()
        ab_settings.clock.tick(60)


if __name__ == '__main__':
    main()