import sys
import time
import pygame
import typing
import word_database

from main_menu import MainMenu
from game_base import Game, GameInfo, SWAP_GAME, END_GAME

pygame.init()

DEFAULT_SIZE = (960, 540)
NS_PER_SEC = 1000000000
UPDATES_PER_SEC = 60
UPDATE_TIME = NS_PER_SEC/UPDATES_PER_SEC

GAMES: typing.List[GameInfo] = [
    MainMenu.info()
]


def init() -> None:
    word_database.init()
    pygame.display.set_mode(DEFAULT_SIZE)


def deinit():
    pass


def main():
    init()
    main_menu: MainMenu = MainMenu(available_games=GAMES)
    game: Game = main_menu

    current_time = time.perf_counter_ns()
    lag = 0
    while True:
        old_time = current_time
        current_time = time.perf_counter_ns()
        lag += current_time - old_time

        for event in pygame.event.get():
            game.handle_pygame_event(event)
            if event.type is pygame.QUIT:
                sys.exit(1)

        while lag > UPDATE_TIME:
            game.update()
            lag -= UPDATE_TIME
        game.display()

        pygame.display.flip()

        for event in game.emitted_events():
            if event.type is END_GAME:
                game = main_menu
            elif event.type is SWAP_GAME:
                if event.new_game is not None:
                    game = event.new_game()


if __name__ == '__main__':
    main()
