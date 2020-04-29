import sys, time
import pygame
from pygame.locals import *


def check_me_move(me, ab_state):
    """检测我放飞机移动事件"""
    if ab_state.game_active:
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            me.move_up()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.move_down()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.move_left()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.move_right()


def check_event(me, ab_settings, ab_state, ab_board):
    check_me_move(me, ab_state)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == ab_settings.INVINCIBLE_TIME:
            me.invincible = False
            pygame.time.set_timer(ab_settings.INVINCIBLE_TIME, 0)
        elif event.type == MOUSEBUTTONDOWN:
            # 重新开始
            if event.button == 1 and ab_board.again_rect.collidepoint(event.pos):
                ab_settings.bullet_sound.play()
                time.sleep(1)
                import main
                main.main()
            elif event.button == 1 and ab_board.game_over_rect.collidepoint(event.pos):
                sys.exit()


def update_screen(ab_settings, screen, me, bullet1s, ab_board, ab_state):
    screen.blit(ab_settings.bg_image, (0, 0))
    if ab_state.game_active:
        ab_board.draw_score_board()
        ab_board.draw_me_life()
        me.blitme()
        blit_bullet(ab_settings, bullet1s)
        blit_enemy(ab_settings)
        check_bullet_hit_enemy(ab_settings, bullet1s)
        check_enemy_hit_me(ab_settings, me, ab_state)
    else:
        ab_settings.stop_all_music()
        ab_settings.update_recorded()
        ab_board.draw_recorded()
        ab_board.draw_final_score()
        ab_board.draw_game_over_or_again()


def is_switch_image(ab_settings):
    """每5帧切换一下我方飞机的图片"""
    if not(ab_settings.delay % 5):
        ab_settings.switch_image = not ab_settings.switch_image


def update_delay(ab_settings):
    """
    改变图片显示的延迟变量值
    :param ab_settings:
    :return:
    """
    ab_settings.delay -= 1
    if ab_settings == 0:
        ab_settings.delay = 100


def generate_bullet(Bullet1, screen, ab_settings, me):
    bullet1s = []
    bullet_num = 4
    for _ in range(bullet_num):
        bullet1s.append(Bullet1(screen, ab_settings, me))
    return bullet1s


def blit_bullet(ab_settings, bullet1s):
    # 每个10帧，重置一个子弹的位置
    if not (ab_settings.delay % 10):
        ab_settings.bullet_sound.play()
        bullet1s[ab_settings.bullet1_index].reset()
        ab_settings.bullet1_index = (ab_settings.bullet1_index + 1) % ab_settings.bullet1_num
    for bullet in bullet1s:
        bullet.move()
        bullet.blitme()


def generate_small_enemys(enemy_type, num, ab_settings, screen):
    for _ in range(num):
        enemy1 = enemy_type.SmallEnemy(ab_settings, screen)
        ab_settings.enemys.add(enemy1)
        ab_settings.small_enemys.add(enemy1)


def generate_mid_enemys(enemy_type, num, ab_settings, screen):
    for _ in range(num):
        enemy2 = enemy_type.MidEnemy(ab_settings, screen)
        ab_settings.enemys.add(enemy2)
        ab_settings.mid_enemys.add(enemy2)


def generate_big_enemys(enemy_type, num, ab_settings, screen):
    for _ in range(num):
        enemy3 = enemy_type.BigEnemy(ab_settings, screen)
        ab_settings.enemys.add(enemy3)
        ab_settings.big_enemys.add(enemy3)



def blit_enemy(ab_settings):
    for enemy_type in ab_settings.blit_enemy_order:
        for enemy in enemy_type:
            enemy.move()
            enemy.blitme()


def check_bullet_hit_enemy(ab_settings, bullet1s):
    for bullet in bullet1s:
        if bullet.active:
            enemy_hit = pygame.sprite.spritecollide(bullet, ab_settings.enemys, False, pygame.sprite.collide_mask)
            if enemy_hit:
                bullet.active = False
                for enemy in enemy_hit:
                    enemy.hit = True
                    enemy.energy -= 1
                    if enemy.energy == 0:
                        enemy.active = False
                        update_score(enemy, ab_settings)


def update_score(enemy, ab_settings):
    if enemy in ab_settings.big_enemys:
        ab_settings.score += 10000
    elif enemy in ab_settings.mid_enemys:
        ab_settings.score += 5000
    else:
        ab_settings.score += 1000


def check_enemy_hit_me(ab_settings, me, ab_state):
    if me.active and not me.invincible:
        enemy_down = pygame.sprite.spritecollide(
            me, ab_settings.enemys,
            False, pygame.sprite.collide_mask)
        if enemy_down:
            me.active = False
            me.invincible = True
            pygame.time.set_timer(ab_settings.INVINCIBLE_TIME, 5 * 1000)    # 5s无敌时间
            ab_settings.me_life_left -= 1
            if ab_settings.me_life_left == 0:
                ab_state.game_active = False
            for enemy in enemy_down:
                enemy.active = False