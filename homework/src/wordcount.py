# Ejemplo para casos de uso
# python3 -m homework data/input data/output


import argparse

from ._internals import read_all_lines


def parse_args():
    parser = argparse.ArgumentParser(description="Count Word in files.")
    parser.add_argument(
        "input", type=str, help="Path to the input folder containing files to process."
    )
    parser.add_argument(
        "output",
        type=str,
        help="Path to the output folder containing files to process.",
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output


def preprocess_lines(lines):
    return [line.strip().lower() for line in lines]


def split_into_words(preprocessed_lines):
    pass


def count_words(words):
    pass


def write_count_words(output_folder, word_counts):
    pass


def main():
    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)
    preprocessed_lines = preprocess_lines(lines)
    words = split_into_words(preprocessed_lines)
    word_counts = count_words(words)
    write_count_words(output_folder, word_counts)
