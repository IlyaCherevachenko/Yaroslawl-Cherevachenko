from pygame import *
from enemy import Enemy
from environment import Background, Ground, Platform, Cage, Bomb
from hero import Hero


class World:
    def __init__(self, screen, bullets):
        self.all_sprites = sprite.Group()
        self.enemy_group = sprite.Group()
        self.ground_group = sprite.Group()
        self.platform_group = sprite.Group()
        self.hero_group = sprite.Group()
        self.cage_group = sprite.Group()
        self.bomb_group = sprite.Group()
        self.background_group = sprite.Group()
        self.all_sprites = sprite.Group()

        self.screen = screen
        self.bullets = bullets

        self.width_block = 50
        self.height_block = 50

        self.level = ['b                      b                      b                       ',
                      '                                                                      ',
                      '                                                                      ',
                      '                                       pc                             ',
                      '                                                                      ',
                      '               p                pk                       pc           ',
                      '                                                                      ',
                      '                       pc                     pc                      ',
                      '        p                                                      pk     ',
                      'b                      b                       b                      ',
                      '                                P                                     ',
                      '              p                                        P              ',
                      '                                                                      ',
                      '                                                                      ',
                      'gh                                        g                           ',
                      '               e    k       e        e         e        k         e   ']

    def render_world(self):
        x, y = 0, 0
        keg_count = 0
        for row in self.level:
            for col in row:
                if col == 'b':
                    background = Background(x, y, self.screen)
                    self.background_group.add(background)
                    self.all_sprites.add(background)
                elif col == 'p':
                    platform = Platform('image/environ/platform.png', self.screen, x, y)
                    self.platform_group.add(platform)
                    self.all_sprites.add(platform)
                elif col == 'P':
                    platform = Platform('image/environ/big_platform.png', self.screen, x, y)
                    self.platform_group.add(platform)
                    self.all_sprites.add(platform)
                elif col == 'g':
                    ground = Ground(x, y + 50, self.screen)
                    self.ground_group.add(ground)
                    self.all_sprites.add(ground)
                elif col == 'c':
                    cage = Cage(x, platform.rect.top - 35)
                    self.cage_group.add(cage)
                    self.all_sprites.add(cage)
                elif col == 'h':
                    hero = Hero(x, y, 'image/hero/right/peace.png', self.screen, self.platform_group,
                                self.bullets, self.cage_group)
                    self.hero_group.add(hero)
                elif col == 'e':
                    enemy = Enemy(x, ground.rect.top - 62, 'image/enemy/right/idle/peace1.png', self.screen,
                                  self.hero_group)
                    self.enemy_group.add(enemy)
                    self.all_sprites.add(enemy)
                elif col == 'k':
                    if keg_count < 2:
                        bomb = Bomb(x, platform.rect.top)
                    else:
                        bomb = Bomb(x, ground.rect.top)
                    keg_count += 1
                    self.bomb_group.add(bomb)
                    self.all_sprites.add(bomb)
                x += self.width_block
            y += self.height_block
            x = 0

    def clean_world(self):
        self.platform_group.remove(plat for plat in self.platform_group)
        self.enemy_group.remove(enemy for enemy in self.enemy_group)
        self.cage_group.remove(cage for cage in self.cage_group)
        self.bomb_group.remove(bomb for bomb in self.bomb_group)
        self.hero_group.remove(hero for hero in self.hero_group)
        self.background_group.remove(bg for bg in self.background_group)
        self.ground_group.remove(gr for gr in self.ground_group)
