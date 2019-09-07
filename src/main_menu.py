import typing
from abc import abstractmethod, ABC
import pygame
import pygame.freetype
import simple_ui

from game_base import Game, GameInfo, SWAP_GAME, END_GAME


class _MenuOption:
    def __init__(self, surface, x, y, callback, callback_argument):
        self.x = x
        self.y = y
        self.surface = surface
        self.callback = callback
        self.callback_argument = callback_argument

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


class MainMenuDelegate(ABC):
    def __init__(self, parent, return_callback):
        self.return_callback = return_callback
        self.parent = parent
        self.has_event: bool = False
        self.event: pygame.event.Event = None

    @abstractmethod
    def display(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def handle_event(self, event) -> None:
        pass

    def return_to_main_menu(self) -> None:
        self.return_callback()


class NormalMainMenu(MainMenuDelegate):
    TITLE_Y_PERCENTAGE = .20
    TITLE_FONT_SIZE = 48
    MENU_Y_PERCENTAGE = .50
    MENU_OPTION_OFFSET = 10
    MENU_FONT_SIZE = 24

    def __init__(self, parent, return_callback, menu_options):
        super().__init__(parent, return_callback)
        self.title = '日本語のミニゲイム'

        font_options = {
            'fgcolor': (255, 255, 255),
            'bgcolor': (0, 0, 0),
            'style': pygame.freetype.STYLE_DEFAULT,
            'rotation': 0,
            'size': self.TITLE_FONT_SIZE,
        }
        def make_font_surface(text): return self.parent.font.render(text, **font_options)[0]

        self.title_surface = make_font_surface(self.title)

        font_options['size'] = self.MENU_FONT_SIZE
        self.title_x = self.parent.surface.get_width() / 2 - self.title_surface.get_width() / 2
        self.title_y = self.TITLE_Y_PERCENTAGE * self.parent.surface.get_height()

        y_offset = 0
        self.options = []
        for option in menu_options:
            surface = make_font_surface(option[0])
            y = self.MENU_Y_PERCENTAGE * self.parent.surface.get_height() + y_offset
            x = self.parent.surface.get_width()/2 - surface.get_width()/2
            y_offset += surface.get_height() + self.MENU_OPTION_OFFSET
            menu_option = _MenuOption(surface, x, y, option[1], option[2])
            self.options.append(menu_option)

    def display(self):
        self.parent.surface.fill((0, 0, 0))
        self.parent.surface.blit(self.title_surface, (self.title_x, self.title_y))
        for option in self.options:
            self.parent.surface.blit(option.surface, (option.x, option.y))

    def handle_event(self, event) -> None:
        if event.type is pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for option in self.options:
                if option.collision(x, y):
                    option.callback(option.callback_argument)

    def update(self):
        pass


class MiniGameSelectMenu(MainMenuDelegate):
    GAME_FONT_SIZE = 36
    GAME_HEIGHT_PERCENT = .25
    GAME_WIDTH_PERCENT = .30
    GAME_MIN_X_PERCENT = .03
    GAME_MIN_Y_PERCENT = .25/4

    def __init__(self, parent, return_callback, mini_games: typing.List[GameInfo]):
        super().__init__(parent, return_callback)
        self.game_width = self.GAME_WIDTH_PERCENT * self.parent.surface.get_width()
        self.game_height = self.GAME_HEIGHT_PERCENT * self.parent.surface.get_height()
        self.game: typing.Optional[GameInfo] = None
        self.mini_games: typing.List[typing.Tuple[pygame.Rect, GameInfo]] = []

        self.ui_items: typing.List[simple_ui.SimpleUIElement] = []
        x = self.GAME_MIN_X_PERCENT * self.parent.surface.get_width()
        y = self.GAME_MIN_Y_PERCENT * self.parent.surface.get_height()
        for game in mini_games:
            item: simple_ui.SpinnerBox = simple_ui.SpinnerBox(x, y, 0, 0, 100)
            item.add_value_change_callback(lambda thing: print(f'Value changed to {thing.value}!'))
            self.ui_items.append(item)
            # game_rect = pygame.Rect(x, y, self.game_width, self.game_height)
            # self.mini_games.append((game_rect, game))
            x += self.GAME_WIDTH_PERCENT*self.parent.surface.get_width() + 20
            y += self.GAME_HEIGHT_PERCENT*self.parent.surface.get_height() + 20

    # def _draw_game_box(self, x, y, game_title):
        # game_rect = pygame.Rect(x, y, self.game_width, self.game_height)
        # pygame.draw.rect(self.parent.surface, (255, 255, 255), game_rect)
        # game_rect.x += 2
        # game_rect.y += 2
        # game_rect.width -= 4
        # game_rect.height -= 4
        # pygame.draw.rect(self.parent.surface, (0, 0, 0), game_rect)
        #
        # # TODO: We have code duplication here. This entire module could really do with some refactoring later.
        # font_options = {
        #     'fgcolor': (255, 255, 255),
        #     'bgcolor': (0, 0, 0),
        #     'style': pygame.freetype.STYLE_DEFAULT,
        #     'rotation': 0,
        #     'size': self.GAME_FONT_SIZE
        # }
        # font_surface = self.parent.font.render(game_title, **font_options)[0]
        #
        # x = self.game_width/2 - font_surface.get_width()/2 + x
        # y = self.game_height/2 - font_surface.get_height()/2 + y
        # self.parent.surface.blit(font_surface, (x, y))

    def display(self):
        self.parent.surface.fill((0, 0, 0))
        for item in self.ui_items:
            self.parent.surface.blit(item.draw_self(), (item.x, item.y))
        # self.parent.surface.fill((0, 0, 0))
        # for game in self.mini_games:
        #     self._draw_game_box(game[0].x, game[0].y, game[1].title)

    def handle_event(self, event) -> None:
        for item in self.ui_items:
            item.handle_event(event)
        # if event.type is pygame.MOUSEBUTTONDOWN:
        #     # for game in self.mini_games:
        #     #     if game[0].collidepoint(event.pos):
        #     #         self.game = game[1]

    def update(self) -> None:
        if self.game is not None:
            self.has_event = True
            data = {
                'new_game': self.game
            }
            self.event = pygame.event.Event(SWAP_GAME, data)


class MainMenu(Game):
    def __init__(self, available_games: typing.List[GameInfo]):
        super().__init__(show_menu_bar=False)
        self.font = pygame.freetype.Font("./fonts/NotoSansCJKjp-Regular.otf")

        def return_callback(): self._change_state(None)
        self.mini_game_select_delegate = MiniGameSelectMenu(self, return_callback, available_games)

        menu_options = [
            ("Mini Games", self._change_state, self.mini_game_select_delegate),
            ("Credits", self._change_state, None),
            ("Scores", self._change_state, None),
        ]

        self.main_menu = NormalMainMenu(self, None, menu_options)
        self.delegate = self.main_menu

    def display(self):
        self.delegate.display()

    def handle_event(self, event) -> None:
        self.delegate.handle_event(event)

    def update(self):
        self.delegate.update()
        if self.delegate.has_event:
            self.emit_event(self.delegate.event)

    def title(self):
        return 'Main Menu'

    def _change_state(self, delegate):
        if delegate is not None:
            self.delegate = delegate
        else:
            self.delegate = self.main_menu

    @classmethod
    def info(cls) -> typing.Optional[GameInfo]:
        return GameInfo("Main Menu", cls, None, img=None)
