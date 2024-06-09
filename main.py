
def main():
    frankenstein_path = 'books/frankenstein.txt'
    frankenstein_content = get_book_content(frankenstein_path)
    frankenstein_word_count = get_word_count(frankenstein_content)
    print(f'{frankenstein_word_count} words found in {frankenstein_path}')
    frankenstein_char_count = get_char_count(frankenstein_content)
    print(frankenstein_char_count)

def get_char_count(contents):
    char_count = {}
    for char in contents:
        lower_char = char.lower()
        if lower_char in char_count.keys():
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count

def get_word_count(contents):
    word_count = len(contents.split())
    return word_count

def get_book_content(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

if __name__ == '__main__':
    main()