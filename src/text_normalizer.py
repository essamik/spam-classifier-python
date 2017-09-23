import re
from stemming.porter2 import stem


def normalize(mail):
    # ********* Normalization *********
    mail = mail.lower()
    mail = re.sub('<[^<>]+>', '', mail)
    mail = re.sub('[0-9]+', 'number', mail)
    mail = re.sub('(http|https)://[^\s]*', 'httpaddr', mail)
    mail = re.sub('[^\s]+@[^\s]+', 'emailaddr', mail)
    mail = re.sub('[$]+', 'dollar', mail)

    # ********* Tokenization and Stemming *********
    cleaned_words = []
    if mail:
        words = re.split('[ @$/#.-:$*+=?!(){},\'">_<;%]', mail)
        for word in words:
            if word:
                word = re.sub('[^a-zA-Z0-9]', '', word)
                word = stem(word)
                cleaned_words.append(word)

    return cleaned_words
