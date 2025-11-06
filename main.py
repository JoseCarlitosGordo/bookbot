from stats import get_num_word, list_character_occurrence, report
import sys
def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    text = get_book_text(sys.argv[1])
    num_words = get_num_word(text)
    print(f"Found {num_words} total words")
    character_occurences = list_character_occurrence(text)
    print(character_occurences)
    data = report(character_occurences)
    print("--------- Character Count -------")
    for item in data:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
            
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


main()
