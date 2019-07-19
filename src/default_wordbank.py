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
#   0. All words, english included, should be in lowercase.
#   1. The exceptions to the above rule are the special case of 'None', and the note field.
#   2. If a word has multiple english meanings, separate them with an underscore.
#   3. If a word has multiple grammar types, separate them with an underscore.
#   4. All Grammar Types are innumerated in VALID_GRAMMAR_TYPES. Make sure your type belongs, or add it.
#   5. If a word has no kanji, use the string literal 'None'
#   6. If a word does not have a chapter in Genki, use 0
#   7. If there is no note to be made about the word, use the string literal 'None'

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
    'adverb',
    'preposition',
    'adjective',
    'い-adjective',
    'な-adjective',
    'う-verb',
    'る-verb',
    'exclamation',
    'prefix',
    'suffix',
    'counter',
    'honorific',
    'expression',

    'uncertain',  # Use this when you /think/ you know the kind, but are unsure. Should be first in the list.
    'unclassified',  # Use this if you don't even have a guess.
]

words = [
    ('good morning', 'ohayou', 'お早う', 1, 'expression', 'Usually written using only kana, though the kanji is used '
                                         'for abbreviation sometimes.'),
    ('good morning', 'ohayougozaimasu', 'お早うございます', 1, 'expression', 'See note for "お早う"'),
    ('good afternoon', 'konnichiha', '今日は', 1, 'expression', 'Usually written using only kana'),
    ('good evening', 'konbanha', '今晩は', 1, 'expression', 'Usually written using only kana'),
    ('goodbye', 'sayonara', 'None', 1, 'expression', 'Only used when you expect to never see a person again!'),
    ('goodnight', 'oyasuminasai', 'お休みなさい', 1, 'expression', 'Generally written with kana alone. The nasai is '
                                                                     'important, as it can otherwise be interpretted to'
                                                                     ' mean holiday!'),
    ('thank you', 'arigatou', '有り難う', 1, 'expression', 'Usually written with only kana.'),
    ('thank you', 'arigatougozaimasu', '有難うございます', 1, 'expression', 'Usually written with only kana.'),
    ('excuse me_i\'m sorry', 'sumimasen', '済みませ', 1, 'expression', 'Usually written with kana alone.'),
    ('no_not at all', 'iie', 'None', 1, 'unclassified', 'None'),
    ('i will go and come back', 'ittekimasu', '行ってきます', 1, 'expression', 'Usually written with kana alone. Often '
                                                                               'replied to with 行ってらっしゃい'),
    ('please go and come back', 'itterasshai', '行ってらっしゃい', 1, 'expression', 'Usually written with kana alone. '
                                                                                    'Often said in response to '
                                                                                    '行ってきます.'),
    ('just now_i\'m home_presently_right now', 'tadaima', 'ただ今', 1, 'expression_noun_adverb', 'None'),
    ('welcome home', 'okaerinasai', 'お帰りなさい', 1, 'expression', 'None'),
    ('thank you for the meal', 'itadakimasu', '頂ますよう', 1, 'expression', 'Usually written with kana alone. Said '
                                                                             'before the meal begins.'),
    ('thank you for the meal', 'gochisousamadeshita', 'ご馳走様でした', 1, 'expression', 'Usually written with kana '
                                                                                         'alone.'),
    ('nice to meet you_how do you do', 'hajimemashite', '初めまして', 1, 'expression', 'Usually written with kana '
                                                                                       'alone.'),
    ('please treat me well_please remember me', 'yoroshikuonegaishimasu', 'よろしくお願いします', 1, 'expression',
                                                                                                     'None'),
    ('um...', 'ano', 'None', 1, 'unclassified', 'None'),
    ('now', 'ima', '今', 1, 'noun', 'None'),
    ('english', 'eigo', '英語', 1, 'noun', 'None'),
    ('yes', 'ee', 'None', 1, 'unclassified', 'None'),
    ('student', 'gakusei', '学生', 1, 'noun', 'None'),
    ('language_...language', 'go', '語', 1, 'suffix', 'None'),
    ('high school', 'koukou', '高校', 1, 'noun', 'None'),
    ('a.m.', 'gozen', '午前', 1, 'noun', 'None'),
    ('p.m.', 'gogo', '午後', 1, 'noun', 'None'),
    ('years old_...years old', 'sai', '歳', 1, 'suffix_counter', 'Sometimes seen as 才, due to writing '
                                                                 'difficulty'),
    ('mr._ms._mrs.', 'san', 'None', 1, 'honorific', 'Cannot be used to refer to one\'s self.'),
    ('o\'clock_...o\'clock_hour', 'ji', '時', 1, 'noun_suffix', 'None'),
    ('people_...person', 'jin', '人', 1, 'suffix', 'None'),
    ('major_field of study', 'senkou', '先行', 1, 'noun', 'None'),
    ('teacher_professor', 'sensei', '先生', 1, 'pronoun_honorific', 'Can also be used to describe a master of a craft.'),
    ('that\'s right', 'soudesu', 'None', 1, 'expression', 'None'),
    ('i see_is that so?', 'soudesuka', 'None', 1, 'expression', 'None'),
    ('college_university', 'daigaku', '大学', 1, 'noun', 'None'),
    ('telephone', 'denwa', '電話', 1, 'noun', 'Deri'),
    ('friend', 'tomodachi', '友達', 1, 'noun', 'None'),
    ('name', 'namae', '名前', 1, 'noun', 'None'),
    ('what', 'nani', '何', 1, 'noun', 'None'),
    ('japan', 'nihon', '日本', 1, 'noun', 'None'),
    ('...year student_year student', 'nensei', '年生', 1, 'suffix_noun', 'Grammatically, this is a noun that is only '
                                                                         'ever used as a suffix.'),
    ('yes', 'hai', 'None', 1, 'unclassified', 'None'),
    ('half', 'han', '半', 1, 'noun', 'None'),  # Yes, apparently. According to https://jisho.org, half is a noun.
    ('number', 'bangou', '番号', 1, 'noun', 'None'),
    ('international student', 'ryuugakusei', '留学生', 1, 'noun', 'None'),
    ('i', 'watashi', '私', 1, 'pronoun', 'None'),
    ('america', 'amerika', 'None', 1, 'noun', 'None'),
    ('britain', 'igirisu', 'None', 1, 'noun', 'None'),
    ('australia', 'oosutoraria', 'None', 1, 'noun', 'None'),
    ('korea', 'kankoku', '韓国', 1, 'noun', 'None'),
    ('sweden', 'suweeden', 'None', 1, 'noun', 'None'),
    ('china', 'chuugoku', '中国', 1, 'noun', 'None'),
    ('science', 'kagaku', '科学', 1, 'noun', 'None'),
    ('asian studies', 'ajiakenkyuu', 'アジア研究', 1, 'noun', 'None'),
    ('economics', 'keizai', '経済', 1, 'noun', 'None'),
    ('international relations', 'kokusaikankei', '国際関係', 1, 'noun', 'None'),
    ('computer science', 'konpyuutaa', 'None', 1, 'noun', 'None'),
    ('anthropology', 'jinruigaku', '人類学', 1, 'noun', 'None'),
    ('politics', 'seiji', '正常', 1, 'noun', 'None'),
    ('business', 'bijinesu', 'None', 1, 'noun', 'None'),
    ('literature', 'bungaku', '文学', 1, 'noun', 'None'),
    ('history', 'rekishi', '歴史', 1, 'noun', 'None'),
    ('job_work_occupation', 'shigoto', '仕事', 1, 'noun', 'None'),
    ('doctor_medical doctor', 'isha', '医者', 1, 'noun', 'None'),
    ('office worker_company employee', 'kaishain', '会社員', 1, 'noun', 'None'),
    ('high school student', 'koukousei', '高校生', 1, 'noun', 'None'),
    ('housewife', 'shufu', '主婦', 1, 'noun', 'None'),
    ('graduate student', 'daigakuinsei', '大学院生', 1, 'noun', 'None'),
    ('college student', 'daigakusei', '大学生', 1, 'noun', 'None'),
    ('lawyer', 'bengoshi', '弁護士', 1, 'noun', 'None'),
    ('mother', 'okaasan', 'お母さん', 1, 'noun', 'None'),
    ('father', 'otousan', 'お父さん', 1, 'noun', 'None'),
    ('older sister', 'oneesan', 'お姉さん', 1, 'noun', 'None'),
    ('older brother', 'oniisan', 'お兄さん', 1, 'noun', 'None'),
    ('younger sister', 'imouto', '妹', 1, 'noun', 'None'),
    ('younger brother', 'otouto', '弟', 1, 'noun', 'None'),

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
    ('educational kanji', 'kyouikukanji', '教育漢字', 0, 'noun', 'The name given to the list of kanji maintained by the'
                                                                ' Japanese Ministry of Education that must be taught to'
                                                                ' primary school children in Japan. It consists of 1006'
                                                                ' different kanji.'),
    ('primary school pupil_child', 'jidou', '児童', 0, 'noun', 'None'),
    ('primary student_primary school student', 'shougakusei', '小学生', 0, 'noun', 'Literally, "small student"'),
    ('middle school student', 'chuugakusei', '中学生', 0, 'noun', 'Literally, "middle student"'),
    ('high school student', 'koukousei', '高校生', 0, 'noun', 'None'),
    ('college student', 'daigakusei', '大学生', 0, 'noun', 'Literally, "big stduent"'),
    ('graduate student', 'daigakuinsei', '大学院生', 0, 'noun', 'None'),
    ('student id card', 'gakuseishou', '学生証', 0, 'noun', 'None'),
    ('junior high_junior high school', 'chuugakkou', '中学校', 0, 'noun', 'None'),
    ('senior high_senior high school', 'koutougakkou', '高等学校', 0, 'noun', 'Often abbreviated to 高校'),
    ('pupil', 'seito', '生徒', 0, 'noun', 'Can describe a student up to and including high school, but not past that.'),
]

def list_unclassified():
    print("The following words have an unclassified grammar type:")
    for word in words:
        if 'unclassified' in word[GRAMMAR_INDEX].split('_'):
            print(word)
    print("The following words have an uncertain grammar type:")
    for word in words:
        if 'uncertain' in word[GRAMMAR_INDEX].split('_'):
            print(word)

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
    print('Now printing inconsistently classified words:')
    list_unclassified()
