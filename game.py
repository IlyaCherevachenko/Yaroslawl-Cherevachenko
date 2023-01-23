from pygame import *
from menu import Gameover, Menu, Win, Pause
from world import World
from environment import Score, Healthbar

size = width, height = 1200, 850
FPS = 60
bullets = []
backgrounds = []


if __name__ == '__main__':
    mixer.init(48000, -16, 1, 1024)
    init()
    screen = display.set_mode(size)
    display.set_caption('The Savior')
    display.set_icon(image.load('image/icon/icon2.png'))
    clock = time.Clock()

    world = World(screen, bullets)
    game_over = Gameover(screen)
    menu = Menu(screen, width, height)
    score = Score(screen)
    win = Win(screen)
    health_bar = Healthbar(screen)
    pause = Pause(screen)

    mixer.music.load('sounds/menu/stone-fortress.wav')
    kill_enemy = mixer.Sound('sounds/attack_enemy/STRM_gob_Kill.wav')
    attack_sound = mixer.Sound('sounds/play/attack_hero.wav')
    bird_sound = mixer.Sound('sounds/play/bird_song_1.wav')

    mixer.music.play()

    running = True
    begin = True

    while running:
        if begin:
            world.render_world()
            for background in world.background_group:
                backgrounds.append(background)

            for hero_ohne_group in world.hero_group:
                hero = hero_ohne_group

        for value in event.get():
            if value.type == QUIT:
                running = False
            elif value.type == KEYUP:
                hero.go = False
            elif value.type == KEYDOWN:
                if value.key == K_e and sprite.spritecollide(hero, world.cage_group, False):
                    hero.this_cage.image = image.load('image/environ/cage/cage.png')
                    hero.cage_count += 1
                    bird_sound.play()
                elif value.key == K_ESCAPE:
                    pause.pause_status = True

        if menu.menu:
            menu.render()
            display.update()
            begin = False
        else:
            mixer.music.stop()
            if not pause.pause_status:
                if not hero.win:
                    if not hero.over:
                        world.background_group.draw(screen)
                        world.ground_group.draw(screen)

                        score.render_cage_score(hero.cage_count)
                        score.render_kill_score(hero.kill_count)
                        health_bar.render(hero.health)

                        hero.all_sprites = world.all_sprites
                        if backgrounds[0].rect.left + 120 >= hero.rect.left:
                            hero.can_scroll_right = False
                        elif backgrounds[2].rect.right - 120 <= hero.rect.right:
                            hero.can_scroll_left = False

                        if hero.can_scroll_left:
                            for sprites in world.all_sprites:
                                sprites.rect.x -= 6
                            hero.can_scroll_left = False
                        elif hero.can_scroll_right:
                            for sprites in world.all_sprites:
                                sprites.rect.x += 6
                            hero.can_scroll_right = False

                        for platform in world.platform_group:
                            if platform.rect.left - 50 < hero.rect.x < platform.rect.right + 50 and hero.rect.y < platform.rect.bottom + 30:
                                this_platform = platform.rect.y
                                hero.this_platform = platform
                                break
                            else:
                                this_platform = 0

                        if hero.cage_count == 4 and hero.kill_count == 5:
                            hero.win = True

                        for cage in world.cage_group:
                            if cage.rect.left - 50 < hero.rect.x < cage.rect.right + 50:
                                hero.this_cage = cage
                                break

                        hero.update(750 - hero.rect.height, this_platform - hero.rect.height)
                        hero.action()
                        hero.render()

                        world.hero_group.draw(screen)
                        world.platform_group.draw(screen)
                        world.cage_group.draw(screen)
                        world.bomb_group.draw(screen)

                        for bomb in world.bomb_group:
                            bomb.hero = hero
                            bomb.hero_group = world.hero_group
                            bomb.render()
                            if bomb.boom_frame > 3:
                                world.bomb_group.remove(bomb)
                                bomb.boom = False

                        for bullet in bullets:
                            if sprite.spritecollide(bullet, world.enemy_group, False):
                                for enemy in world.enemy_group:
                                    if abs(enemy.rect.x - bullet.rect.x) < 120:
                                        enemy.health -= 1
                                        attack_sound.play()
                                bullets.remove(bullet)

                        for enemy in world.enemy_group:
                            if enemy.health <= 0:
                                world.enemy_group.remove(enemy)
                                kill_enemy.play()
                                enemy.alive_enemy = False
                                hero.kill_count += 1
                            enemy.update()
                            enemy.action()

                        world.enemy_group.draw(screen)

                        display.update()
                    else:
                        game_over.render()
                        display.update()
                        backgrounds[0].rect.left = 0
                        backgrounds[2].rect.right = 3500
                        world.clean_world()
                        game_over.sounds_play = True
                        menu.music_play.stop()
                        if game_over.click():
                            begin = True
                            menu.menu = True
                            mixer.music.play()
                else:
                    win.render()
                    display.update()
                    backgrounds[0].rect.left = 0
                    backgrounds[2].rect.right = 3500
                    world.clean_world()
                    menu.music_play.stop()
                    if win.click():
                        begin = True
                        menu.menu = True
                        mixer.music.play()
            else:
                pause.render()
                display.update()
                if pause.click():
                    menu.music_play.stop()
                    backgrounds[0].rect.left = 0
                    backgrounds[2].rect.right = 3500
                    world.clean_world()
                    begin = True
                    menu.menu = True
                    pause.pause_status = False
                    mixer.music.play()
        clock.tick(FPS)
quit()
