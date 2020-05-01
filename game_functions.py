import sys, random
import pygame
from pygame.locals import *


def check_game_level(ab_settings, ab_state, enemy, screen):
    if ab_state.game_level == 1 and ab_settings.score >= ab_state.score_level_2:
        ab_state.game_level = 2
        update_game_level(ab_settings, enemy, [3, 2, 1], screen, False)
    elif ab_state.game_level == 2 and ab_settings.score >= ab_state.score_level_3:
        ab_state.game_level = 3
        update_game_level(ab_settings, enemy, [5, 3, 2], screen, True)
    elif ab_state.game_level == 3 and ab_settings.score >= ab_state.score_level_4:
        ab_state.game_level = 4
        update_game_level(ab_settings, enemy, [5, 3, 2], screen, True)
    elif ab_state.game_level == 4 and ab_settings.score >= ab_state.score_level_5:
        ab_state.game_level = 5
        update_game_level(ab_settings, enemy, [5, 3, 2], screen, True)


def check_me_move(me, ab_state):
    """检测我方飞机移动事件"""
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


def check_event(me, ab_settings, ab_state, ab_board, enemy, screen, ab_supply):
    check_me_move(me, ab_state)
    check_game_level(ab_settings, ab_state, enemy, screen)
    for event in pygame.event.get():
        if event.type == QUIT:
            ab_settings.update_recorded()
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:
            # 游戏结束时
            if not ab_state.game_active:
                if event.button == 1 and ab_board.again_rect.collidepoint(event.pos):
                    ab_settings.button_sound.play()
                    reset_game()
                elif event.button == 1 and ab_board.game_over_rect.collidepoint(event.pos):
                    sys.exit()
            elif ab_state.game_start:
                if event.button == 1 and ab_board.pause_rect.collidepoint(event.pos):
                    ab_settings.button_sound.play()
                    ab_state.game_paused = not ab_state.game_paused
                    if ab_state.game_paused:
                        ab_board.pause_resume_image = ab_board.resume_nor_image
                        set_game_paused(ab_settings)
                    else:
                        ab_board.pause_resume_image = ab_board.pause_nor_image
                        set_game_resume(ab_settings)

        elif event.type == MOUSEMOTION:
            # 游戏未结束时
            if ab_state.game_start and ab_state.game_active:
                if ab_board.pause_rect.collidepoint(event.pos):
                    ab_board.is_confirm = True
                    if ab_state.game_paused:
                        ab_board.pause_resume_image = ab_board.resume_pressed_image
                    else:
                        ab_board.pause_resume_image = ab_board.pause_pressed_image
                else:
                    ab_board.is_confirm = False
                    pygame.mouse.set_visible(True)
                    if ab_state.game_paused:
                        ab_board.pause_resume_image = ab_board.resume_nor_image
                    else:
                        ab_board.pause_resume_image = ab_board.pause_nor_image
            elif not ab_state.game_active:
                if ab_board.again_rect.collidepoint(event.pos):
                    ab_board.is_confirm = True
                elif ab_board.game_over_rect.collidepoint(event.pos):
                    ab_board.is_confirm = True
                else:
                    ab_board.is_confirm = False
                    pygame.mouse.set_visible(True)

        elif event.type == KEYDOWN:
            if not ab_state.game_start:
                ab_state.game_start = True
            elif event.key == K_SPACE and not ab_state.game_paused:
                if ab_settings.bomb_left:
                    bomb_clear_screen_enemy(ab_settings)

        elif event.type == ab_settings.INVINCIBLE_TIME:
            me.invincible = False
            pygame.time.set_timer(ab_settings.INVINCIBLE_TIME, 0)

        elif event.type == ab_settings.SUPPLY_TIME:
            if ab_state.game_start and not ab_state.game_paused:
                ab_settings.supply_sound.play()
                supply = random.choice(ab_supply)
                supply.reset()
        elif event.type == ab_settings.DOUBLE_BULLET_TIME:
            ab_settings.is_double_bullet = False
            pygame.time.set_timer(ab_settings.DOUBLE_BULLET_TIME, 0)


def reset_game():
    pygame.mouse.set_visible(True)
    import main
    main.main()


def generate_supply(ab_settings, screen, supply):
    bomb_supply = supply.BombSupply(ab_settings, screen)
    bullet_supply = supply.BulletSupply(ab_settings, screen)
    return [bomb_supply, bullet_supply]


