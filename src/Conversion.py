def romaji_to_hiragana(s):
    if s == '':
        return s

    for char in s:
        # vowels fist, and the special boy ん
        if s[0] == 'a':
            return 'あ' + romaji_to_hiragana(s[1:])
        elif s[0] == 'i':
            return 'い' + romaji_to_hiragana(s[1:])
        elif s[0] == 'u':
            return 'う' + romaji_to_hiragana(s[1:])
        elif s[0] == 'e':
            return 'え' + romaji_to_hiragana(s[1:])
        elif s[0] == 'o':
            return 'お' + romaji_to_hiragana(s[1:])
        elif s[0] == 'n' and len(s) == 1:
            return 'ん' + romaji_to_hiragana(s[1:])

        # Since it would otherwise break the elif chain, this elif must be responsible for returning the
        # character resulting from 'n' being its first letter.
        elif s[0] == 'n' and len(s) > 1:
            if s[1] != 'a' and s[1] != 'i' and s[1] != 'u' and s[1] != 'e' and s[1] != 'o' and s[1] != 'y':
                return 'ん' + romaji_to_hiragana(s[1:])
            elif s[0] == 'n' and s[1] == 'a':
                return 'な' + romaji_to_hiragana(s[2:])
            elif s[0] == 'n' and s[1] == 'i':
                return 'に' + romaji_to_hiragana(s[2:])
            elif s[0] == 'n' and s[1] == 'u':
                return 'ぬ' + romaji_to_hiragana(s[2:])
            elif s[0] == 'n' and s[1] == 'e':
                return 'ね' + romaji_to_hiragana(s[2:])
            elif s[0] == 'n' and s[1] == 'o':
                return 'の' + romaji_to_hiragana(s[2:])
            elif s[0] == 'n' and len(s) == 1:
                return 'ん' + romaji_to_hiragana(s[1:])

            elif s[0] == 'n' and s[1] == 'y' and s[2] == 'a':
                return 'にゃ' + romaji_to_hiragana(s[3:])
            elif s[0] == 'n' and s[1] == 'y' and s[2] == 'u':
                return 'にゅ' + romaji_to_hiragana(s[3:])
            elif s[0] == 'n' and s[1] == 'y' and s[2] == 'o':
                return 'にょ' + romaji_to_hiragana(s[3:])

        # Now characters with small ya, yu, or yo
        elif s[0] == 'k' and s[1] == 'y' and s[2] == 'a':
            return 'きゃ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'k' and s[1] == 'y' and s[2] == 'u':
            return 'きゅ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'k' and s[1] == 'y' and s[2] == 'o':
            return 'きょ' + romaji_to_hiragana(s[3:])

        elif s[0] == 'g' and s[1] == 'y' and s[2] == 'a':
            return 'ぎゃ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'g' and s[1] == 'y' and s[2] == 'u':
            return 'ぎゅ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'g' and s[1] == 'y' and s[2] == 'o':
            return 'ぎょ' + romaji_to_hiragana(s[3:])

        elif s[0] == 's' and s[1] == 'h' and s[2] == 'a':
            return 'しゃ' + romaji_to_hiragana(s[3:])
        elif s[0] == 's' and s[1] == 'h' and s[2] == 'u':
            return 'しゅ' + romaji_to_hiragana(s[3:])
        elif s[0] == 's' and s[1] == 'h' and s[2] == 'o':
            return 'しょ' + romaji_to_hiragana(s[3:])

        elif s[0] == 'j' and s[1] == 'a':
            return 'じゃ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'j' and s[1] == 'u':
            return 'じゅ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'j' and s[1] == 'o':
            return 'じょ' + romaji_to_hiragana(s[2:])

        elif s[0] == 'z' and s[1] == 'a':
            return 'じゃ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'z' and s[1] == 'u':
            return 'じゅ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'z' and s[1] == 'o':
            return 'じょ' + romaji_to_hiragana(s[2:])

        elif s[0] == 'c' and s[1] == 'h' and s[2] == 'a':
            return 'ちゃ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'c' and s[1] == 'h' and s[2] == 'u':
            return 'ちゅ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'c' and s[1] == 'h' and s[2] == 'o':
            return 'ちょ' + romaji_to_hiragana(s[3:])

        elif s[0] == 'm' and s[1] == 'y' and s[2] == 'a':
            return 'みゃ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'm' and s[1] == 'y' and s[2] == 'u':
            return 'みゅ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'm' and s[1] == 'y' and s[2] == 'o':
            return 'みょ' + romaji_to_hiragana(s[3:])

        elif s[0] == 'h' and s[1] == 'y' and s[2] == 'a':
            return 'ひゃ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'h' and s[1] == 'y' and s[2] == 'u':
            return 'ひゅ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'h' and s[1] == 'y' and s[2] == 'o':
            return 'ひょ' + romaji_to_hiragana(s[3:])

        elif s[0] == 'b' and s[1] == 'y' and s[2] == 'a':
            return 'びゃ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'b' and s[1] == 'y' and s[2] == 'u':
            return 'びゅ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'b' and s[1] == 'y' and s[2] == 'o':
            return 'びょ' + romaji_to_hiragana(s[3:])

        elif s[0] == 'p' and s[1] == 'y' and s[2] == 'a':
            return 'ぴゃ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'p' and s[1] == 'y' and s[2] == 'u':
            return 'ぴゅ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'p' and s[1] == 'y' and s[2] == 'o':
            return 'ぴょ' + romaji_to_hiragana(s[3:])

        elif s[0] == 'r' and s[1] == 'y' and s[2] == 'a':
            return 'りゃ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'r' and s[1] == 'y' and s[2] == 'u':
            return 'りゅ' + romaji_to_hiragana(s[3:])
        elif s[0] == 'r' and s[1] == 'y' and s[2] == 'o':
            return 'りょ' + romaji_to_hiragana(s[3:])

        # Christ, that's a big statement. Here's the default case, i.e. nothing special.
        elif s[0] == 'k' and s[1] == 'a':
            return 'か' + romaji_to_hiragana(s[2:])
        elif s[0] == 'k' and s[1] == 'i':
            return 'き' + romaji_to_hiragana(s[2:])
        elif s[0] == 'k' and s[1] == 'u':
            return 'く' + romaji_to_hiragana(s[2:])
        elif s[0] == 'k' and s[1] == 'e':
            return 'け' + romaji_to_hiragana(s[2:])
        elif s[0] == 'k' and s[1] == 'o':
            return 'こ' + romaji_to_hiragana(s[2:])

        elif s[0] == 's' and s[1] == 'a':
            return 'さ' + romaji_to_hiragana(s[2:])
        elif s[0] == 's' and s[1] == 'h' and s[2] == 'i':
            return 'し' + romaji_to_hiragana(s[3:])
        elif s[0] == 's' and s[1] == 'u':
            return 'す' + romaji_to_hiragana(s[2:])
        elif s[0] == 's' and s[1] == 'e':
            return 'せ' + romaji_to_hiragana(s[2:])
        elif s[0] == 's' and s[1] == 'o':
            return 'そ' + romaji_to_hiragana(s[2:])

        elif s[0] == 't' and s[1] == 'a':
            return 'た' + romaji_to_hiragana(s[2:])
        elif s[0] == 'c' and s[1] == 'h' and s[2] == 'i':
            return 'ち' + romaji_to_hiragana(s[3:])
        elif s[0] == 't' and s[1] == 's' and s[2] == 'u':
            return 'つ' + romaji_to_hiragana(s[3:])
        elif s[0] == 't' and s[1] == 'e':
            return 'て' + romaji_to_hiragana(s[2:])
        elif s[0] == 't' and s[1] == 'o':
            return 'と' + romaji_to_hiragana(s[2:])

        elif s[0] == 'h' and s[1] == 'a':
            return 'は' + romaji_to_hiragana(s[2:])
        elif s[0] == 'h' and s[1] == 'i':
            return 'ひ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'h' and s[1] == 'u':
            return 'ふ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'f' and s[1] == 'u':
            return 'ふ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'h' and s[1] == 'e':
            return 'へ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'h' and s[1] == 'o':
            return 'ほ' + romaji_to_hiragana(s[2:])

        elif s[0] == 'm' and s[1] == 'a':
            return 'ま' + romaji_to_hiragana(s[2:])
        elif s[0] == 'm' and s[1] == 'i':
            return 'み' + romaji_to_hiragana(s[2:])
        elif s[0] == 'm' and s[1] == 'u':
            return 'む' + romaji_to_hiragana(s[2:])
        elif s[0] == 'm' and s[1] == 'e':
            return 'め' + romaji_to_hiragana(s[2:])
        elif s[0] == 'm' and s[1] == 'o':
            return 'も' + romaji_to_hiragana(s[2:])

        elif s[0] == 'y' and s[1] == 'a':
            return 'や' + romaji_to_hiragana(s[2:])
        elif s[0] == 'y' and s[1] == 'u':
            return 'ゆ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'y' and s[1] == 'o':
            return 'よ' + romaji_to_hiragana(s[2:])

        elif s[0] == 'r' and s[1] == 'a':
            return 'ら' + romaji_to_hiragana(s[2:])
        elif s[0] == 'r' and s[1] == 'i':
            return 'り' + romaji_to_hiragana(s[2:])
        elif s[0] == 'r' and s[1] == 'u':
            return 'る' + romaji_to_hiragana(s[2:])
        elif s[0] == 'r' and s[1] == 'e':
            return 'れ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'r' and s[1] == 'o':
            return 'ろ' + romaji_to_hiragana(s[2:])

        elif s[0] == 'w' and s[1] == 'a':
            return 'わ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'w' and s[1] == 'o':
            return 'を' + romaji_to_hiragana(s[2:])

        # Almost done, now we have dialectical marks i.e. dakuten and handakuten.
        elif s[0] == 'g' and s[1] == 'a':
            return 'が' + romaji_to_hiragana(s[2:])
        elif s[0] == 'g' and s[1] == 'i':
            return 'ぎ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'g' and s[1] == 'u':
            return 'ぐ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'g' and s[1] == 'e':
            return 'げ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'g' and s[1] == 'o':
            return 'ご' + romaji_to_hiragana(s[2:])

        elif s[0] == 'z' and s[1] == 'a':
            return 'ざ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'j' and s[1] == 'i':
            return 'じ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'z' and s[1] == 'i':
            return 'じ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'z' and s[1] == 'u':
            return 'ず' + romaji_to_hiragana(s[2:])
        elif s[0] == 'z' and s[1] == 'e':
            return 'ぜ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'z' and s[1] == 'o':
            return 'ぞ' + romaji_to_hiragana(s[2:])

        elif s[0] == 'd' and s[1] == 'a':
            return 'だ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'd' and s[1] == 'i':
            return 'ぢ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'd' and s[1] == 'u':
            return 'づ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'd' and s[1] == 'e':
            return 'で' + romaji_to_hiragana(s[2:])
        elif s[0] == 'd' and s[1] == 'o':
            return 'ど' + romaji_to_hiragana(s[2:])

        elif s[0] == 'b' and s[1] == 'a':
            return 'ば' + romaji_to_hiragana(s[2:])
        elif s[0] == 'b' and s[1] == 'i':
            return 'び' + romaji_to_hiragana(s[2:])
        elif s[0] == 'b' and s[1] == 'u':
            return 'ぶ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'b' and s[1] == 'e':
            return 'べ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'b' and s[1] == 'o':
            return 'ぼ' + romaji_to_hiragana(s[2:])

        elif s[0] == 'p' and s[1] == 'a':
            return 'ぱ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'p' and s[1] == 'i':
            return 'ぴ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'p' and s[1] == 'u':
            return 'ぷ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'p' and s[1] == 'e':
            return 'ぺ' + romaji_to_hiragana(s[2:])
        elif s[0] == 'p' and s[1] == 'o':
            return 'ぽ' + romaji_to_hiragana(s[2:])

        # Last but not least, if there is a consonant followed by the same consonant, we will replace the first with 'っ'
        elif s[0] == s[1]:
            return 'っ' + romaji_to_hiragana(s[1:])


if __name__ == '__main__':
    import os
    romaji = input('Enter some romaji [q to quit]: ').lower()
    while romaji is not 'q':
        print(romaji_to_hiragana(romaji))
        romaji = input('Enter some romaji [q to quit]: ').lower()
