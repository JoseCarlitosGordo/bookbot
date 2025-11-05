from stats import get_num_word, list_character_occurrence

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_word(text)
    print(f"Found {num_words} total words")
    print(list_character_occurrence(text))


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


main()