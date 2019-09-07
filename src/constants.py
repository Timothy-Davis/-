import typing
import pygame
from pygame import Color
import pygame.freetype
pygame.init()

# Typing aliases, because these can get pretty darn lengthy
PygameEvent = pygame.event.Event
PygameEventType = pygame.event.EventType
PygameEventList = typing.List[pygame.event.EventType]

# Global game defaults
DEFAULT_FONT_SIZE = 24
DEFAULT_GAME_FONT = pygame.freetype.Font("./fonts/NotoSansCJKjp-Regular.otf")
DEFAULT_FONT_OPTIONS = {
    'fgcolor': Color(255, 255, 255, 255),
    'bgcolor': Color(0, 0, 0, 255),
    'style': pygame.freetype.STYLE_DEFAULT,
    'rotation': 0,
    'font-size': DEFAULT_FONT_SIZE
}

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (255, 0, 0)
BLUE = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 128)
PINK = (255, 0, 255)

