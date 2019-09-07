from abc import ABC, abstractmethod

import constants
import pygame
import pygame.freetype
pygame.init()
pygame.freetype.init(resolution=72)


class SimpleUIElement(ABC):
    def __init__(self, x: int, y: int, width: int, height: int):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._click_callbacks = []

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if x < 0:
            x = 0
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if y < 0:
            y = 0
        self._y = y

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width < 0:
            width = 1
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height < 0:
            height = 1
        self._height = height

    @property
    def pos(self):
        return self.x, self.y

    @property
    def collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def move_to(self, x: int, y: int):
        self.x = x
        self.y = y

    def add_on_click_callback(self, callback):
        self._click_callbacks.append(callback)

    def remove_on_click_callback(self, callback):
        self._click_callbacks.remove(callback)

    def handle_event(self, event: pygame.event.Event):
        """
        Handles a generic pygame event. The base class only handles the event for things such as click callbacks.
        :warning: If you override this method, be sure to call super().handle_event somewhere in your code unless you
                  want to fiddle with the coordinates yourself. This method changes the event's coordinates to local
                  coordinates for ease of use.
        :param event:
        :return:
        """
        if event.type is pygame.MOUSEBUTTONDOWN:
            if self.collision_rect.collidepoint(event.pos[0], event.pos[1]):
                for callback in self._click_callbacks:
                    callback(self)
            event.pos = event.pos[0]-self.x, event.pos[1]-self.y

    @abstractmethod
    def draw_self(self) -> pygame.Surface:
        pass


class Label(SimpleUIElement):
    def __init__(self, text: str, x: int, y: int, **kwargs):
        super().__init__(x, y, 1, 1)
        self.font_options = {
                             'size': kwargs.get('font_size', constants.DEFAULT_FONT_SIZE),
                             'fgcolor': kwargs.get('fgcolor', constants.DEFAULT_FONT_OPTIONS['fgcolor']),
                             'bgcolor': kwargs.get('bgcolor', constants.DEFAULT_FONT_OPTIONS['bgcolor']),
                             'style': kwargs.get('style', constants.DEFAULT_FONT_OPTIONS['style']),
                             'rotation': kwargs.get('rotation', constants.DEFAULT_FONT_OPTIONS['rotation'])
                            }
        print(f"INITIALIZED WITH FONT SIZE: {self.font_options['size']}")
        self.font = kwargs.get('font', constants.DEFAULT_GAME_FONT)
        self.text = text
        self.surface = self.font.render(self.text, **self.font_options)[0]
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

    def draw_self(self) -> pygame.Surface:
        return self.surface


class Button(SimpleUIElement):
    def __init__(self, text: str, x: int, y: int, **kwargs):
        super().__init__(x, y, 0, 0)
        self.options = {
            'border': kwargs.get('border', True),
            'border_width': kwargs.get('border_width', 2),
            'padding': kwargs.get('padding', 10),
            'margin': kwargs.get('margin', 2),
            'fgcolor': kwargs.get('fgcolor', (255, 255, 255)),
            'bgcolor': kwargs.get('bgcolor', (0, 0, 0)),
            'border_color': kwargs.get('border_color', (255, 255, 255)),
            'font_size': kwargs.get('font_size', constants.DEFAULT_FONT_SIZE)
        }
        self.text = text
        text_subsurface = Label(text, 0, 0, **kwargs).draw_self()
        self.width = (self.options['padding']*2 + self.options['margin']*2 +
                      self.options['border_width']*2 + text_subsurface.get_width())
        self.height = (self.options['padding']*2 + self.options['margin']*2 +
                       self.options['border_width']*2 + text_subsurface.get_height())
        self._surface = pygame.Surface((self.width, self.height))
        border_rect = pygame.Rect(self.options['margin'], self.options['margin'],
                                  self.options['border_width']*2+text_subsurface.get_width()+self.options['padding']*2,
                                  self.options['border_width']*2+text_subsurface.get_height()+self.options['padding']*2)
        border_rect2 = pygame.Rect(self.options['margin']+self.options['border_width'],
                                   self.options['margin']+self.options['border_width'],
                                   self.options['padding']*2+text_subsurface.get_width(),
                                   self.options['padding']*2+text_subsurface.get_height())
        pygame.draw.rect(self._surface, self.options['border_color'], border_rect)
        pygame.draw.rect(self._surface, self.options['bgcolor'], border_rect2)
        offset = self.options['margin']+self.options['padding']+self.options['border_width']
        self._surface.blit(text_subsurface, (offset, offset))

    def draw_self(self) -> pygame.Surface:
        return self._surface


