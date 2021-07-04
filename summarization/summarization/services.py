import stopwords_manager
import utils

from collections import defaultdict


MIN_OCCURRENCE_PERCENTAGE = 0.05 
MAX_OCCURRENCE_PERCENTAGE = 0.5


def preprocessing(text, language_code):
    stopwords = stopwords_manager.get_stoplist(language_code)
    return " ".join(
                    filter(
                            lambda sub: sub not in stopwords, text.split()))


def get_keywords(words):
    counting_dict = defaultdict(int)
    for word in words:
        counting_dict[word] += 1

    keywords = set()
    len_words = len(words)
    for word, occurrences in counting_dict.items():
        occurrence_percentage = occurrences / len_words
        if (occurrence_percentage <= MAX_OCCURRENCE_PERCENTAGE 
            and occurrence_percentage >= MIN_OCCURRENCE_PERCENTAGE):
            keywords.add(word)

    return keywords


def get_sentence_weight(sentence, keywords):
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


def get_list_sentence_weight(preprocessing_text, sentences):
    list_sentence_weight = defaultdict(float)
    words = utils.get_words(preprocessing_text)
    keywords = get_keywords(words)

    for sentence in sentences:
        sentence_weight = get_sentence_weight(sentence , keywords)
        list_sentence_weight[sentence] = sentence_weight

    result = dict(sorted(
                        list_sentence_weight.items(), key = lambda x: (x[1], x[0]), 
                        reverse = True))
    return result.keys()


def summarize_sentences(
            sentences, list_sentence_weight, 
            number_of_sentences):
    real_sentences = min(number_of_sentences, len(sentences))
    result = ""
    i = 0
    for content in list_sentence_weight:
        if i < real_sentences:
            result += content + "\n"
        else:
            break
        i += 1
    return result