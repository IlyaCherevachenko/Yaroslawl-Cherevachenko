from pygame import *
import sys

size = w, h = 800, 600


class Menu:
    def __init__(self, screen):
        self.name_options = []
        self.actions = []
        self.select_id = 0
        self.screen = screen

    def option_add(self, option, action):
        self.name_options.append(Arial_50.render(option, True, 'white'))
        self.actions.append(action)

    def selector(self, status):
        self.select_id = abs((self.select_id + status) % 3)

    def select(self):
        self.actions[self.select_id]()

    def draw(self, y, padding):
        for numb, option in enumerate(self.name_options):

            option_rect = option.get_rect(center=(w//2, h//2))
            option_rect.y = y + numb * padding

            if numb == self.select_id:
                draw.rect(self.screen, 'orange', option_rect)

            self.screen.blit(option, option_rect)


class Stop(sprite.Sprite):
    def __init__(self):
        super().__init__()


class Game_over(sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image_over = image.load('image/menu/game_over.png').convert_alpha()
        self.rect_over = self.image_over.get_rect(center=(600, 150))
        self.screen = screen

    def render(self):
        self.screen.fill('black')
        self.screen.blit(self.image_over, self.rect_over)


if __name__ == '__main__':
    init()

    screen = display.set_mode(size)
    Arial_50 = font.SysFont('arial', 50)

    running = True

    menu = Menu(screen)
    menu.option_add('Играть', lambda: print('Типо игра'))
    menu.option_add('Настройки', lambda: print('Типо настройки'))
    menu.option_add('Выход', sys.exit)

    while running:
        for value in event.get():
            if value.type == QUIT:
                running = False
            elif value.type == KEYDOWN:
                if value.key == K_w or value.key == K_UP:
                    menu.selector(-1)
                elif value.key == K_s or value.key == K_DOWN:
                    menu.selector(1)
                elif value.key == K_SPACE or value.key == K_RETURN:
                    menu.select()

        screen.fill('blue')
        menu.draw(100, 100)
        display.flip()
    quit()
