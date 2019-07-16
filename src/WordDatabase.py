"""
Word Database is the center for all operations on the list of all words that are both stored on the User's computer, and
that are kept in memory by the program at runtime. This module defines the Dictionary class, and functions for creating
Dictionaries from queries, as well as providing the global_dictionary, which is the dictionary containing all words.
"""

# This module implements the Database connection methods necessary for the rest of the games to work, by allowing them
# to retrieve lists of words based on various criteria, add words to the dictionary that the user requests added, and
# allow for ease in updating words if there is an error the user has spotted.
#
# The most important class in here is the DatabaseConnection class, which is actually not a single class, but a
# collection of classes that masquerade as a single class when the client requests a database connection. The connection
# they get is actually decided at runtime based on the version of the Database they are using. It's really a moot point
# at the moment, since we only have a single version, but that will likely change as the app grows. So, for the future,
# it is better if all database operations are completed through the helper functions to avoid corrupting any future
# databases!

# TODO: Implement a singular Fetch function that allows fetching based on criteria (such as chapter range)

import os
import random
import sqlite3

import default_wordbank
import exceptions
import tree

# Note: We use japanese only for the Windows name because not all non-nt systems are guaranteed to support
# Unicode filenames!
__DATABASE_NAME = 'wordbank.db'
__DATABASE_DIR_WIN = '~/Documents/日本語のゲイム/'
__DATABASE_DIR_DEF = '~/.config/nihongonogeimu/'
__DATABASE_DIR = __DATABASE_DIR_WIN if os.name is 'nt' else __DATABASE_DIR_DEF
__DATABASE_PATH = __DATABASE_DIR + __DATABASE_NAME


class Word:
    def __init__(self, english=None, romaji='', kanji='', chapter=0, note=''):
        if english is None:
            self.english = []
        else:
            self.english = english
        self.chapter = chapter
        self.kanji = kanji
        self.romaji = romaji
        self.hiragana = tree.convert_to_kana(romaji, tree.HIRAGANA)
        self.katakana = tree.convert_to_kana(romaji, tree.KATAKANA)
        self.note = note


