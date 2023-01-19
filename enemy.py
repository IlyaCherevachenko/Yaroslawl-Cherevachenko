from pygame import *


class Enemy(sprite.Sprite):
    def __init__(self, x, y, file, screen, hero, hero_group):
        sprite.Sprite.__init__(self)
        self.image = image.load(file).convert_alpha()

        self.rect = self.image.get_rect(center=(x, y))
        self.screen = screen
        self.hero = hero
        self.hero_group = hero_group
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.walk = ['walk1.png', 'walk2.png', 'walk3.png', 'walk4.png', 'walk5.png']
        self.idle = ['peace1.png', 'peace2.png', 'peace3.png', 'peace4.png']
        self.attack = ['attack1.png', 'attack2.png', 'attack3.png', 'attack4.png']

        self.walk_frame = 0
        self.attack_idle_frame = 0
        self.distantion = 300
        self.health = 7

        self.right = False
        self.left = True
        self.go = False
        self.idling = False
        self.go_attack = False

    def update(self):
        if self.right:
            file = 'right'

        elif self.left:
            file = 'left'

        if self.go:
            self.walk_frame += 0.1
            if self.walk_frame > 5:
                self.walk_frame -= 5
            self.image = image.load(f'image/enemy/{file}/walk/{self.walk[int(self.walk_frame)]}'
                                    ).convert_alpha()
        elif self.go_attack:
            self.attack_idle_frame += 0.1
            if self.attack_idle_frame > 4:
                self.attack_idle_frame -= 4
                self.hero.health -= 3
            self.image = image.load(f'image/enemy/{file}/attack/{self.attack[int(self.attack_idle_frame)]}'
                                    ).convert_alpha()
        else:
            self.attack_idle_frame += 0.1
            if self.attack_idle_frame > 4:
                self.attack_idle_frame -= 4
            self.image = image.load(f'image/enemy/{file}/idle/{self.idle[int(self.attack_idle_frame)]}').convert_alpha()

    def action(self):
        self.go = False
        self.go_attack = False

        #нужно сделать проще
        if (self.rect.left - self.distantion < self.hero.rect.centerx < self.rect.right) and not self.hero.an_platform:
            self.left = True
            self.right = False
            if sprite.spritecollide(self, self.hero_group, False):
                self.go = False
                self.go_attack = True
            else:
                self.rect.x -= 2
                self.go = True

        elif not self.hero.an_platform and (self.rect.left < self.hero.rect.centerx < self.rect.right + self.distantion):
            self.left = False
            self.right = True
            if sprite.spritecollide(self, self.hero_group, False):
                self.go = False
                self.go_attack = True
            else:
                self.rect.x += 2
                self.go = True
