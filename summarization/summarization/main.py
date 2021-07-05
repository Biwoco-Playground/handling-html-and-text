import utils
import services


if __name__ == "__main__":
    text = utils.load_text("words.txt")

    preprocessed_text = services.preprocessing(text, "vi")

    sentences = utils.get_sentences(preprocessed_text)
    set_of_sentence_weights = services.get_set_of_sentence_weights(preprocessed_text, sentences)

    summarization = services.summarize_sentences(
                                                sentences, set_of_sentence_weights, 
                                                number_of_sentences = 10)

    utils.dump_file(summarization, "result.txt")
