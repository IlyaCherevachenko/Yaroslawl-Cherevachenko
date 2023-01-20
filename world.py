from pygame import *
from enemy import Enemy
from environment import Background, Ground, Platform, Cage, Bomb
from hero import Hero


class World:
    def __init__(self, width, height, screen, bullets):
        self.all_sprites = sprite.Group()
        self.enemy_group = sprite.Group()
        self.ground_group = sprite.Group()
        self.platform_group = sprite.Group()
        self.hero_group = sprite.Group()
        self.cage_group = sprite.Group()
        self.bomb_group = sprite.Group()
        self.background_group = sprite.Group()

        self.width = width
        self.height = height
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
                      '                        pc                                            ',
                      '        p                                                      pk     ',
                      '                                                                      ',
                      '                                                                      ',
                      'gh                                        g                           ',
                      '               e    k       e                  e        k         e   ']

    def render_world(self):
        x, y = 0, 0
        keg_count = 0
        for row in self.level:
            for col in row:
                if col == 'b':
                    background = Background(x, y, self.screen)
                    self.background_group.add(background)
                elif col == 'p':
                    platform = Platform(self.screen, x, y)
                    self.platform_group.add(platform)
                elif col == 'g':
                    ground = Ground(x, y + 50, self.screen)
                    self.ground_group.add(ground)
                elif col == 'c':
                    cage = Cage(x, platform.rect.top - 35)
                    self.cage_group.add(cage)
                elif col == 'h':
                    hero = Hero(x, y, 'image/hero/right/peace.png', self.screen, self.platform_group,
                                self.bullets, self.cage_group)
                    self.hero_group.add(hero)
                elif col == 'e':
                    enemy = Enemy(x, ground.rect.top - 62, 'image/enemy/right/idle/peace1.png', self.screen,
                                  self.hero_group)
                    self.enemy_group.add(enemy)
                elif col == 'k':
                    if keg_count < 2:
                        bomb = Bomb(x, platform.rect.top)
                    else:
                        bomb = Bomb(x, ground.rect.top)
                    keg_count += 1
                    self.bomb_group.add(bomb)
                x += self.width_block
            y += self.height_block
            x = 0