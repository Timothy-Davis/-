import word_database
import conversion
import random
word_database.init()


# The following method will fill the dictionary that will be used by main
def fill_dictionary():
    grammar_types = input("1. Verbs \n2. Adjectives \n3. Both \n")

    starting_chapter = input("Please input the beginning chapter: ").strip()
    ending_chapter = input("Please input the ending chapter: ").strip()

    chapter_range = (int(starting_chapter) if starting_chapter is not '' else 1,
                     int(ending_chapter) if ending_chapter is not '' else 1024)

    if grammar_types == '1':
        words = word_database.create_dictionary(chapters=chapter_range, grammar_types=('う-verb', 'る-verb'))
    elif grammar_types == '2':
        words = word_database.create_dictionary(chapters=chapter_range, grammar_types=('い-adjective', 'な-adjective'))
    else:
        words = word_database.create_dictionary(chapters=chapter_range,
                                                grammar_types=('い-adjective', 'な-adjective', 'う-verb', 'る-verb'))
    return words


"""
The following method is responsible for conjugating na-adjectives, i-adjectives, u-verbs, and ru-verbs to their present 
affirmative form; this includes the -ます, -です, and -だ endings (when it is grammatically required), short forms, and
changing the ending character of u-verbs. 
"""


def conjugate_present_affirmative(word, short_form, kanji):
    print(short_form)
    if short_form == 2:
        short_form = random.randint(0, 2)

    # Ru-verbs:
    if word.grammar_types == ['verb', 'る-verb']:
        if short_form == 0:
            if kanji == 1 and word.kanji is not None:
                conjugation = word.kanji[0:len(word.kanji)-1] + 'ます'
                return conjugation
            else:
                conjugation = word.hiragana[0:len(word.hiragana)-1] + 'ます'
                return conjugation
        else:
            if kanji == 1 and word.kanji is not None:
                conjugation = word.kanji
                return conjugation
            else:
                conjugation = word.hiragana
                return conjugation

    # U-verbs
    elif word.grammar_types == ['verb', 'う-verb']:
        if short_form == 0:
            if kanji == 1 and word.kanji is not None:
                temp = conversion.convert_to_kana(word.romaji[0:len(word.romaji)-1] + 'i')
                conjugation = word.kanji[0:len(word.kanji)-1] + temp[len(temp)-1] + 'ます'
                return conjugation
            else:
                temp = conversion.convert_to_kana(word.romaji[0:len(word.romaji) - 1] + 'i')
                conjugation = word.hiragana[0:len(word.hiragana) - 1] + temp[len(temp) - 1] + 'ます'
                return conjugation
        else:
            if kanji == 1 and word.kanji is not None:
                conjugation = word.kanji
                return conjugation
            else:
                conjugation = word.hiragana
                return conjugation

    # Na-Adjectives
    elif word.grammar_types == ['adjective', 'な-adjective']:
        if short_form == 0:
            if kanji == 1 and word.kanji is not None:
                conjugation = word.kanji + 'です'
                return conjugation
            else:
                conjugation = word.hiragana + 'です'
                return conjugation
        else:
            if kanji == 1 and word.kanji is not None:
                conjugation = word.kanji + 'だ'
                return conjugation
            else:
                conjugation = word.hiragana + 'だ'
                return conjugation

    # I-adjectives
    elif word.grammar_types == ['adjective', 'い-adjective']:
        if short_form == 0:
            if kanji == 1 and word.kanji is not None:
                conjugation = word.kanji + 'です'
                return conjugation
            else:
                conjugation = word.hiragana + 'です'
                return conjugation
        else:
            if kanji == 1 and word.kanji is not None:
                conjugation = word.kanji
                return conjugation
            else:
                conjugation = word.hiragana
                return conjugation


"""
The following method is responsible for conjugating い/な-adjectives and る/う verbs into the present negative tense,
this includes the special case short form for verbs that end in う, specifically. -ます, です, and -だ are also added
where ever they are grammatically required.
"""


