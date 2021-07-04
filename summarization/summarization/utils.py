import os
import re

def init_results_dir():
    dir = 'results'
    if not os.path.exists(dir):
        os.makedirs(dir)


def dump_file(str_content, filename):
    with open("results/" + filename, "w") as f:
        f.write(str_content)


def load_text(filename):
    return " ".join(list(
                        map(
                            lambda word: word.strip(), open(filename))))


def get_sentences(text):
    return text.split('.')


def get_words(text):
    only_words_text = re.compile(r'[^0-9^a-z^A-Z\s]').sub('', text)
    return only_words_text.split(' ')


def get_text_from_file (filename):
    with open(filename , 'r') as myfile:
        text = myfile.read().replace('\n','')
    return text