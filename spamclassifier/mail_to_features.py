from os.path import dirname as dn, join as jp

import numpy as np

from .text_normalizer import normalize_text


def preprocess_mail(text: str) -> []:
    # 1. Preprocess mail
    words = normalize_text(text)

    # 2. Word to indices
    word_indices = map_to_voc_indices(words)

    # 3. Features vectorize
    features = binarize(word_indices)

    return features


def map_to_voc_indices(words: [str]) -> [int]:
    word_indices = []
    with open(jp(dn(__file__), 'data', 'dataset', 'vocab.txt')) as f:
        vocab_list = f.read().splitlines()
        # TODO Map your words to their indices in vocab_list (if an indice exists for your word)
        raise NotImplementedError

    return word_indices


def binarize(word_indices: [int]) -> []:
    n = 1899
    x = np.zeros(n, np.int8)

    for i in range(0, len(word_indices)):
        x[word_indices[i]] = 1

    return x
