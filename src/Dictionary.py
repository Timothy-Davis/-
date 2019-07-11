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

    @staticmethod
    def init(self):
        self.wordlist = Database.load_all()

    def get_random_word(self):
        amount_of_words = len(self.wordlist)
        random_index = random.randint(0, amount_of_words-1)

        return self.wordlist[random_index]


# Globally accessible dictionary that most of the mini games will actually use
global_dictionary = Dictionary()
global_dictionary.get_random_word()