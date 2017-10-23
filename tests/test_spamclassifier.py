import unittest
from os.path import dirname as dn, join as jp

from spamclassifier.model_trainer import train_svm
from spamclassifier.mail_to_features import preprocess_mail


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
