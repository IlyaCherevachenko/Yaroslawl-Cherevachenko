from pygame import *
from sys import exit


def print_back_menu(x, y, screen):
    if 205 < x < 995 and 685.5 < y < 721.5:
        image_button = image.load('image/menu/game over/button1.png').convert_alpha()
        rect_button = image_button.get_rect(center=(600, 690))
    else:
        image_button = image.load('image/menu/game over/button2.png').convert_alpha()
        rect_button = image_button.get_rect(center=(600, 690))
    screen.blit(image_button, rect_button)


class Menu:
    def __init__(self, screen, width, height):
        self.image_button = ['button1.png', 'button2.png', 'button3.png']
        self.image_name = image.load('image/menu/name.png').convert_alpha()
        self.image_hero_bg = image.load('image/menu/hero_bg.png').convert_alpha()
        self.image_bird_bg = image.load('image/menu/bird.png').convert_alpha()
        self.music_play = mixer.Sound('sounds/play/bingo_bass_background_music.wav')
        self.width = width
        self.height = height
        self.rect = self.image_name.get_rect(center=(self.width // 2, 100))
        self.rect_hero_bg = self.image_hero_bg.get_rect(center=(1000, 500))
        self.rect_bird_bg = self.image_bird_bg.get_rect(center=(200, 500))
        self.screen = screen

        self.menu_sound = True
        self.menu = True

    def render(self):
        x, y = mouse.get_pos()
        padding_count = 0
        padding = 150

        self.screen.fill('black')
        self.screen.blit(self.image_bird_bg, self.rect_bird_bg)
        self.screen.blit(self.image_hero_bg, self.rect_hero_bg)
        self.screen.blit(self.image_name, self.rect)

        for i in range(len(self.image_button)):
            image_button = image.load(f'image/menu/buttons/{self.image_button[i]}').convert_alpha()
            rect_button = image_button.get_rect(center=(self.width // 2, 345 + padding * padding_count))
            if rect_button.left < x < rect_button.right and rect_button.top < y < rect_button.bottom:
                image_button = image.load(f'image/menu/buttons_click/{self.image_button[i]}').convert_alpha()
                rect_button = image_button.get_rect(center=(self.width // 2, 345 + padding * padding_count))
            padding_count += 1
            self.click()
            self.screen.blit(image_button, rect_button)

        if not self.menu:
            self.music_play.play(-1)

    def click(self):
        x, y = mouse.get_pos()
        if mouse.get_pressed()[0] and 298.5 < y < 391.5 and 497 < x < 703:
            self.menu = False
            self.menu_sound = False
            return self.menu

        elif mouse.get_pressed()[0] and 442.5 < y < 547.5 and 410 < x < 790:
            print('settings')

        elif mouse.get_pressed()[0] and 606 < y < 685.5 and 503.5 < x < 696.5:
            exit()


class Gameover:
    def __init__(self, screen):
        self.image_over = image.load('image/menu/game over/game_over.png').convert_alpha()
        self.sound_over = mixer.Sound('sounds/game_over/mixkit-player-losing-or-failing-2042.wav')
        self.rect_over = self.image_over.get_rect(center=(600, 325))
        self.screen = screen
        self.game_over = True
        self.play_over = True

    def render(self):
        x, y = mouse.get_pos()
        self.screen.fill('black')
        self.screen.blit(self.image_over, self.rect_over)
        print_back_menu(x, y, self.screen)
        if self.play_over:
            self.sound_over.play()
            self.play_over = False
        self.click()

    def click(self):
        x, y = mouse.get_pos()
        if mouse.get_pressed()[0] and 658.5 < y < 721.5 and 205 < x < 995:
            self.game_over = False
            self.play_over = True
            return True


class Win:
    def __init__(self, screen):
        self.image_cong = image.load('image/menu/win/congratulations.png')
        self.win_sond = mixer.Sound('sounds/winner/mixkit-game-level-completed-2059.wav')
        self.rect = self.image_cong.get_rect(center=(600, 300))
        self.screen = screen
        self.win_sound_play = True

        self.win_anim = ['you_win1.png', 'you_win2.png', 'you_win3.png', 'you_win4.png', 'you_win5.png']

        self.count_frame = 0

    def render(self):
        x, y = mouse.get_pos()

        self.screen.fill('pink')
        self.screen.blit(self.image_cong, self.rect)
        self.count_frame += 0.2

        if self.count_frame > 5:
            self.count_frame -= 5

        image_win = image.load(f'image/menu/win/{self.win_anim[int(self.count_frame)]}')
        rect = image_win.get_rect(center=(600, 380))

        self.screen.blit(image_win, rect)
        if self.win_sound_play:
            self.win_sond.play()
            self.win_sound_play = False

        print_back_menu(x, y, self.screen)
        self.click()

    def click(self):
        x, y = mouse.get_pos()
        if mouse.get_pressed()[0] and 658.5 < y < 721.5 and 205 < x < 995:
            self.win_sound_play = True
            return True


class Pause:
    def __init__(self, screen):
        self.screen = screen
        self.pause_status = False
        self.image = image.load('image/menu/pause/pause.png')
        self.rect = self.image.get_rect(center=(600, 300))

    def render(self):
        x, y, = mouse.get_pos()

        draw.rect(self.screen, (124, 113, 216), (300, 200, 600, 450))
        self.screen.blit(self.image, self.rect)

        if 468 < x < 731 and 457 < y < 504:
            image_button_cont = image.load('image/menu/pause/button4.png').convert_alpha()
            rect_button_cont = image_button_cont.get_rect(center=(600, 480))
        else:
            image_button_cont = image.load('image/menu/pause/button3.png').convert_alpha()
            rect_button_cont = image_button_cont.get_rect(center=(600, 480))

        if 347 < x < 853 and 551 < y < 588:
            image_button = image.load('image/menu/pause/button1.png').convert_alpha()
            rect_button = image_button.get_rect(center=(600, 570))
        else:
            image_button = image.load('image/menu/pause/button2.png').convert_alpha()
            rect_button = image_button.get_rect(center=(600, 570))

        self.screen.blit(image_button_cont, rect_button_cont)
        self.screen.blit(image_button, rect_button)
        self.click()

    def click(self):
        x, y = mouse.get_pos()
        if mouse.get_pressed()[0] and 459 < y < 501 and 474 < x < 731:
            self.pause_status = False
        elif mouse.get_pressed()[0] and 554 < y < 587 and 362 < x < 853:
            return True
