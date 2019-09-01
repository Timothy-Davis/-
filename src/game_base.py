from abc import ABC, abstractmethod

import typing
import pygame
pygame.init()

# TODO: This entire module really needs to be cleaned up once we get at least a few mini games working...

_MENU_BAR_HEIGHT_PERCENT = 0.05

# Emittable Events
SWAP_GAME: int = 0xF1
END_GAME: int = 0xF2

# TODO: We probably need an enum here, too.
EMITTABLE_EVENTS: typing.List[int] = [
    SWAP_GAME, END_GAME
]


class GameInfo:
    def __init__(self, title, constructor, img=None):
        self.title = title
        self.init = constructor
        self.img = img


class Game(ABC):
    def __init__(self, show_menu_bar: bool = True):
        self._real_surface: pygame.Surface = pygame.display.get_surface()
        self._show_menu_bar: bool = show_menu_bar
        self._emitted_events: typing.List[pygame.event.Event] = []

        if self._show_menu_bar:
            menu_bar_height = _MENU_BAR_HEIGHT_PERCENT * self._real_surface.get_height()
            subrect = pygame.Rect(0,
                                  menu_bar_height,
                                  self._real_surface.get_width(),
                                  self._real_surface.get_height() - menu_bar_height)
            self.surface: pygame.Surface = self._real_surface.subsurface(subrect)
        else:
            self.surface: pygame.Surface = self._real_surface

    def handle_pygame_event(self, event) -> None:
        if event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]:
            if self._show_menu_bar:
                event.pos = event.pos[0], event.pos[1]-(_MENU_BAR_HEIGHT_PERCENT * self._real_surface.get_height())
        self.handle_event(event)

    def emit_event(self, event: pygame.event.Event) -> None:
        """
        Emits a Event for the outer framework to handle. This method should not be overriden by subclasses under any
        circumstances.
        :param event: The Event object to be emitted. If the type of the Event object is not among the valid
                      emittable events, it will be discarded.
        """
        if event.type in EMITTABLE_EVENTS:
            self._emitted_events += event

    def emitted_events(self) -> typing.List[pygame.event.Event]:
        """
        Returns the list events that have been put into the queue with emit_event(). This method should not be overriden
        by subclasses under any circumstances.
        :return: An iterable of Event objects that have been emitted by the game.
        """
        return self._emitted_events

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> bool:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def display(self) -> None:
        pass

    @classmethod
    @abstractmethod
    def info(cls) -> typing.Optional[GameInfo]:
        return None
