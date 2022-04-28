import logging
from os.path import dirname as dn, join as jp

from spamclassifier.mail_to_features import preprocess_mail
from spamclassifier.model_trainer import train_svm

logging.basicConfig(level=logging.INFO)


def train_run():
    model = train_svm()

    with open(jp(dn(__file__), 'data', 'test', 'email_nonspam.txt')) as f:
        content_nonspam = f.read()
    with open(jp(dn(__file__), 'data', 'test', 'email_spam.txt')) as f:
        content_spam = f.read()

    x_nonspam = preprocess_mail(content_nonspam)
    x_spam = preprocess_mail(content_spam)

    pred_nonspam = model.predict([x_nonspam])
    assert pred_nonspam[0] == 0  # First is not a spam

    pred_spam = model.predict([x_spam])
    assert pred_spam[0] == 1  # Second one IS a spam


if __name__ == '__main__':
    train_run()
