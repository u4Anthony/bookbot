
def main():
    frankenstein_path = 'books/frankenstein.txt'
    frankenstein_content = get_book_content(frankenstein_path)
    frankenstein_word_count = get_word_count(frankenstein_content)
    print(f'{frankenstein_word_count} words found in {frankenstein_path}')

def get_word_count(contents):
    word_count = len(contents.split())
    return word_count

def get_book_content(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

if __name__ == '__main__':
    main()