def bomb_clear_screen_enemy(ab_settings):
    ab_settings.bomb_sound.play()
    ab_settings.bomb_left -= 1
    for enemy in ab_settings.enemys:
        if 0 < enemy.rect.bottom < ab_settings.height + enemy.rect.height:
            enemy.active = False
            update_score(enemy, ab_settings)


def set_game_paused(ab_settings):
    ab_settings.pause_music()
    pygame.time.set_timer(ab_settings.SUPPLY_TIME, 0)


def set_game_resume(ab_settings):
    ab_settings.resume_music()
    pygame.time.set_timer(ab_settings.SUPPLY_TIME, 30*1000)


def check_bullet_type(ab_settings, bullet1s, bullet2s):
    bullets = bullet2s if ab_settings.is_double_bullet else bullet1s
    return bullets


def update_screen(ab_settings, screen, me, bullets, ab_board, ab_state, ab_supply):
    screen.blit(ab_settings.bg_image, (0, 0))
    if not ab_state.game_start:
        ab_board.draw_game_start()
        blit_bullet(ab_settings, bullets, me)
        me.blitme()

    elif ab_state.game_active:
        ab_board.draw_pause_board()
        if not ab_state.game_paused:
            ab_board.draw_score_board()
            ab_board.draw_me_life()
            ab_board.draw_bomb_board()
            me.blitme()
            blit_bullet(ab_settings, bullets, me)
            blit_enemy(ab_settings)
            blit_supply(ab_supply)
            check_supply_hit_me(ab_settings, me, ab_supply)
            check_bullet_hit_enemy(ab_settings, bullets)
            check_enemy_hit_me(ab_settings, me, ab_state)
    else:
        ab_settings.stop_all_music()
        ab_settings.update_recorded()
        ab_board.draw_recorded()
        ab_board.draw_final_score()
        ab_board.draw_game_over_or_again()

    ab_board.draw_confirm_mouse()


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


def generate_bullet1(Bullet1, screen, ab_settings):
    bullet1s = []
    bullet_num = 4
    for _ in range(bullet_num):
        bullet1s.append(Bullet1(screen, ab_settings))
    return bullet1s


def generate_bullet2(Bullet2, screen, ab_settings):
    bullet2s = []
    bullet_num = 8
    for _ in range(bullet_num // 2):
        bullet2s.append(Bullet2(screen, ab_settings))
        bullet2s.append(Bullet2(screen, ab_settings))
    return bullet2s


def blit_bullet(ab_settings, bullets, me):
    # 每个10帧，重置一个子弹的位置
    if not (ab_settings.delay % 10):
        ab_settings.bullet_sound.play()
        if ab_settings.is_double_bullet:
            bullets[ab_settings.bullet2_index].reset((me.rect.centerx - 33, me.rect.centery))
            bullets[ab_settings.bullet2_index + 1].reset((me.rect.centerx + 30, me.rect.centery))
            ab_settings.bullet2_index = (ab_settings.bullet2_index + 2) % ab_settings.bullet2_num
        else:
            bullets[ab_settings.bullet1_index].reset((me.rect.centerx, me.rect.top - 5))
            ab_settings.bullet1_index = (ab_settings.bullet1_index + 1) % ab_settings.bullet1_num
    for bullet in bullets:
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


def blit_supply(ab_supply):
    for supply in ab_supply:
        if supply.active:
            supply.move()
            supply.blitme()


def check_supply_hit_me(ab_settings, me, ab_supply):
    for supply in ab_supply:
        if supply.active:
            if pygame.sprite.collide_mask(me, supply):
                supply.active = False
                if supply.name == 'bomb_supply':
                    ab_settings.get_bomb_sound.play()
                    if ab_settings.bomb_left < 3:
                        ab_settings.bomb_left += 1
                elif supply.name == 'bullet_supply':
                    ab_settings.get_bullet_sound.play()
                    ab_settings.is_double_bullet = True
                    pygame.time.set_timer(ab_settings.DOUBLE_BULLET_TIME, 18 * 1000)    # 18s双弹模式


def check_bullet_hit_enemy(ab_settings, bullets):
    for bullet in bullets:
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
                pygame.time.delay(100)
            for enemy in enemy_down:
                enemy.active = False