from pygame import *
from hero import Hero
from enemy import Enemy
from environment import Background, Ground, Platform, Cage, Bomb
from menu import Menu, Game_over

size = width, height = 1200, 720
FPS = 60
bullets = []

if __name__ == '__main__':
    init()
    screen = display.set_mode(size)
    display.set_caption('BossFight')
    display.set_icon(image.load('image/icon/icon2.png'))
    Arial_50 = font.SysFont('arial', 50)
    clock = time.Clock()

    background = Background(screen)
    ground = Ground(screen)

    #нужно упростить установку добавлением платформ append с выставленным x, y (отделный класс world)
    platform = Platform(screen, 440, 440) #Platform(screen, 740, 330)
    cage = Cage(platform.rect.top, platform.rect.y - 34)
    game_over = Game_over(screen)

    enemy_group = sprite.Group()
    ground_group = sprite.Group()
    platform_group = sprite.Group()
    hero_group = sprite.Group()
    cage_group = sprite.Group()
    bomb_group = sprite.Group()

    ground_group.add(ground)
    platform_group.add(platform)
    cage_group.add(cage)
    hero = Hero(30, 600, 'image/hero/right/peace.png', screen, platform_group, platform, bullets, cage_group)
    hero_group.add(hero)
    enemy = Enemy(700, ground.rect.top - 62, 'image/enemy/right/idle/peace1.png', screen, hero, hero_group)
    enemy_group.add(enemy)
    bomb = Bomb(ground.rect.top, ground.rect.y - 38, hero_group, hero)
    bomb_group.add(bomb)

    running = True

    while running:
        for value in event.get():
            if value.type == QUIT:
                running = False
            elif value.type == KEYUP:
                hero.go = False

        if not hero.end():
            background.render()
            ground.render()

            hero.update(ground.rect.y - hero.rect.height, platform.rect.y - hero.rect.height)
            hero.action()
            hero.render()

            screen.blit(hero.image, hero.rect)
            platform_group.draw(screen)
            cage_group.draw(screen)
            bomb_group.draw(screen)
            bomb.render()
            if bomb.boom_frame > 3:
                bomb_group.remove(bomb)
                bomb.boom = False

            print(bomb.boom)

            for bullet in bullets:
                if sprite.spritecollide(bullet, enemy_group, False):
                    enemy.health -= 1
                    bullets.remove(bullet)
            if enemy.health <= 0:
                enemy_group.remove(enemy)

            enemy.update()
            enemy.action()
            enemy_group.draw(screen)

            display.update()
        else:
            game_over.render()
            display.update()
        clock.tick(FPS)
quit()