def conjugate_present_negative(word, short_form, kanji):
    if short_form == 2:
        short_form = random.randint(0, 2)

    # Ru-verbs:
    if word.grammar_types == ['verb', 'る-verb']:
        if short_form == 0:
            if kanji == 1 and word.kanji is not None:
                conjugation = word.kanji[0:len(word.kanji) - 1] + 'ません'
                return conjugation
            else:
                conjugation = word.hiragana[0:len(word.hiragana) - 1] + 'ません'
                return conjugation
        else:
            if kanji == 1 and word.kanji is not None:
                conjugation = word.kanji[0:len(word.kanji) - 1] + 'ない'
                return conjugation
            else:
                conjugation = word.hiragana[0:len(word.kanji) - 1] + 'ない'
                return conjugation

    # U-verbs
    elif word.grammar_types == ['verb', 'う-verb']:
        if short_form == 0:
            if kanji == 1 and word.kanji is not None:
                temp = conversion.convert_to_kana(word.romaji[0:len(word.romaji) - 1] + 'i')
                conjugation = word.kanji[0:len(word.kanji) - 1] + temp[len(temp) - 1] + 'ません'
                return conjugation
            else:
                temp = conversion.convert_to_kana(word.romaji[0:len(word.romaji) - 1] + 'i')
                conjugation = word.hiragana[0:len(word.hiragana) - 1] + temp[len(temp) - 1] + 'ません'
                return conjugation
        else:
            if kanji == 1 and word.kanji is not None:
                if word.kanji[len(word.kanji) - 1] == 'う':
                    conjugation = word.kanji[0:len(word.kanji) - 1] + 'わない'
                    return conjugation

                temp = conversion.convert_to_kana(word.romaji[0:len(word.romaji) - 1] + 'a')
                conjugation = word.kanji[0:len(word.kanji) - 1] + temp[len(temp) - 1] + 'ない'
                return conjugation
            else:
                temp = conversion.convert_to_kana(word.romaji[0:len(word.romaji) - 1] + 'a')
                conjugation = word.hiragana[0:len(word.hiragana) - 1] + temp[len(temp) - 1] + 'ない'
                return conjugation

    # Na-Adjectives
    elif word.grammar_types == ['adjective', 'な-adjective']:
        if short_form == 0:
            if kanji == 1 and word.kanji is not None:
                conjugation = word.kanji + 'じゃないです'
                return conjugation
            else:
                conjugation = word.hiragana + 'じゃないです'
                return conjugation
        else:
            if kanji == 1 and word.kanji is not None:
                conjugation = word.kanji + 'じゃない'
                return conjugation
            else:
                conjugation = word.hiragana + 'じゃない'
                return conjugation

    # I-adjectives
    elif word.grammar_types == ['adjective', 'い-adjective']:
        if short_form == 0:
            if kanji == 1 and word.kanji is not None:
                conjugation = word.kanji[0:len(word.kanji) - 1] + 'くないです'
                return conjugation
            else:
                conjugation = word.hiragana[0:len(word.hiragana) - 1] + 'くないです'
                return conjugation
        else:
            if kanji == 1 and word.kanji is not None:
                conjugation = word.kanji[0:len(word.kanji) - 1] + 'くない'
                return conjugation
            else:
                conjugation = word.hiragana[0:len(word.hiragana) - 1] + 'くない'
                return conjugation

# def conjugate_past_affirmative(word, short_form, kanji):
# def conjugate_past_negative(word, short_form, kanji):
# def conjugate_te_form(word, kanji):


if __name__ == '__main__':
    word_list = fill_dictionary()
    sf = int(input("0. Polite \n1. Plain \n2. Both \n"))
    han = int(input("0. No Kanji \n1. Kanji \n"))
    for x in range(1, 6):
        current_word = word_list.random_word()
        print(current_word.kanji)
        print(conjugate_present_negative(current_word, sf, han))


