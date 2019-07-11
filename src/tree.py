# The parse tree is made up of several trees and dictionaries mapped together. While it may look complicated, the
# overall structure is relatively simple. When the parse begins, it looks at the first character, and checks the tree.
# If the character maps to a list, then the parser knows it has reached a leaf and can check HIRAGANA_INDEX of the list
# to get the hiragana character, or KATAKANA_INDEX for the katakana character. If it maps to another dictionary, the
# parser knows it has to look at the next character to determine what the final character(s) should be.

# Note: Some characters can only be represented by katakana, and are invalid in hiragana. The parser can check the 
# HAS_HIRAGANA index for a boolean that indicates if the character has a hiragana equivalent.

HAS_HIRAGANA   = 0
HIRAGANA_INDEX = 1
KATAKANA_INDEX = 2

parse_tree ={
                # Top level vowels. These always map one-to-one if they are the first character.
                'a': [True, 'あ', 'ア'],
                'i': [True, 'い', 'イ'],
                'u': [True, 'う', 'ウ'],
                'e': [True, 'え', 'エ'],
                'o': [True, 'お', 'オ'],

                'k': {
                        'a': [True, 'か', 'カ'],
                        'i': [True, 'き', 'キ'],
                        'u': [True, 'く', 'ク'],
                        'e': [True, 'け', 'ケ'],
                        'o': [True, 'こ', 'コ'],

                        'y': {
                                'a': [True, 'きゃ', 'キャ'],
                                'o': [True, 'きょ', 'キョ'],
                                'u': [True, 'きゅ', 'キュ'],
                            }
                    },
                'n': None,
                's': None,
                'z': None,
                'j': None,
                't': None,
                'd': None,
                'c': None,
                'h': None,
                'b': None,
                'f': None,
                'm': None,
                'y': None,
                'r': None,
                'w': None,
                'g': None,
        }

TSU_CONSONANTS = ['k', , 's', 'z', 'j', 't', 'd', 'c', 'h', 'b', 'f', 'm', 'y', 'r', 'w', 'g']

HIRAGANA = False
KATAKANA = True

def convert_to_kana(romaji: str, kana: bool = HIRAGANA) -> str:
    output_str = ''
    index = 0
    while index != len(romaji):
        temp = parse_tree
        if (index <= len(romaji)-2 and romaji[index] == romaji[index+1] and romaji[index] in TSU_CONSONANTS):
            if kana is KATAKANA:
                output_str += 'ッ'
            else:
                output_str += 'っ'
            index += 1
            continue
        while type(temp) != list:
            temp = temp[romaji[index]]
            index += 1

        if kana is KATAKANA:
            output_str+=temp[KATAKANA_INDEX]
        else:
            if temp[HAS_HIRAGANA]:
                output_str+=temp[HIRAGANA_INDEX]
            else:
                raise ValueError("Invalid romaji to hiragana conversion. Romaji: " + romaji)
    return output_str

if __name__ == '__main__':
    romaji = input('Please input some romaji [q to quit]: ').lower()
    while romaji is not 'q':
        print(convert_to_kana(romaji))
        print(convert_to_kana(romaji, kana=KATAKANA))
        romaji = input('Please input some romaji [q to quit]: ').lower()
