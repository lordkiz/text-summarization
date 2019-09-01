import heapq
import argparse

from functions import text_preprocessing, sentence_scores, sample_text


def reorder_sentences(original_text, summarized_text_list):
    """
    :param original_text: String
    :param summarized_text_list: list
    :return: summarized_text: list

    This function basically reorders the summarized sentence
    so that all the sentences align with the order of the
    sentences of the original document.
    We will take summarized sentences and sentences
    from the original document into consideration and perform the sorting operation.
    """
    reordered_sentences = sorted(summarized_text_list, key=lambda x: original_text.index(x))
    return reordered_sentences


def summarize(text, total_summary_sentences):
    formatted_text = text_preprocessing(text)
    sentence_scores_dict = sentence_scores(formatted_text)

    summary_sentences = heapq.nlargest(total_summary_sentences, sentence_scores_dict, key=sentence_scores_dict.get)

    summary = " ".join(reorder_sentences(formatted_text, summary_sentences))


    print("summary", summary)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, default=sample_text())
    parser.add_argument('--total_sentences', type=int, default=7)
    args = parser.parse_args()

    summarize(args.text, args.total_sentences)


if __name__ == '__main__':
    main()
