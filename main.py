def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    
    total_words = len(file_contents.split())

    print(total_words)

main()
