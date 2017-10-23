from os.path import dirname as dn, join as jp

import numpy as np

from .text_normalizer import normalize


def preprocess_mail(mail):
    # 1. Preprocess mail
    words = normalize(mail)

    # 2. Numerize
    word_indices = map_to_voc_indices(words)

    # 3. Features vectorize
    features = extract_features(word_indices)

    return features


def map_to_voc_indices(words):
    word_indices = []
    with open(jp(dn(__file__), 'data', 'vocab.txt')) as f:
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
