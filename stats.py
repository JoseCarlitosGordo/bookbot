def get_num_word(words_of_book):
    list_words = words_of_book.split()
    return len(list_words)

def list_character_occurrence(words_of_book):
    list_characters = {}
    for char in words_of_book.lower():
        if char not in list_characters:
            list_characters[char] = 1
        else:
            list_characters[char] += 1
    return list_characters

def sort_on(items):
    return items["num"]
def report(list_characters):
    sorted_list = [{"char": key, "num": value} for key, value in list_characters.items()]
    sorted_list.sort(key = sort_on, reverse = True)
    return sorted_list

