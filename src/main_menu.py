from abc import abstractmethod, ABC
import pygame
import pygame.freetype

from game_base import Game


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
    def __init__(self, parent, return_callback):
        super().__init__(parent, return_callback)
        self.red = 0
        self.count = 3

    def display(self):
        self.parent.surface.fill((self.red, 0, 0))

    def handle_event(self, event) -> None:
        pass

    def update(self) -> None:
        self.red += 1
        self.red %= 256
        if self.red == 0:
            self.count -= 1
        if self.count is 0:
            self.return_to_main_menu()

    def selected_game(self) -> Game:
        return None

class MainMenu(Game):
    def __init__(self):
        super().__init__(show_menu_bar=False)
        self.font = pygame.freetype.Font("./fonts/NotoSansCJKjp-Regular.otf")

        def return_callback(): self._change_state(None)
        self.mini_game_select_delegate = MiniGameSelectMenu(self, return_callback)

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

    def _change_state(self, delegate):
        if delegate is not None:
            self.delegate = delegate
        else:
            self.delegate = self.main_menu

    def selected_game(self):
        if self.delegate is not self.mini_game_select_delegate:
            return None
        else:
            return self.delegate.selected_game()
