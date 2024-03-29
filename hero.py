from pygame import *


class Hero(sprite.Sprite):
    def __init__(self, x, y, file, screen, group_platform, bullets, cage_group):
        sprite.Sprite.__init__(self)
        self.image = image.load(file).convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.screen = screen
        self.group_platform = group_platform
        self.bullets = bullets
        self.cage_group = cage_group

        self.walk_anim = ['wal1.png', 'wal2.png', 'wal3.png', 'wal4.png', 'wal5.png', 'wal6.png',
                          'wal7.png', 'wal8.png', 'wal9.png', 'wal10.png', 'wal11.png', 'wal12.png',
                          'wal13.png', 'wal14.png']

        self.jump_anim = ['jmp_1.png', 'jmp_2.png', 'jmp_3.png', 'jmp_4.png', 'jmp_5.png',
                          'jmp_6.png', 'jmp_7.png', 'jmp_8.png']

        self.attack_anim = ['attack_far1.png', 'attack_far2.png', 'attack_far3.png', 'attack_far4.png',
                            'attack_far5.png']

        self.run_x = 0
        self.run_y = 0
        self.attack_frame = 0
        self.player_frame = 0
        self.jump_frame = 0
        self.health = 50
        self.high_jump = -20
        self.this_platform = 0
        self.this_cage = 0
        self.cage_count = 0
        self.kill_count = 0

        self.all_sprites = None

        self.an_earth = False
        self.an_platform = False
        self.go = False
        self.jump = False
        self.left = False
        self.right = True
        self.attack = False
        self.can_left = True
        self.can_right = True
        self.over = False
        self.idle = True
        self.bullet_status = False
        self.can_scroll_right = False
        self.can_scroll_left = False
        self.win = False

        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self, *args):
        #движение
        self.can_left = True
        self.can_right = True
        self.rect.x += self.run_x
        self.rect.y += self.run_y
        self.an_earth = False
        self.idle = True

        if self.this_platform != 0:
            if self.this_platform.rect.colliderect(self.rect.x + self.run_x, self.rect.y, self.width, self.height):
                self.run_y = 0
                self.run_x = 0
                self.can_left = False
                self.can_right = False

                if not self.can_right and not self.can_left:
                    self.run_y += 0.9

                if self.rect.bottom + self.run_y > self.this_platform.rect.top + 2:
                    if self.rect.y - 23 < args[1]:
                        self.rect.y = args[1] + 2
                        self.run_y = 0

                        self.an_platform = True
                        self.an_earth = False
                        self.jump = False
                        self.can_left = True
                        self.can_right = True
            else:
                self.an_platform = False

        if not self.an_platform:
            if self.rect.y > args[0]:
                self.rect.y = args[0]
                self.run_y = 0

                self.an_earth = True
                self.jump = False

        self.end()
        self.shot()

        if not self.an_earth:
            self.run_y += 0.9

        self.run_x = 0

    def action(self):
        sense = key.get_pressed()
        if not self.over:
            if sense[K_SPACE]:
                self.attack = True
                self.bullet_status = True
                self.can_left = False
                self.can_right = False

            elif sense[K_LEFT] or sense[K_a]:
                if self.can_left:
                    if self.rect.x < 200:
                        self.can_scroll_right = True
                    else:
                        self.run_x -= 5
                    self.go = True
                    self.left = True
                    self.right = False
                    self.idle = False

            elif sense[K_RIGHT] or sense[K_d]:
                if self.can_right:
                    if self.rect.x > 1000:
                        self.can_scroll_left = True
                    else:
                        self.run_x += 5
                    self.go = True
                    self.left = False
                    self.right = True
                    self.idle = False

            elif sense[K_w] or sense[K_UP]:
                if self.an_earth or self.an_platform:
                    self.run_y = self.high_jump
                    self.an_earth = False
                    self.jump = True
                    self.idle = False

    def end(self):
        if self.health <= 0:
            self.over = True
            self.idle = False

    def shot(self):
        if self.bullet_status:
            for bullet in self.bullets:
                self.screen.blit(bullet.image, bullet.rect)
                bullet.move_bullets()

    def render(self):
        if self.right:
            file = 'right'

        elif self.left:
            file = 'left'

        if not self.jump:
            if self.go:
                self.player_frame += 0.2
                if self.player_frame > 14:
                    self.player_frame -= 14
                self.image = image.load(f'image/hero/{file}/{self.walk_anim[int(self.player_frame)]}'
                                        ).convert_alpha()
            elif self.idle:
                self.image = image.load(f'image/hero/{file}/peace.png').convert_alpha()
        else:
            self.jump_frame += 0.2
            if self.jump_frame > 7:
                self.jump_frame -= 7
            self.image = image.load(f'image/hero/{file}/jump/{self.jump_anim[int(self.jump_frame)]}'
                                    ).convert_alpha()

        if self.attack:
            self.attack_frame += 0.1
            if self.attack_frame > 5:
                self.attack = False
                if self.left:
                    bullet = Bullet(self.rect.left + 10, self.rect.centery, self.bullets, self.rect.left, self.left,
                                    self.right, file)
                else:
                    bullet = Bullet(self.rect.right - 10, self.rect.centery, self.bullets, self.rect.right, self.left,
                                    self.right, file)
                self.bullets.append(bullet)
                self.attack_frame -= 5
            self.image = image.load(f'image/hero/{file}/attack_far/{self.attack_anim[int(self.attack_frame)]}'
                                    ).convert_alpha()


class Bullet(sprite.Sprite):
    def __init__(self, x, y, bullets, hero_x, left, right, file):
        sprite.Sprite.__init__(self)
        self.image = image.load(f'image/hero/{file}/arrow.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.bullets = bullets
        self.distantion = 480
        self.hero_x = hero_x
        self.left = left
        self.right = right

    def move_bullets(self):
        for bullet in self.bullets:
            if self.left:
                bullet.rect.x -= 10
                if bullet.rect.x < self.hero_x - self.distantion:
                    self.bullets.remove(bullet)
            elif self.right:
                bullet.rect.x += 10
                if bullet.rect.x > self.hero_x + self.distantion:
                    self.bullets.remove(bullet)
