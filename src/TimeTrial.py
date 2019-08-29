"""
The point of the TimeTrial game is to, given a range of chapters, correctly guess the english word, or japanese romaji,
for a given word for all words in that range of chapters. Later changes to this module may allow the player to specify
a particular kind of grammar construct instead, such as only verbs. For now, it will be limited to attempting to get a
series of words correct.
"""

import sys
from word_database import Dictionary, create_dictionary, init, Word

init()

def get_user_bool(prompt):
    try:
        user_input = input(prompt).strip().lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            raise ValueError
    except ValueError:
        print(f"'{user_input}': That is an invalid value. Please try again.")
    except IOError as e:
        print("I/O Error Occurred:\n", e)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def get_user_int(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input is None:
                raise ValueError
            return user_input
        except ValueError:
            print("That is an invalid value. Please try again.")
        except IOError as e:
            print("I/O Error Occurred:\n", e)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise


def run():
    import time
    okay = False
    while not okay:
        chapter_begin = get_user_int("What chapter would you like to begin at: ")
        chapter_end = get_user_int("What chapter would you like to end at: ")
        print()

        word_dict = create_dictionary((chapter_begin, chapter_end))

        print("You have selected the following options:")
        print(f"Chapter Range: [{chapter_begin}, {chapter_end}]")
        print(f"Number of Words Found: {len(word_dict)}")
        okay = get_user_bool("Are these options okay [Y/N]: ")

    start = time.perf_counter()
    for word in word_dict.wordlist:
        correct = False
        guesses = 0
        while not correct:
            guess = input(f'{word.hiragana}: ').strip().lower()
            if guess in word.english:
                print("Correct!")
                correct = True
            else:
                guesses += 1
                if guesses == 3:
                    print("The correct answer was:", word.english)
                print("Sorry, that's not correct.")
    end = time.perf_counter()
    total = round(end - start, 2)
    print("Time Taken:", total, 'seconds')

if __name__ == '__main__':
    run()