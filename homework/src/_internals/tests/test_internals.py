import os
import shutil
import sys

from ...wordcount import (
    count_words,
    parse_args,
    preprocess_lines,
    split_into_words,
    write_count_words,
)
from ..read_all_lines import read_all_lines


def test_parse_args():

    test_args = ["homework", "data/input", "data/output"]
    sys.argv = test_args

    input_folder, output_folder = parse_args()

    assert input_folder == "data/input"
    assert output_folder == "data/output"


def test_read_all_lines():
    input_folder = "data/input/"
    lines = read_all_lines(input_folder)
    assert len(lines) > 0
    assert any(
        "Analytics refers to the systematic computational analysis of data" in line
        for line in lines
    )


def test_preprocess_lines():
    lines = [" Hello, World!  ", "Python is GREAT."]
    preprocessed = preprocess_lines(lines)
    assert preprocessed == ["hello, world!", "python is great."]


def test_split_into_words():
    lines = ["hello, world!", "python is great."]
    words = split_into_words(lines)
    assert words == ["hello", "world", "python", "is", "great"]


def test_count_words():
    words = ["hello", "world", "python", "is", "great"]
    word_counts = count_words(words)
    assert word_counts == {"hello": 2, "world": 1, "python": 1}


def test_write_word_counts():
    output_folder = "data/output"
    word_counts = {"hello": 2, "world": 1, "python": 1}

    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)

    write_count_words(output_folder, word_counts)

    output_file = os.path.join(output_folder, "wordcount.tsv")
    assert os.path.exists(output_file), "Output file was not create"

    with open(output_file, encoding="utf-8") as f:
        lines = f.readlines()

    assert lines == ["hello\t2\n", "world\t1\n", "python\t1\n"]

    # Clean up
    shutil.rmtree(output_folder)