# The DatabaseInterface as defined for version 0.1.0 of the program.
class __DatabaseInterfaceV010:
    """
    This class is responsible for maintaining and operating on the physical SQLite3 Database that is used to back the
    application. A simple CRUD class, so that most of the Database logic can be consolidated in one place. It is not
    meant to be used outside of this module, since the rest of the app should be totally uncaring of whether we use a
    real database or not.
    """

    __WORD_TABLE_NAME = 'words'
    WORD_FIELDS = ['id', 'english', 'romaji', 'kanji', 'chapter', 'note', 'user_added']
    WORD_ID_FIELD = 0
    WORD_ENGLISH_FIELD = 1
    WORD_ROMAJI_FIELD = 2
    WORD_KANJI_FIELD = 3
    WORD_CHAPTER_FIELD = 4
    WORD_NOTE_FIELD = 5
    WORD_USER_ADDED_FIELD = 6

    __VERSION_TABLE_NAME = 'version_info'
    VERSION_FIELDS = ['id', 'version_major', 'version_minor', 'version_patch']
    VERSION_ID_FIELD = 0
    VERSION_MAJOR_FIELD = 1
    VERSION_MINOR_FIELD = 2
    VERSION_PATCH_FIELD = 3

    __CREATE_TABLE_STATEMENTS = [
        f'''
            CREATE TABLE IF NOT EXISTS {__WORD_TABLE_NAME} 
            (
                id integer PRIMARY KEY,
                english text NOT NULL,
                romaji text NOT NULL,
                kanji text NOT NULL,
                chapter integer NOT NULL,
                note text,
                user_added integer NOT NULL
            );
        ''',
        f'''
            CREATE TABLE IF NOT EXISTS {__VERSION_TABLE_NAME}
            (
                id integer PRIMARY KEY,
                version_major integer NOT NULL,
                version_minor integer NOT NULL,
                version_patch integer NOT NULL
            );
        ''',
    ]

    __INSERT_STATEMENT = 'INSERT INTO words(english,romaji,kanji,chapter,note,user_added) VALUES(?,?,?,?,?,?)'
    __VERSION_INSERT_STATEMENT = '''INSERT INTO version_info(version_major,version_minor,version_patch) VALUES(?,?,?)'''

    def __init__(self, db_path):
        if db_path is None:
            raise ValueError('Database path is invalid!')
        self.db_path = db_path
        self.db_conn = None
        self.__connect()

    def __del__(self):
        if self.db_conn is not None:
            self.db_conn.commit()
            self.db_conn.close()

    def __connect(self):
        """
        Creates the true SQLite connection to the database
        """
        try:
            self.db_conn = sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            if self.db_conn is not None:
                self.db_conn.close()
                self.db_conn = None
                raise exceptions.DatabaseError('Error connection to SQLite DB:\n'+str(e))

    def create_new(self):
        """
        Initializes the database as though it were new.
        """
        self.__create_tables()
        self.__setup_version_table()

    def __create_tables(self):
        """
        Creates the Database Tables if they do not already exist.
        """
        if self.db_conn is not None:
            try:
                cursor = self.db_conn.cursor()
                for TABLE_STATEMENT in self.__CREATE_TABLE_STATEMENTS:
                    cursor.execute(TABLE_STATEMENT)
                cursor.close()
            except sqlite3.Error as e:
                raise exceptions.DatabaseError('Error creating tables:\n'+str(e))
        else:
            raise exceptions.DatabaseError("Can't setup version table without a connection!")

    def __setup_version_table(self):
        if self.db_conn is not None:
            try:
                cursor = self.db_conn.cursor()
                cursor.execute(self.__VERSION_INSERT_STATEMENT, (0, 1, 0))
                cursor.close()
            except sqlite3.Error as e:
                raise exceptions.DatabaseError('Error inserting version info:\n'+str(e))
        else:
            raise exceptions.DatabaseError("Can't setup version table without a connection!")

    def insert_word(self, word: Word, user_defined=False):
        """
        Inserts a new word into the Database. Note: If attempting to insert multiple words, use batch_insert() instead.
        :param word: The Word object representing the word to be inserted
        :param user_defined: A boolean representing if this word was made by the user or came from a default list
        """
        if self.db_conn is not None:
            try:
                cursor = self.db_conn.cursor()
                eng = word.english.join('_')
                word_tuple = (eng, word.romaji, word.kanji, word.chapter, word.note, 1 if user_defined else 0)
                cursor.execute(self.__INSERT_STATEMENT, word_tuple)
                cursor.close()
            except sqlite3.Error as e:
                raise exceptions.DatabaseError('Unable to insert word:\n'+str(e))
        else:
            raise exceptions.DatabaseError('Unable to insert word without a connection!')

    def batch_insert(self, words: list, user_defined=False):
        try:
            cursor = self.db_conn.cursor()
            for word in words:
                eng = word.english.join('_')
                word_tuple = (eng, word.romaji, word.kanji, word.chapter, word.note, 1 if user_defined else 0)
                cursor.execute(self.__INSERT_STATEMENT, word_tuple)
            cursor.close()
        except sqlite3.Error as err:
            print("Error inserting new word into DB:")
            print(err)

    def fetch_all(self) -> list:
        """
        Retrieves all words from the Database in a list
        :return: A list of Word objects from the Database
        """
        word_list = []
        if self.db_conn is not None:
            cursor = self.db_conn.cursor()
            cursor.execute(f'SELECT * FROM {self.__WORD_TABLE_NAME}')
            raw_word_list = cursor.fetchall()
            cursor.close()
            for word in raw_word_list:
                # word[0] is omitted because it is merely the primary ID key of the database.
                # Kanji and Note are not guaranteed to exist, in which case they are 'None'
                kanji = None if word[self.WORD_KANJI_FIELD] is 'None' else word[self.WORD_KANJI_FIELD]
                note = None if word[self.WORD_NOTE_FIELD] is 'None' else word[self.WORD_NOTE_FIELD]
                eng = word[self.WORD_ENGLISH_FIELD].split('_')
                word_list.append(Word(eng, word[self.WORD_ROMAJI_FIELD], kanji, word[self.WORD_CHAPTER_FIELD], note))
            return word_list
        else:
            raise exceptions.DatabaseError('Can\'t fetch words without a connection!')


class Dictionary:
    def __init__(self, words: list = None):
        """
        Creates a new Dictionary object from a list of words.
        :param words: A list object containing Word objects
        """
        if words is None:
            self.wordlist = None
        else:
            self.wordlist = tuple(words)

    def random_word(self):
        return random.choice(self.wordlist)


def __create_connection(path):
    database_existed = os.path.exists(__DATABASE_DIR) and os.path.exists(__DATABASE_PATH)
    if not os.path.exists(__DATABASE_DIR):
        os.makedirs(__DATABASE_DIR, exist_ok=True)

    if not database_existed:
        # Easy, just make the latest version connection
        conn = __DatabaseInterfaceV010(path)
        conn.create_new()
        conn.batch_insert(default_wordbank.words, False)
        return conn
    else:
        # Right now, we only have one version. Later we'll have to start checking the version number...
        return __DatabaseInterfaceV010(path)


# Initialized by init(), and used for all future operations on the words.
__database_connection = None


def init():
    global __database_connection
    __database_connection = __create_connection(__DATABASE_PATH)


def create_dictionary(chapters=None) -> Dictionary:
    """
    Returns a new Dictionary that conforms to the passed parameters
    :param chapters: A 2-element Tuple defining the range (inclusive), or None for all chapters. Default value is None.
    :return: A Dictionary object representing the filtered list of words.
    """
    if chapters is None:
        return Dictionary(__database_connection.fetch_all())
    else:
        raise NotImplemented('Fetching by chapter is not yet implemented!')
    # __database_connection.fetch(where_clause='CHAPTERS')


if __name__ == '__main__':
    init()
    dictionary = create_dictionary()
    for current_word in dictionary.wordlist:
        print(current_word.english, '|',
              current_word.romaji, '|',
              current_word.hiragana, '|',
              current_word.katakana, '|',
              current_word.kanji, '|',
              current_word.chapter, '|',
              current_word.note)