class SpinnerBox(SimpleUIElement):
    def __init__(self, x: int, y: int, initial_value: int, min_value: int, max_value: int, font_size=24):
        super().__init__(x, y, 1, 1)
        self._min = min_value
        self._max = max_value
        self.font_size = font_size
        self._value_callbacks = []
        self.value = initial_value
        self._remake_surface()

    def handle_event(self, event):
        super().handle_event(event)
        if event.type is pygame.MOUSEBUTTONDOWN:
            if self._value_up_rect.collidepoint(event.pos[0], event.pos[1]):
                self.value += 1
            elif self._value_down_rect.collidepoint(event.pos[0], event.pos[1]):
                self.value -= 1

    def _remake_surface(self):
        # The default Pygame Freetype font resolution assumes 72 dpi. We can use this to convert points to pixels and
        # back
        button_options = {
            'padding': 0,
            'margin': 0,
            'border': False,
            'border_width': 0,
            'font_size': self.font_size/2
        }
        value_up_button_surface = Button('▲', 0, 0, **button_options).draw_self()
        value_down_button_surface = Button('▼', 0, 0, **button_options).draw_self()
        label_surface = Label(str(self.value), 0, 0, font_size=self.font_size).draw_self()

        # Set the width to accomdate the maximum possible value. 9 usually one of the widest numbers, so we'll
        # calculate the width of several 9's, where the number of 9s is the same as the number of digits in
        # the maximum value.
        self.width = constants.DEFAULT_GAME_FONT.get_rect('9' * len(str(self._max)), size=self.font_size).width
        #self.width = nihongo_game_constants.DEFAULT_GAME_FONT.size('9'*len(str(self._max)))
        # self.width = Label(str('9')*len(str(self._max)), 0, 0, font_size=self.font_size).draw_self().get_width()
        self.width += value_up_button_surface.get_width() + 2
        self.height = value_up_button_surface.get_height() + 2 + value_down_button_surface.get_height()

        self._value_up_rect = pygame.Rect(0, 0, 0, 0)
        self._value_up_rect.x = self.width - value_up_button_surface.get_width()
        self._value_up_rect.y = 0
        self._value_up_rect.width = value_up_button_surface.get_width()
        self._value_up_rect.height = value_up_button_surface.get_height()

        self._value_down_rect = pygame.Rect(0, 0, 0, 0)
        self._value_down_rect.x = self._value_up_rect.x
        self._value_down_rect.y = self.height - value_down_button_surface.get_height()
        self._value_down_rect.width = value_down_button_surface.get_width()
        self._value_down_rect.height = value_down_button_surface.get_height()

        self.surface: pygame.Surface = pygame.Surface((self.width, self.height))
        self.surface.blit(value_up_button_surface, (self._value_up_rect.x, self._value_up_rect.y))
        self.surface.blit(value_down_button_surface, (self._value_down_rect.x, self._value_down_rect.y))
        self.surface.blit(label_surface, (self.width - label_surface.get_width() - value_up_button_surface.get_width() - 2,
                                          self.height/2 - label_surface.get_height()/2))
        print("Size: ", self.font_size)
        print("Actual Size: ", self.height)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value < self._min:
            value = self._min
        if value > self._max:
            value = self._max
        self._value = value
        self._remake_surface()
        for value_callback in self._value_callbacks:
            value_callback(self)

    def add_value_change_callback(self, callback):
        self._value_callbacks.append(callback)

    def remove_value_change_callback(self, callback):
        self._value_callbacks.remove(callback)

    def draw_self(self) -> pygame.Surface:
        return self.surface
