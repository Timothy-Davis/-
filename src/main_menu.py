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
    def __init__(self):
        super().__init__(show_menu_bar=False)
        self.font = pygame.freetype.Font("./fonts/NotoSansCJKjp-Regular.otf")
        self.title = '日本語のミニゲイム'
        self.menu_options = ["Mini Games", "Credits", "Scores"]

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

        self.option_surfaces = [make_font_surface(option) for option in self.menu_options]

    def display(self):
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.title_surface, (self.title_x, self.title_y))
        y_offset = 0
        for surface in self.option_surfaces:
            y = MENU_Y_PERCENTAGE * self.surface.get_height() + y_offset
            x = self.surface.get_width()/2 - surface.get_width()/2
            self.surface.blit(surface, (x, y))
            y_offset += surface.get_height() + MENU_OPTION_OFFSET


    def handle_event(self, event) -> None:
        print(event)
        pass

    def update(self):
        pass
