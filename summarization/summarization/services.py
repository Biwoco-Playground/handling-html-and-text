import stopwords_manager
import utils

from collections import defaultdict


MIN_OCCURRENCE_PERCENTAGE = 0.05 # Min occurrence percentage of a word
MAX_OCCURRENCE_PERCENTAGE = 0.5 # Max occurrence percentage of a word


def preprocessing(text, language_code):
    """Preprocessing text
    
    Keyword arguments:
    text(str) -- the string split
    language_code(str) -- the string of language code(Ex: en, vi, fr,...)

    Returns:
    str: the processed string

    """

    stopwords = stopwords_manager.get_stopwords(language_code)
    return " ".join(
                    filter(
                            lambda sub: sub not in stopwords, text.split()))


def get_keywords(preprocessed_text):
    """Get keywords
    
    Keyword arguments:
    preprocessed_text(str) -- the processed string(Let's see preprocessing.__doc__)

    Returns:
    set(str): the set of words in preprocessed_text argument have occurrence percentage 
    between MIN and MAX

    """

    counting_dict = defaultdict(int)
    for word in preprocessed_text:
        counting_dict[word] += 1

    keywords = set()
    len_preprocessed_text = len(preprocessed_text)
    for word, occurrences in counting_dict.items():
        occurrence_percentage = occurrences / len_preprocessed_text
        if (occurrence_percentage <= MAX_OCCURRENCE_PERCENTAGE 
            and occurrence_percentage >= MIN_OCCURRENCE_PERCENTAGE):
            keywords.add(word)

    return keywords


def get_sentence_weight(sentence, keywords):
    """Get sentence weight
    
    Keyword arguments:
    sentence(str) -- sentence from text(Ex: "Hello Hi. World." 
                    -> Require "Hello Hi" or "World")
    keywords(set) -- set of keywords(Let's see get_keywords.__doc__)

    Returns:
    float: weight of sentence

    """

    sentence_split = sentence.split()
    len_sentence_split = len(sentence_split)

    index = 0
    flag = True
    window_start = 0
    while (flag
        and index < len_sentence_split):
        if sentence_split[index] in keywords:
            window_start = index
            flag = False
        index += 1

    index = len_sentence_split - 1
    flag = True
    window_end = -1
    while (flag
        and index >= window_start):
        if sentence_split[index] in keywords:
            window_end = index
            flag = False
        index -= 1

    if window_start > window_end:
        return 0
    else:
        window_size = window_end - window_start + 1
        keywords_occurrences = 0
        for word in sentence_split:
            if word in keywords:
                keywords_occurrences += 1

        return keywords_occurrences**2 / window_size


def get_set_of_sentence_weights(preprocessed_text, sentences):
    """Get set of sentence weights
    
    Keyword arguments:
    preprocessed_text(str) -- the preprocessed text
    sentences(list): list of sentences in text 

    Returns:
    set(float): set of sentence weights

    """

    list_sentence_weight = defaultdict(float)
    words = utils.get_words(preprocessed_text)
    keywords = get_keywords(words)

    for sentence in sentences:
        sentence_weight = get_sentence_weight(sentence , keywords)
        list_sentence_weight[sentence] = sentence_weight

    result = dict(sorted(
                        list_sentence_weight.items(), key = lambda x: (x[1], x[0]), 
                        reverse = True))
    return result.keys()


def summarize_sentences(
            sentences, set_of_sentence_weights, 
            number_of_sentences):
    """Summarize sentences
    
    Keyword arguments:
    sentences(list(str)) -- list of sentences(Let's see get_sentences.__doc__)
    set_of_sentence_weights(set(float)) -- set of sentence weights
                                        (Let's see get_set_of_sentence_weights.__doc__)
    number_of_sentences(int) -- the number of sentences as output

    Returns:
    str: the summarized string

    """
    
    real_sentences = min(number_of_sentences, len(sentences))
    result = ""
    i = 0
    for content in set_of_sentence_weights:
        if i < real_sentences:
            result += content + "\n"
        else:
            break
        i += 1
    return result