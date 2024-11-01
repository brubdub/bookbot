def main():
    book_path = 'books/frankenstein.txt'
    text = get_book(book_path)
    total_words = get_num_words(text)
    char_counts = get_num_chars(text)
    sorted_char_counts = sort_chars(char_counts)

    print(f'\n--- Begin report of {book_path} ---\n')
    print(f'{total_words} words were found in the document\n')
    for char, count in sorted_char_counts.items():
        print(f"The '{char}' character was found {count} times")
    print(f'\n--- End report ---\n')

def get_num_words(text):
    words = text.split()

    return len(words)

def get_num_chars(text):
    chars_dict = {}
    for char in text.lower():
        if char.isalpha():
            if char in chars_dict:
                chars_dict[char] += 1
            elif char not in chars_dict:
                chars_dict[char] = 1

    return chars_dict

def sort_chars(num_chars):
    sorted_chars = dict(sorted(num_chars.items()))

    return sorted_chars

def get_book(path):
    with open(path) as f:

        return f.read()

main()
