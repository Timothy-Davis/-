import Dictionary


def load_all() -> list:
    """
    Loads all the words from the database into a list of Word objections, as defined in the Dictionary module.
    :return: A list containing all Word objects in the database
    """
    words = [
        Dictionary.Word(['cold'], 5, 'samui', 'さむい', 'サムイ', '寒い'),
        Dictionary.Word(['hot'], 5, 'atsui', 'あつい', 'アツい', '暑い', note='Hot Weather'),
        Dictionary.Word(['hot'], 5, 'atsui', 'あつい', 'アツい', '熱い', note='Hot to the Touch'),
        Dictionary.Word(['thick'], 0, 'atsui', 'あつい', 'アツい', '厚い', note='Thick'),
        Dictionary.Word(['deep', 'strong'], 0, 'atsui', 'あつい', 'アツい', '篤い', note='Deep or Strong'),
        Dictionary.Word(['this one'], 2, 'kore', 'これ', 'コレ', None),
        Dictionary.Word(['my older sister'], 7, 'ane', 'あ', 'アネ', '姉'),
        Dictionary.Word(['job', 'work', 'occupation'], 8, 'shigoto', 'しごと', 'シゴト', '仕事'),
        Dictionary.Word(['winter'], 8, 'fuyu', 'ふゆ', 'フユ', '冬'),
        Dictionary.Word(['to take medicine'], 9, 'kusuriwonomu', 'くすりをのむ', 'クスリヲノム', '薬を飲む'),
    ]

    return words
