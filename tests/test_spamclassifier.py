import unittest
import logging
import sys
from os.path import dirname as dn, join as jp

from spamclassifier.model_trainer import train_svm
from spamclassifier.mail_to_features import preprocess_mail

log = logging.getLogger('spamclassifier')
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)


class TestSpamClassifier(unittest.TestCase):
    def test_basic_spam(self):
        """Test the basic behaviour of the spam classifier"""
        model = train_svm()

        with open(jp(dn(__file__), 'data', 'email_nonspam.txt')) as f:
            content_nonspam = f.read()
        with open(jp(dn(__file__), 'data', 'email_spam.txt')) as f:
            content_spam = f.read()

        test_data = [preprocess_mail(content_nonspam),
                     preprocess_mail(content_spam)]

        predictions = model.predict(test_data)
        self.assertEquals(predictions[0], 0)  # First is not a spam
        self.assertEquals(predictions[1], 1)  # Second one IS a spam


if __name__ == '__main__':
    unittest.main()
