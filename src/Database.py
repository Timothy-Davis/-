import os
import sqlite3

import Dictionary
import default_wordbank


class Database:
    def __init__(self):
        self.TEST_DIR = os.path.expanduser('~/.config/nihongonogeimu/')
        if not os.path.exists(self.TEST_DIR):
            os.makedirs(self.TEST_DIR)

        self.TEST_FILE = self.TEST_DIR + 'wordbank.db'
        self.db_conn = None
        self.database_updated = False

        # Unlikely to ever change much, so stored in the class here
        self.__CREATE_TABLE_STATEMENTS = [
            '''CREATE TABLE IF NOT EXISTS words (
                    id integer PRIMARY KEY,
                    english text NOT NULL,
                    romaji text NOT NULL,
                    kanji text NOT NULL,
                    chapter integer NOT NULL,
                    note text
            );''',
        ]

        self.__connect_to_db()

    def __del__(self):
        print("Committing and Closing DB")
        if self.database_updated:
            self.db_conn.commit()
        if self.db_conn is not None:
            self.db_conn.close()

    def __connect_to_db(self):
        print('DB_FILE:', self.TEST_FILE)
        try:
            db_file_existed = os.path.exists(self.TEST_FILE)
            self.db_conn = sqlite3.connect(self.TEST_FILE)
            if not db_file_existed:
                print('Filling!')
                self.__fill_database_from_defaults()
        except sqlite3.Error as e:
            print('Error connecting to SQLite DB!')
            print(e)
            if self.db_conn is not None:
                self.db_conn.close()

    def __fill_database_from_defaults(self):
        self.__create_tables()
        self.__fill_data()
        self.database_updated = True

    def __create_tables(self):
        if self.db_conn is not None:
            try:
                for TABLE_STATEMENT in self.__CREATE_TABLE_STATEMENTS:
                    cursor = self.db_conn.cursor()
                    cursor.execute(TABLE_STATEMENT)
                    cursor.close()
            except sqlite3.Error as e:
                print('Error creating table(s):')
                print(e)

    def __fill_data(self):
        INSERT_STATEMENT = '''INSERT INTO words(english,romaji,kanji,chapter,note) VALUES(?,?,?,?,?)'''
        cursor = self.db_conn.cursor()
        try:
            for word in default_wordbank.words:
                cursor.execute(INSERT_STATEMENT, word)
        except sqlite3.Error as err:
            print("Error inserting new word into DB:")
            print(err)
        cursor.close()

    def load_all(self):
        word_list = None
        if self.db_conn is not None:
            word_list = []
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT * FROM words")
            raw_word_list = cursor.fetchall()
            cursor.close()
            for word in raw_word_list:
                # word[0] is omitted because it is merely the primary ID key of the database.
                # Kanji and Note are not guaranteed to exist, in which case they are 'None'
                kanji = None if word[3] is 'None' else word[3]
                note  = None if word[5] is 'None' else word[5]
                Dictionary.Word(word[1], word[2], kanji, word[4], note)
                word_list.append(Dictionary.Word(word[1], word[2], word[3], word[4], word[5]))
        return word_list


if __name__ == '__main__':
    db = Database()
    word_list = db.load_all()
    for word in word_list:
        print(word.english, '|',
              word.romaji, '|',
              word.hiragana, '|',
              word.katakana, '|',
              word.kanji, '|',
              word.chapter, '|',
              word.note)
