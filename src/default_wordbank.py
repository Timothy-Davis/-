"""
This module contains the default wordbank used by the program upon first installation, row when the Database file has
somehow been damaged/is missing.
"""

# Words in this file should follow a very strict format. If you add, change, or delete
# a word in this file, it should be run as a main module so that the automated checker can run through all the words to
# make sure there are no formatting errors!

# Words follow this pattern:
# (enlgish, romaji, kanji, chapter, grammar_types, note)
# Please observe the following tenants:
#   0. All words, english included, should be in lowercase. The only exception is the special case of 'None'.
#   1. If a word has multiple english meanings, separate them with an underscore.
#   2. If a word has multiple grammar types, separate them with an underscore.
#   3. All Grammar Types are innumerated in VALID_GRAMMAR_TYPES. Make sure your type belongs, or add it.
#   3. If a word has no kanji, use the string literal 'None'
#   4. If a word does not have a chapter in Genki, use 0
#   5. If there is no note to be made about the word, use the string literal 'None'

# Although this file is currently not very organized, in the future it would be best moving forward if words are kept in
# order by their chapter. Words not belonging to any chapter should be at the end of the list, with chapter number 0.

FIELDS = 6
ENGLISH_INDEX = 0
ROMAJI_INDEX = 1
KANJI_INDEX = 2
CHAPTER_INDEX = 3
GRAMMAR_INDEX = 4
NOTE_INDEX = 5

VALID_GRAMMAR_TYPES = [
    'noun',
    'pronoun',
    'verb',
    'adjective',
    'い-adjective',
    'な-adjective',
    'う-verb',
    'る-verb',
]

words = [
    ('this one', 'kore', 'None', 2, 'pronoun', 'None'),

    ('cold', 'samui', '寒い', 5, 'adjective_い-adjective', 'None'),
    ('hot', 'atsui', '暑い', 5, 'adjective_い-adjective', 'Hot Weather'),
    ('hot', 'atsui', '熱い', 5, 'adjective_い-adjective', 'Hot to the Touch'),
    ('fond_likeable', 'suki', '好き', 5, 'adjective_な-adjective', 'None'),

    ('my older sister', 'ane', '姉', 7, 'pronoun', 'None'),

    ('job_work_occupation', 'shigoto', '仕事', 8, 'noun', 'None'),
    ('winter', 'fuyu', '冬', 8, 'noun', 'None'),

    ('to take medicine', 'kusuriwonomu', '薬を飲む', 9, 'verb_う-verb', 'None'),

    ('thick', 'atsui', '厚い', 0, 'adjective_い-adjective', 'Thick'),
    ('deep_strong', 'atsui', '篤い', 0, 'adjective_い-adjective', 'Deep or Strong'),
]


def __check_word(check_word):
    if len(check_word) != FIELDS:
        return 'There are not exactly ' + str(FIELDS) + ' fields!'
    for item in check_word:
        if item is None:
            return 'No item should be None type! Use \'None\' instead!'

    if type(check_word[0]) != str:
        return 'The english words should be a string!'

    if type(check_word[1]) != str:
        return 'The romaji should be a string!'
    if not check_word[1].isalpha():
        return 'The romaji should be purely alphabetic!'

    if type(check_word[2]) != str:
        return 'The kanji should be a string!'
    for char in check_word[2]:
        if char.isspace() or not char.isprintable():
            return 'The kanji should not contain spaces or non-printable characters!'

    if type(check_word[3]) != int:
        return 'Chapter should be an integer!'
    if check_word[3] < 0:
        return 'Chapter should be 0 or greater.'

    if check_word[4] is None or check_word[4] is '':
        return 'Grammar Types string cannot be None or empty!'
    if type(check_word[4]) != str:
        return 'Grammar Types should be underscore-separated string!'
    for grammar_type in check_word[4].split('_'):
        if grammar_type not in VALID_GRAMMAR_TYPES:
            return f'Grammar Type {grammar_type} is not in the list of valid grammar types!'

    if type(check_word[5]) != str:
        return 'The note should be a string'


if __name__ == '__main__':
    error = None
    for word in words:
        error = __check_word(word)
        if error is not None:
            print('ERROR IN WORD:', word)
            print(error)
    print('Finished checking!')
