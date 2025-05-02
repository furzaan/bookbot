import sys
from stats import count_words, count_characters, sorted_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print(count_words(book_path))
    count_dict = count_characters(book_path)

    sorted_chars = sorted_dict(count_dict)

    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict['num']}")
    
main()