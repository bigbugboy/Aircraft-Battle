import sys, time
import pygame
from pygame.locals import *


def check_game_level(ab_settings, ab_state, enemy, screen):
    if ab_state.game_level == 1 and ab_settings.score >= 50000:
        ab_state.game_level = 2
        update_game_level(ab_settings, enemy, [3, 2, 1], screen, False)

    elif ab_state.game_level == 2 and ab_settings.score >= 300000:
        ab_state.game_level = 3
        update_game_level(ab_settings, enemy, [5, 3, 2], screen, True)
    elif ab_state.game_level == 3 and ab_settings.score >= 600000:
        ab_state.game_level = 4
        update_game_level(ab_settings, enemy, [5, 3, 2], screen, True)
    elif ab_state.game_level == 4 and ab_settings.score >= 1000000:
        ab_state.game_level = 5
        update_game_level(ab_settings, enemy, [5, 3, 2], screen, True)




def check_me_move(me, ab_state):
    """检测我放飞机移动事件"""
    if ab_state.game_active and not ab_state.game_paused:
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            me.move_up()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.move_down()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.move_left()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.move_right()


def check_event(me, ab_settings, ab_state, ab_board, enemy, screen):
    check_me_move(me, ab_state)
    check_game_level(ab_settings, ab_state, enemy, screen)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == ab_settings.INVINCIBLE_TIME:
            me.invincible = False
            pygame.time.set_timer(ab_settings.INVINCIBLE_TIME, 0)
        elif event.type == MOUSEBUTTONDOWN:
            # 游戏结束时
            if not ab_state.game_active:
                if event.button == 1 and ab_board.again_rect.collidepoint(event.pos):
                    ab_settings.bullet_sound.play()
                    time.sleep(0.6)
                    import main
                    main.main()
                elif event.button == 1 and ab_board.game_over_rect.collidepoint(event.pos):
                    sys.exit()
            else:
                if event.button == 1 and ab_board.pause_rect.collidepoint(event.pos):
                    ab_state.game_paused = not ab_state.game_paused
                    if ab_state.game_paused:
                        ab_board.pause_resume_image = ab_board.resume_nor_image
                        set_game_paused(ab_settings)
                    else:
                        ab_board.pause_resume_image = ab_board.pause_nor_image
                        set_game_resume(ab_settings)

        elif event.type == MOUSEMOTION:
            if ab_board.pause_rect.collidepoint(event.pos):
                if ab_state.game_paused:
                    ab_board.pause_resume_image = ab_board.resume_pressed_image
                else:
                    ab_board.pause_resume_image = ab_board.pause_pressed_image
            else:
                if ab_state.game_paused:
                    ab_board.pause_resume_image = ab_board.resume_nor_image
                else:
                    ab_board.pause_resume_image = ab_board.pause_nor_image

        elif event.type == KEYDOWN:
            if event.key == K_SPACE and ab_state.game_active and not ab_state.game_paused:
                if ab_settings.bomb_left:
                    bomb_clear_screen_enemy(ab_settings)


def bomb_clear_screen_enemy(ab_settings):
    ab_settings.bomb_sound.play()
    ab_settings.bomb_left -= 1
    for enemy in ab_settings.enemys:
        if 0 < enemy.rect.bottom < ab_settings.height + enemy.rect.height:
            enemy.active = False
            update_score(enemy, ab_settings)


def set_game_paused(ab_settings):
    ab_settings.pause_music()


def set_game_resume(ab_settings):
    ab_settings.resume_music()


def update_screen(ab_settings, screen, me, bullet1s, ab_board, ab_state):
    screen.blit(ab_settings.bg_image, (0, 0))
    if ab_state.game_active:
        ab_board.draw_pause_board()
        if not ab_state.game_paused:
            ab_board.draw_score_board()
            ab_board.draw_me_life()
            ab_board.draw_bomb_board()
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


def generate_small_enemy(enemy, num, ab_settings, screen):
    for _ in range(num):
        enemy1 = enemy.SmallEnemy(ab_settings, screen)
        ab_settings.enemys.add(enemy1)
        ab_settings.small_enemys.add(enemy1)


def generate_mid_enemy(enemy, num, ab_settings, screen):
    for _ in range(num):
        enemy1 = enemy.MidEnemy(ab_settings, screen)
        ab_settings.enemys.add(enemy1)
        ab_settings.mid_enemys.add(enemy1)


def generate_big_enemy(enemy, num, ab_settings, screen):
    for _ in range(num):
        enemy1 = enemy.BigEnemy(ab_settings, screen)
        ab_settings.enemys.add(enemy1)
        ab_settings.big_enemys.add(enemy1)


def inc_speed(enemy, increment):
    for e in enemy:
        e.speed += increment


def update_game_level(ab_settings, enemy, enemy_inc_num, screen, inc_mid_speed=False):
    ab_settings.upgrade_sound.play()
    generate_small_enemy(enemy, enemy_inc_num[0], ab_settings, screen)
    generate_mid_enemy(enemy, enemy_inc_num[1], ab_settings, screen)
    generate_big_enemy(enemy, enemy_inc_num[2], ab_settings, screen)
    inc_speed(ab_settings.small_enemys, 1)
    if inc_mid_speed:
        inc_speed(ab_settings.mid_enemys, 1)

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