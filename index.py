import heapq
import argparse

from functions import text_preprocessing, sentence_scores, sample_text


def summarize(text, total_summary_sentences):
    formatted_text = text_preprocessing(text)
    sentence_scores_dict = sentence_scores(formatted_text)

    summary_sentences = heapq.nlargest(total_summary_sentences, sentence_scores_dict, key=sentence_scores_dict.get)

    summary = " ".join(summary_sentences)

    print("summary", summary)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, default=sample_text())
    parser.add_argument('--total_sentences', type=int, default=7)
    args = parser.parse_args()

    summarize(args.text, args.total_sentences)


if __name__ == '__main__':
    main()
