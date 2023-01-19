from pygame import *


class Background(sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = image.load('image/environ/background1.png')

        self.x = 0
        self.y = 0

        self.screen_surf = screen

    def render(self):
        self.screen_surf.blit(self.image, (self.x, self.y))


class Cage(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = image.load('image/environ/cage/cage_with_bird.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))


class Bomb(sprite.Sprite):
    def __init__(self, x, y, hero_group, hero):
        super().__init__()
        self.image = image.load('image/environ/traps/bomb/bomb1.png')
        self.rect = self.image.get_rect(center=(x, y))

        self.boom_anim = ['bomb2.png', 'bomb3.png', 'bomb4.png']
        self.hero_group = hero_group
        self.hero = hero

        self.boom = False

        self.boom_frame = 0
        self.distantion = 50

    def render(self):
        if sprite.spritecollide(self, self.hero_group, False):
            self.boom = True

        if self.boom:
            self.boom_frame += 0.1
            if self.boom_frame < 3:
                self.image = image.load(f'image/environ/traps/bomb/{self.boom_anim[int(self.boom_frame)]}')
            else:
                if self.rect.left - self.distantion < self.hero.rect.x < self.rect.right + self.distantion and self.hero.rect.bottom > self.rect.top + self.distantion and self.boom:
                    self.hero.health -= self.hero.health


class Ground(sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = image.load('image/environ/ground.png')
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect(center=(350, 690))

        self.screen_surf = screen

    def render(self):
        self.screen_surf.blit(self.image, (self.rect.x, self.rect.y))


class Platform(sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.image = image.load('image/environ/2.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.screen_surf = screen

    def render(self):
        self.screen_surf.blit(self.image, (self.rect.x, self.rect.y))
