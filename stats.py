def get_num_word(words_of_book):
    list_words = words_of_book.split()
    return len(list_words)

def list_character_occurrence(words_of_book):
    words_of_book = words_of_book.lower()
    list_characters = {}
    for char in words_of_book:
        if char not in list_characters:
            list_characters[char] = 0
        else:
            list_characters[char] += 1
        return list_characters