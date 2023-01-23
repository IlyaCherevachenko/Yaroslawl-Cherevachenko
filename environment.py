from pygame import *


class Background(sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.image = image.load('image/environ/background1.png')
        self.rect = self.image.get_rect(topleft=(x, y))

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
    def __init__(self, x, y):
        super().__init__()
        self.image = image.load('image/environ/traps/bomb/bomb1.png')
        self.rect = self.image.get_rect(center=(x, y - 35))

        self.boom_anim = ['bomb2.png', 'bomb3.png', 'bomb4.png']
        self.boom_sound = mixer.Sound('sounds/play/rumble.wav')

        self.hero_group = None
        self.hero = None

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
                if int(self.boom_frame) == 2:
                    self.boom_sound.play()
                    if (self.rect.left - self.distantion < self.hero.rect.x < self.rect.right + self.distantion
                            and self.hero.rect.bottom > self.rect.top + self.distantion and self.boom):
                        self.hero.health = 0


class Ground(sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.image = image.load('image/environ/ground.png')
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect(topleft=(x, y))

        self.screen_surf = screen

    def render(self):
        self.screen_surf.blit(self.image, (self.rect.x, self.rect.y))


class Platform(sprite.Sprite):
    def __init__(self, file, screen, x, y):
        super().__init__()
        self.image = image.load(file)
        self.rect = self.image.get_rect(center=(x, y))
        self.screen_surf = screen

    def render(self):
        self.screen_surf.blit(self.image, (self.rect.x, self.rect.y))


class Score(sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def render_cage_score(self, cage_count):
        image_cage = image.load(f'image/environ/cage count/count{cage_count}.png')
        rect_cage = image_cage.get_rect(topleft=(10, 10))
        self.screen.blit(image_cage, rect_cage)

    def render_kill_score(self, kill_count):
        image_kill = image.load(f'image/environ/kill count/count{kill_count}.png')
        rect_kill = image_kill.get_rect(topleft=(10, 58))
        self.screen.blit(image_kill, rect_kill)


class Healthbar(sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def render(self, health):
        if 45 <= health <= 50:
            image_health = image.load(f'image/environ/health_bar/health_bar1.png')
        elif 40 <= health <= 44:
            image_health = image.load(f'image/environ/health_bar/health_bar2.png')
        elif 35 <= health <= 39:
            image_health = image.load(f'image/environ/health_bar/health_bar3.png')
        elif 30 <= health <= 34:
            image_health = image.load(f'image/environ/health_bar/health_bar4.png')
        elif 25 <= health <= 29:
            image_health = image.load(f'image/environ/health_bar/health_bar5.png')
        elif 20 <= health <= 24:
            image_health = image.load(f'image/environ/health_bar/health_bar6.png')
        elif 15 <= health <= 19:
            image_health = image.load(f'image/environ/health_bar/health_bar7.png')
        elif 10 <= health <= 14:
            image_health = image.load(f'image/environ/health_bar/health_bar8.png')
        elif 5 <= health <= 9:
            image_health = image.load(f'image/environ/health_bar/health_bar9.png')
        elif 1 <= health <= 4:
            image_health = image.load(f'image/environ/health_bar/health_bar10.png')
        if int(health) > 0:
            rect_health = image_health.get_rect(topright=(1190, 10))
            self.screen.blit(image_health, rect_health)
