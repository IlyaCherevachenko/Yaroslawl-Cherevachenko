from pygame import *
from menu import Menu, Game_over
from world import World

size = width, height = 3800, 720
FPS = 60
bullets = []

if __name__ == '__main__':
    init()
    screen = display.set_mode(size)
    display.set_caption('BossFight')
    display.set_icon(image.load('image/icon/icon2.png'))
    Arial_50 = font.SysFont('arial', 50)
    clock = time.Clock()

    game_over = Game_over(screen)
    world = World(width, height, screen, bullets)

    world.render_world()

    for hero_ohne_group in world.hero_group:
        hero = hero_ohne_group

    running = True

    while running:

        for value in event.get():
            if value.type == QUIT:
                running = False
            elif value.type == KEYUP:
                hero.go = False

        if not hero.end():

            world.background_group.draw(screen)
            world.ground_group.draw(screen)

            for platform in world.platform_group:
                if platform.rect.left - 50 < hero.rect.x < platform.rect.right + 50:
                    this_platform = platform.rect.y
                    hero.this_platform = platform
                    break
                else:
                    this_platform = 0

            for cage in world.cage_group:
                if cage.rect.left - 50 < hero.rect.x < cage.rect.right + 50:
                    hero.this_cage = cage
                    break

            hero.update(600 - hero.rect.height, this_platform - hero.rect.height)
            hero.action()
            hero.render()

            screen.blit(hero.image, hero.rect)
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
                        print(abs(enemy.rect.x - bullet.rect.x))
                        if abs(enemy.rect.x - bullet.rect.x) < 120:  #если рядом, то умерают вместе
                            enemy.health -= 1
                    bullets.remove(bullet)

            for enemy in world.enemy_group:
                if enemy.health <= 0:
                    world.enemy_group.remove(enemy)
                    enemy.alive_enemy = False
                enemy.update()
                enemy.action()

            print(hero.health)
            world.enemy_group.draw(screen)

            display.update()
        else:
            game_over.render()
            display.update()
        clock.tick(FPS)
quit()