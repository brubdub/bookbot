from collections import Counter

def main():
    book_path = 'books/frankenstein.txt'
    text = get_book(book_path)
    total_words = get_num_words(text)
    char_counts = get_num_chars(text)

    print(f'{total_words} words were found in the document.')
    print('Here are the counts for all the characters:')
    for char, count in char_counts.items():
        print(f'{char} : {count}')

def get_num_words(text):
    words = text.split()

    return len(words)

def get_num_chars(text):
    chars = sorted(list(text.lower()))
    char_counts = Counter(chars)
    
    return char_counts

def get_book(path):
    with open(path) as f:
        return f.read()

main()
