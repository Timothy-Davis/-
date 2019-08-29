import pygame
import pygame.freetype
from pygame.freetype import Font

import game_base
from game_base import Game

TITLE_Y_PERCENTAGE = .20
TITLE_FONT_SIZE = 48
MENU_Y_PERCENTAGE = .50
MENU_OPTION_OFFSET = 10
MENU_FONT_SIZE = 24


class MainMenu(Game):
    class _MenuOption:  # Nested Class because it isn't meant to be used anywhere else
        def __init__(self, surface, x, y, callback):
            self.x = x
            self.y = y
            self.surface = surface
            self.callback = callback

        def collision(self, x, y) -> bool:
            if x < self.x:
                return False
            if y < self.y:
                return False
            if x > self.x + self.surface.get_width():
                return False
            if y > self.y + self.surface.get_height():
                return False
            return True

    def __init__(self):
        super().__init__(show_menu_bar=False)
        self.font = pygame.freetype.Font("./fonts/NotoSansCJKjp-Regular.otf")
        self.title = '日本語のミニゲイム'

        fgcolor = (255, 255, 255)
        bgcolor = (0, 0, 0)
        style = pygame.freetype.STYLE_DEFAULT
        rotation = 0
        size = TITLE_FONT_SIZE
        def make_font_surface(text): return self.font.render(text, fgcolor, bgcolor, style, rotation, size)[0]

        self.title_surface = make_font_surface(self.title)

        size = MENU_FONT_SIZE
        self.title_x = self.surface.get_width() / 2 - self.title_surface.get_width() / 2
        self.title_y = TITLE_Y_PERCENTAGE * self.surface.get_height()

        self.options = []
        menu_options = [('Main Menu', self.handle_main_menu),
                        ('Credits', self.handle_credits),
                        ('Scores', self.handle_scores)]
        y_offset = 0
        for option in menu_options:
            surface = make_font_surface(option[0])
            y = MENU_Y_PERCENTAGE * self.surface.get_height() + y_offset
            x = self.surface.get_width()/2 - surface.get_width()/2
            y_offset += surface.get_height() + MENU_OPTION_OFFSET
            menu_option = self._MenuOption(surface, x, y, option[1])
            self.options.append(menu_option)

    def display(self):
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.title_surface, (self.title_x, self.title_y))
        for option in self.options:
            self.surface.blit(option.surface, (option.x, option.y))

    def handle_event(self, event) -> None:
        if event.type is pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for option in self.options:
                if option.collision(x, y):
                    option.callback()

        pass

    def update(self):
        pass

    def handle_main_menu(self):
        print("Main Menu Clicked")

    def handle_scores(self):
        print("Scores Clicked")

    def handle_credits(self):
        print("Credits Clicked")
