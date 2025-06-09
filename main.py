import sys
from stats import get_num_of_words, get_count_of_chars, get_sorted_dict


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    content = get_book_text(file_path)

    num_words = get_num_of_words(content)

    num_chars = get_count_of_chars(content)

    char_frequency_report = get_sorted_dict(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key in char_frequency_report:
        print(f"{key}: {char_frequency_report[key]}")
    print("============= END ===============")

main()