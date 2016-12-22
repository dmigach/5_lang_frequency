import os
import chardet
import collections
import regex


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'rb') as file_handler:
        encoding = chardet.detect(file_handler.read())['encoding']
    with open(file_path, 'r', encoding=encoding) as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    NUMBER_OF_WORDS_TO_RETURN = 10
    words = regex.findall(r"[\p{L}]+", text.lower())
    return collections.Counter(words).most_common(NUMBER_OF_WORDS_TO_RETURN)


def print_most_frequent_words(words_array):
    for word, count in words_array:
        print('Word {} occurs {} time{}'.format(word, count,
                                                's' * (count != 1)))


if __name__ == '__main__':
    text_to_count = load_data(input('Enter file path\n'))
    if text_to_count is None:
        print('Wrong file path or file doesn\'t exist')
    else:
        top_ten_words = get_most_frequent_words(text_to_count)
        print_most_frequent_words(top_ten_words)
