from stats import get_num_words, get_num_chars, sort_dict
import sys


def get_book_text(filepath):
    file_string = ""
    with open(filepath) as f:
        file_string = f.read()

    return file_string


def main():
    filepath = ""
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(filepath)
    # print(text)
    chars_dict = get_num_chars(text)
    sorted_char_dict = sort_dict(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ---------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    for c in sorted_char_dict:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
        else:
            continue


main()
