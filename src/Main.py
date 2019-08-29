import time
import pygame
import word_database

from game_base import Game
from main_menu import MainMenu

DEFAULT_SIZE = (960, 540)
NS_PER_SEC = 1000000000
NS_PER_MSEC = 1000000
NS_PER_MICROSEC = 1000
UPDATES_PER_SEC = 60
UPDATE_TIME = NS_PER_SEC/UPDATES_PER_SEC

GAMES = [
    #MainMenu()
]

def main():
    word_database.init()
    pygame.init()
    pygame.display.set_mode(DEFAULT_SIZE)

    current_game: Game = MainMenu()

    current_time = time.perf_counter_ns()
    lag = 0
    done = False
    while not done:
        old_time = current_time
        current_time = time.perf_counter_ns()
        lag += current_time - old_time

        current_game.display()

        for event in pygame.event.get():
            current_game.handle_pygame_event(event)

        while lag > UPDATE_TIME:
            current_game.update()
            lag -= UPDATE_TIME

        pygame.display.flip()

        done = current_game.is_done()

if __name__ == '__main__':
    main()
