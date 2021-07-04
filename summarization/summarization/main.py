import utils
import services


if __name__ == "__main__":
    text = utils.get_text_from_file("words.txt")

    preprocessing_text = services.preprocessing(text, "vi")

    sentences = utils.get_sentences(preprocessing_text)
    list_sentence_weight = services.get_list_sentence_weight(preprocessing_text, sentences)

    summarization = services.summarize_sentences(
                                                sentences, list_sentence_weight, 
                                                number_of_sentences = 10)

    utils.dump_file(summarization, "result.txt")
