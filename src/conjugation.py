import word_database
word_database.init()
words = word_database.create_dictionary(grammar_types=('い-adjective', 'な-adjective', 'う-verb', 'る-verb'))
print(words)
