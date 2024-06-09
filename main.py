
def main():
    frankenstein_path = 'books/frankenstein.txt'
    book_report(frankenstein_path)

def book_report(book_path):
    book_title = book_path.split('/')[1]
    book_content = get_book_content(book_path)
    book_word_count = get_word_count(book_content)
    book_char_count = get_char_count(book_content)
    print(f'--- Begin Report of Book: {book_title}')
    print(f'{book_word_count} words found.')
    for char, count in book_char_count.items():
        if char.isalpha():
            print(f'The \'{char}\' character was found {count} times.')
    print('--- End Book Report ---')

def value_getter(item):
    return item[1]

def get_char_count(contents):
    unsorted_char_count = {}
    char_count = {}
    for char in contents:
        lower_char = char.lower()
        if lower_char in unsorted_char_count.keys():
            unsorted_char_count[lower_char] += 1
        else:
            unsorted_char_count[lower_char] = 1
    sorted_char_count = sorted(unsorted_char_count.items(), key=value_getter, reverse=True)
    for char, count in sorted_char_count:
        char_count[char] = count
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