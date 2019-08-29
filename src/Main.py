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
]

MAIN_MENU_STATE = 0
GAME_STATE = 1

def main():
    word_database.init()
    pygame.init()
    pygame.display.set_mode(DEFAULT_SIZE)

    menu = MainMenu()
    game = menu

    done = False
    current_time = time.perf_counter_ns()
    lag = 0
    state = MAIN_MENU_STATE
    while not done:
        old_time = current_time
        current_time = time.perf_counter_ns()
        lag += current_time - old_time

        game.display()
        for event in pygame.event.get():
            game.handle_pygame_event(event)

        while lag > UPDATE_TIME:
            game.update()
            lag -= UPDATE_TIME

        pygame.display.flip()

        # If we are in the MAIN_MENU_STATE, we want to check and see if the
        # main menu has a command to swap out to a game, or if the user wishes to quit entirely.
        if state is MAIN_MENU_STATE:
            done = menu.is_done()
            if menu.selected_game() is not None:
                game = menu.selected_game()
                state = GAME_STATE
        else:
            if game.is_done():
                state = MAIN_MENU_STATE

if __name__ == '__main__':
    main()
