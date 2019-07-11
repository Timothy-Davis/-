import Database
import random


class Word:
    def __init__(self, english=None, chapter=0, romaji='', hiragana='', katakana='', kanji='', note=''):
        if english is None:
            self.english = []
        else:
            self.english = english
        self.chapter = chapter
        self.kanji = kanji
        self.romaji = romaji
        self.hiragana = hiragana
        self.katakana = katakana
        self.note = note


class Dictionary:
    def __init__(self):
        self.wordlist = []

    def init(self):
        self.wordlist = Database.load_all()

    def random_word(self):
        return random.choice(self.wordlist)


# Globally accessible dictionary that most of the mini games will actually use
global_dictionary = Dictionary()

if __name__ == '__main__':
    global_dictionary.init()
    word = global_dictionary.random_word()
    print("Random Word:", word.english, word.kanji, word.hiragana, word.katakana, word.romaji, word.note)
