import re
from stemming.porter2 import stem


def normalize_text(text: str) -> [str]:
    # ********* Normalization / Data Cleaning *********
    text = text.lower()
    text = text.replace('\n', ' ')
    text = re.sub('<[^<>]+>', '', text)
    text = re.sub('[0-9]+', 'number', text)
    text = re.sub('(http|https)://[^\s]*', 'httpaddr', text)
    text = re.sub('[^\s]+@[^\s]+', 'emailaddr', text)
    text = re.sub('[$]+', 'dollar', text)

    # ********* Tokenization and Stemming *********
    cleaned_words = []
    if text:
        words = re.split('[ @$/#.-:$*+=?!(){},\'">_<;%]', text)
        for word in words:
            if word and ' ' not in word:
                word = re.sub('[^a-zA-Z0-9]', '', word)
                word = stem(word)
                cleaned_words.append(word)

    return cleaned_words
