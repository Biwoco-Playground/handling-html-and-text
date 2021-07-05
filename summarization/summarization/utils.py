import os
import re

def init_results_dir():
    ''' Create a directory named results.'''

    dir = 'results'
    if not os.path.exists(dir):
        os.makedirs(dir)


def dump_file(str_content, filename):
    """Dump string to file in results directory.
    
    Keyword arguments:
    str_content(str) -- the string is dumped
    filename(str) -- the filename with file format(Ex: article.txt, article.json,... )

    """

    with open("results/" + filename, "w") as f:
        f.write(str_content)


def load_text(filename):
    """Load string content from file.

    Keyword arguments:
    filename(str) -- the filename with file format(Ex: article.txt, article.json,... )

    Returns:
    str: string content from file
    
    """

    return " ".join(list(
                        map(
                            lambda word: word.strip(), open(filename))))


def get_sentences(text):
    """Get sentences from text

    Keyword arguments:
    text(str) -- the string split

    Returns:
    list(str): list of sentences in text 
    

    """
    
    return text.split('.')


def get_words(text):
    """Get words from text(symbols are excluded) 
    
    Keyword arguments:
    text(str) -- the string split

    Returns:
    list(str): list of words in text(Ex: "ab. cd12! efg!!" -> ['ab', 'cd12', 'efg'])
    
    """

    only_words_text = re.compile(r'[^0-9^a-z^A-Z\s]').sub('', text)
    return only_words_text.split(' ')