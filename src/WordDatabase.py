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

import os
import random
import sqlite3

from typing import Union, List, Tuple

import default_wordbank
import exceptions
import tree

# Note: We use japanese only for the Windows name because not all non-nt systems are guaranteed to support
# Unicode filenames!
__DATABASE_NAME = 'wordbank.db'
__DATABASE_DIR_WIN = '~/Documents/日本語のミニゲイム'
__DATABASE_DIR_DEF = '~/.config/nihongonominigeimu/'
__DATABASE_DIR = os.path.expanduser(__DATABASE_DIR_WIN if os.name is 'nt' else __DATABASE_DIR_DEF)
__DATABASE_PATH = __DATABASE_DIR + __DATABASE_NAME


class Word:
    def __init__(self, english=None, romaji='', kanji='', chapter=0, grammar_types=None, note=''):
        self.english = english if english is not None else []
        self.grammar_types = grammar_types if grammar_types is not None else []
        self.chapter = chapter
        self.kanji = kanji
        self.romaji = romaji
        self.hiragana = tree.convert_to_kana(romaji, tree.HIRAGANA) if romaji is not '' else None
        self.katakana = tree.convert_to_kana(romaji, tree.KATAKANA) if romaji is not '' else None
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
    WORD_FIELDS = ['id', 'english', 'romaji', 'kanji', 'chapter', 'grammar_types', 'note', 'user_added']
    WORD_ID_FIELD = 0
    WORD_ENGLISH_FIELD = 1
    WORD_ROMAJI_FIELD = 2
    WORD_KANJI_FIELD = 3
    WORD_CHAPTER_FIELD = 4
    WORD_GRAMMAR_TYPES_FIELD = 5
    WORD_NOTE_FIELD = 6
    WORD_USER_ADDED_FIELD = 7

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
                grammar_types text NOT NULL,
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

    __INSERT_STATEMENT = '''INSERT INTO words(english,romaji,kanji,chapter,grammar_types,note,user_added) 
                            VALUES(?,?,?,?,?,?,?)'''
    __VERSION_INSERT_STATEMENT = '''INSERT INTO version_info(version_major,version_minor,version_patch) VALUES(?,?,?)'''

    def __init__(self, db_path):
        if db_path is None or db_path is '':
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
            raise exceptions.DatabaseError('Can\'t setup version table without a connection!')

    def __setup_version_table(self):
        if self.db_conn is not None:
            try:
                cursor = self.db_conn.cursor()
                cursor.execute(self.__VERSION_INSERT_STATEMENT, (0, 1, 0))
                cursor.close()
            except sqlite3.Error as e:
                raise exceptions.DatabaseError('Error inserting version info:\n'+str(e))
        else:
            raise exceptions.DatabaseError('Can\'t setup version table without a connection!')

    def insert_word(self, word: Word, user_defined=False):
        """
        Inserts a new word into the Database. Note: If attempting to insert multiple words, use batch_insert() instead.
        :param word: The Word object representing the word to be inserted
        :param user_defined: A boolean representing if this word was made by the user or came from a default list
        """
        if self.db_conn is not None:
            try:
                cursor = self.db_conn.cursor()
                eng = '_'.join(word.english)
                grammar = '_'.join(word.grammar_types)
                word_tuple = (eng, word.romaji, word.kanji, word.chapter, grammar, word.note, 1 if user_defined else 0)
                cursor.execute(self.__INSERT_STATEMENT, word_tuple)
                cursor.close()
            except sqlite3.Error as e:
                raise exceptions.DatabaseError('Unable to insert word:\n'+str(e))
        else:
            raise exceptions.DatabaseError('Unable to insert word without a connection!')

    def batch_insert(self, words: List[Word], user_defined=False):
        try:
            cursor = self.db_conn.cursor()
            for word in words:
                eng = '_'.join(word.english)
                grammar = '_'.join(word.grammar_types)
                word_tuple = (eng, word.romaji, word.kanji, word.chapter, grammar, word.note, 1 if user_defined else 0)
                cursor.execute(self.__INSERT_STATEMENT, word_tuple)
            cursor.close()
        except sqlite3.Error as err:
            print('Error inserting new word into DB:')
            print(err)

    def fetch(self, whereclauses: Union[List[str], None] = None) -> List[Word]:
        """
        Returns a List object containing all the words in the database matching the passed SQL WHERE clause
        :param whereclauses: A List of strings representing the WHERE comparisons, not including the WHERE itself
        :return: A List of Word objects representing the words in the database that matched the request
        """
        word_list = []
        if self.db_conn is not None:
            cursor = self.db_conn.cursor()
            sql_statement = f'SELECT * FROM {self.__WORD_TABLE_NAME}'
            if whereclauses is not None:
                if len(whereclauses) is 1:
                    sql_statement += f' WHERE {whereclauses[0]}'
                else:
                    sql_statement += f' WHERE {whereclauses[0]}'
                    for clause in whereclauses[1:]:
                        sql_statement += f' AND {clause}'
            cursor.execute(sql_statement)
            raw_word_list = cursor.fetchall()
            cursor.close()
            for word in raw_word_list:
                # word[0] is omitted because it is merely the primary ID key of the database.
                # Kanji and Note are not guaranteed to exist, in which case they are 'None'
                kanji = None if word[self.WORD_KANJI_FIELD] is 'None' else word[self.WORD_KANJI_FIELD]
                note = None if word[self.WORD_NOTE_FIELD] is 'None' else word[self.WORD_NOTE_FIELD]
                eng = word[self.WORD_ENGLISH_FIELD].split('_')
                grammar = word[self.WORD_GRAMMAR_TYPES_FIELD].split('_')
                new_word = Word(eng, word[self.WORD_ROMAJI_FIELD], kanji, word[self.WORD_CHAPTER_FIELD], grammar, note)
                word_list.append(new_word)
            return word_list
        else:
            raise exceptions.DatabaseError('Can\'t fetch words without a connection!')

    def fetch_all(self) -> list:
        return self.fetch()


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
        default_words = []
        for word in default_wordbank.words:
            # We cheat a little bit here and don't set the hiragana or katakana since the DB will discard it anyway
            real_word = Word()
            real_word.english = word[default_wordbank.ENGLISH_INDEX].split('_')
            real_word.romaji = word[default_wordbank.ROMAJI_INDEX]
            real_word.kanji = word[default_wordbank.KANJI_INDEX]
            real_word.chapter = word[default_wordbank.CHAPTER_INDEX]
            real_word.grammar_types = word[default_wordbank.GRAMMAR_INDEX].split('_')
            real_word.note = word[default_wordbank.NOTE_INDEX]
            default_words.append(real_word)
        conn.batch_insert(default_words, False)
        return conn
    else:
        # Right now, we only have one version. Later we'll have to start checking the version number...
        return __DatabaseInterfaceV010(path)


