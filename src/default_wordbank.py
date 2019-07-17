"""
This module contains the default wordbank used by the program upon first installation, row when the Database file has
somehow been damaged/is missing.
"""

# Words in this file should follow a very strict format. If you add, change, or delete
# a word in this file, it should be run as a main module so that the automated checker can run through all the words to
# make sure there are no formatting errors!

# Words follow this pattern:
# (enlgish, romaji, kanji, chapter, note)
# Please observe the following tenants:
#    0. All words, english included, should be in lowercase.
#    1. If a word has multiple english meanings, separate them with an underscore.
#    2. If a word has no kanji, use the string literal 'None'
#    3. If a word does not have a chapter in Genki, use 0
#    4. If there is no note to be made about the word, use the string literal 'None'

# Although this file is currently not very organized, in the future it would be best moving forward if words are kept in
# order by their chapter. Words not belonging to any chapter should be at the end of the list, with chapter number 0.

FIELDS = 5
ENGLISH_INDEX = 0
ROMAJI_INDEX = 1
KANJI_INDEX = 2
CHAPTER_INDEX = 3
NOTE_INDEX = 4

words = [
    ('this one', 'kore', 'None', 2, 'None'),

    ('cold', 'samui', '寒い', 5, 'None'),
    ('hot', 'atsui', '暑い', 5, 'Hot Weather'),
    ('hot', 'atsui', '熱い', 5, 'Hot to the Touch'),

    ('my older sister', 'ane', '姉', 7, 'None'),

    ('job_work_occupation', 'shigoto', '仕事', 8, 'None'),
    ('winter', 'fuyu', '冬', 8, 'None'),

    ('to take medicine', 'kusuriwonomu', '薬を飲む', 9, 'None'),

    ('thick', 'atsui', '厚い', 0, 'Thick'),
    ('deep_strong', 'atsui', '篤い', 0, 'Deep or Strong'),
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

    if type(check_word[4]) != str:
        return 'The note should be a string'


if __name__ == '__main__':
    error = None
    for word in words:
        error = __check_word(word)
        if error is not None:
            print('ERROR IN WORD:', word)
            print(error)
    print('Finished checking!')
