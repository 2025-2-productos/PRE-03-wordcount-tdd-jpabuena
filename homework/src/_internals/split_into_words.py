def split_into_words(preprocessed_lines):
    words = []
    for line in preprocessed_lines:
        words.extend(word.strip(",.!?") for word in line.split())
    return words