# Initialized by init(), and used for all future operations on the words.
__database_connection = None


def init():
    global __database_connection
    __database_connection = __create_connection(__DATABASE_PATH)


def create_dictionary(chapters: Tuple[int, int] = None, grammar_types: Tuple[str, ...] = None) -> Dictionary:
    """
    Returns a new Dictionary that conforms to the passed parameters
    :param chapters: A 2-element Tuple defining the range (inclusive), or None for all chapters. Default value is None.
    :param grammar_types: A Tuple defining all the grammar types to filter by. Valid types are in
           default_wordbank.VALID_GRAMMAR_TYPES
    :return: A Dictionary object representing the filtered list of words.
    """
    if chapters is None and grammar_types is None:
        return Dictionary(__database_connection.fetch_all())
    else:
        clauses = []
        if chapters is not None:
            clauses.append(f'chapter BETWEEN {chapters[0]} AND {chapters[1]}')
        if grammar_types is not None:
            grammar_clause = '('
            grammar_clause += f'instr(grammar_types, \'{grammar_types[0]}\') > 0'
            if len(grammar_types) > 1:
                for grammar_type in grammar_types[1:]:
                    grammar_clause += f' OR instr(grammar_types, \'{grammar_types[0]}\') > 0'
            grammar_clause += ')'
            clauses.append(grammar_clause)
        return Dictionary(__database_connection.fetch(whereclauses=clauses))


if __name__ == '__main__':
    init()
    dict1 = create_dictionary()
    dict2 = create_dictionary(chapters=(3, 8))
    dict3 = create_dictionary(grammar_types=('adjective'))
    dict4 = create_dictionary(grammar_types=('い-adjective'))
    dict5 = create_dictionary(grammar_types=('noun', 'pronoun'))
    dict6 = create_dictionary(chapters=(0, 5), grammar_types=('pronoun'))
    print('All pronouns before chapter 6:')
    for current_word in dict6.wordlist:
        print(current_word.english, '|',
              current_word.romaji, '|',
              current_word.hiragana, '|',
              current_word.katakana, '|',
              current_word.kanji, '|',
              current_word.chapter, '|',
              current_word.grammar_types, '|',
              current_word.note)
    print('All nouns and pronouns')
    for current_word in dict5.wordlist:
        print(current_word.english, '|',
              current_word.romaji, '|',
              current_word.hiragana, '|',
              current_word.katakana, '|',
              current_word.kanji, '|',
              current_word.chapter, '|',
              current_word.grammar_types, '|',
              current_word.note)
    print('All い-adjectives only: ')
    for current_word in dict4.wordlist:
        print(current_word.english, '|',
              current_word.romaji, '|',
              current_word.hiragana, '|',
              current_word.katakana, '|',
              current_word.kanji, '|',
              current_word.chapter, '|',
              current_word.grammar_types, '|',
              current_word.note)
    print('All adjectives only:')
    for current_word in dict3.wordlist:
        print(current_word.english, '|',
              current_word.romaji, '|',
              current_word.hiragana, '|',
              current_word.katakana, '|',
              current_word.kanji, '|',
              current_word.chapter, '|',
              current_word.grammar_types, '|',
              current_word.note)
    print('Words in chapters 3 through 8:')
    for current_word in dict2.wordlist:
        print(current_word.english, '|',
              current_word.romaji, '|',
              current_word.hiragana, '|',
              current_word.katakana, '|',
              current_word.kanji, '|',
              current_word.chapter, '|',
              current_word.grammar_types, '|',
              current_word.note)
    print('All Words:')
    for current_word in dict1.wordlist:
        print(current_word.english, '|',
              current_word.romaji, '|',
              current_word.hiragana, '|',
              current_word.katakana, '|',
              current_word.kanji, '|',
              current_word.chapter, '|',
              current_word.grammar_types, '|',
              current_word.note)
