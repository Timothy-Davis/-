"""
This file contains the "brains" for a Typeracer style game where you
will be given a word in Japanese and be tasked with typing the romaji
for the word in the quickest time possible.
"""

import word_database
import random


class TypeRace:
    def __init__(self, word_list: word_database.Dictionary, lives=3):
        self.current_word = None
        self.word_list = list(word_list.wordlist)
        self.lives = lives

        self.assign_word()

    def assign_word(self):
        if len(self.word_list) > 0:
            self.current_word = (
                self.word_list.pop(random.randrange(len(self.word_list))))
            print(len(self.word_list))
        return None

    def check_answer(self, answer):
        if self.current_word.romaji == answer:
            return True
        self.reduce_lives()
        return False

    def reduce_lives(self):
        self.lives -= 1


if __name__ == "__main__":
    word_database.init()
    new_game = TypeRace(word_database.create_dictionary(), 3)
    incorrect_words = []

    print("##########   CLI TYPERACER ########## ")
    print("Type the Japanese word displayed without fucking up!\n")

    while new_game.current_word is not None and new_game.lives > 0:
        print("LIVES: " + str(new_game.lives) + "\nCURRENT WORD: \n" + new_game.current_word.hiragana)
        answer = input("YOUR GUESS: \n")
        if new_game.check_answer(answer):
            print("NICE! \n\n")
        else:
            print("YOU SUCK \n\n")
            incorrect_words.append(new_game.current_word)

        new_game.assign_word()

    if new_game.current_word is None:
        print("You 've won! Tim must have taught you Japanese!")
    else:
        print("Bro... Did Aaron teach you Japanese? You are cheeks.")

    print("you sucked espcially with these words: ")
    for word in incorrect_words:
        print(word)
