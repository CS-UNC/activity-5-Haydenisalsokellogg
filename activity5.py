def more_than_20(file):
    long_words = []
    words_file = open(file, 'r')

    for line in words_file:
        word = line.strip()  
        if len(word) > 20:
            long_words.append(word)

    words_file.close()
    return long_words


def has_no_e(word):
    return 'e' not in word.lower()

def uses_only(word, letters):
    for char in word:
        if char not in letters:
            return False
    return True


def all_uses_only(file, letters):
    valid_words = []
    words_file = open(file, 'r')

    for line in words_file:
        word = line.strip()
        if uses_only(word, letters):  
            valid_words.append(word)

    words_file.close()
    return valid_words
