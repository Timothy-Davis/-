import pygame
from abc import ABC, abstractmethod

MENU_BAR_HEIGHT = 22


class Game(ABC):
    def __init__(self, show_menu_bar: bool = True):
        self.done = False
        self.real_surface: pygame.Surface = pygame.display.get_surface()
        if show_menu_bar:
            subrect: pygame.Rect = pygame.Rect(0,
                                               MENU_BAR_HEIGHT,
                                               self.real_surface.get_width(),
                                               self.real_surface.get_height()-MENU_BAR_HEIGHT)
            self.surface: pygame.Surface = self.real_surface.subsurface(subrect)
        else:
            self.surface: pygame.Surface = self.real_surface

    def handle_pygame_event(self, event):
        if event.type is pygame.QUIT:
            self.done = True
        else:
            self.handle_event(event)

    @abstractmethod
    def handle_event(self, event) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def display(self) -> None:
        pass

    def is_done(self) -> bool:
        return self.done
