import logging
from pathlib import Path

from spamclassifier.model_trainer import train_svm

logging.basicConfig(level=logging.INFO)


def train_run():
    model = train_svm()

    path_nonspam = Path(__file__) / '../data/test/email_nonspam.txt'
    with path_nonspam.open() as f:
        content_nonspam = f.read()

    path_spam = Path(__file__) / '../data/test/email_spam.txt'
    with path_spam.open() as f:
        content_spam = f.read()

    # TODO Preprocess both your email body
    raise NotImplementedError
    x_nonspam = []
    x_spam = []

    # TODO Make the prediction. Are they correct ?
    raise NotImplementedError
    pred_nonspam = []

    assert pred_nonspam[0] == 0  # First is not a spam

    pred_spam = []
    assert pred_spam[0] == 1  # Second one IS a spam


if __name__ == '__main__':
    train_run()
