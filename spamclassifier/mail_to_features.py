from src import text_normalizer
import numpy as np


def preprocess_mail(mail):
    # 1. Preprocess mail
    words = text_normalizer.normalize(mail)

    # 2. Numerize
    word_indices = map_to_voc_indices(words)

    # 3. Features vectorize
    features = extract_features(word_indices)

    return features


def map_to_voc_indices(words):
    filename = '../res/vocab.txt'
    word_indices = []
    with open(filename) as f:
        vocab_list = f.read().splitlines()
        for word in words:
            if word in vocab_list:
                i = vocab_list.index(word)
                word_indices.append(i)

    return word_indices


def extract_features(word_indices):
    n = 1899
    x = np.zeros(n, np.int8)

    for i in range(0, len(word_indices)):
        x[word_indices[i]] = 1

    return x
