from stats import get_book_text, word_count, count_letters, character_count, get_sorted_character_counts

import sys

if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def main():
    book_text = get_book_text(path)

    num_words = word_count(book_text)
    print(f"Found {num_words} total words")  # ← DO NOT CHANGE THIS LINE

    num_letters = count_letters(book_text)
    print(f"{num_letters} letters found in the document")

    print("--------- Character Count -------")
    sorted_chars_list = get_sorted_character_counts(character_count(book_text))

    for item in sorted_chars_list:
        char = item["char"]
        count = item["num"]

        # Only a–z allowed, no weird extended characters
        if char.isalpha() and char >= 'a' and char <= 'z':
            print(f"{char}: {count}")

if __name__ == "__main__":
    main()




    