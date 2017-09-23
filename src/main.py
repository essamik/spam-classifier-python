from src import model_trainer, mail_to_features


# Get them modlz
model = model_trainer.train_svm()

# Test with a sample spam and a sample non spam mail
with open('../res/email_nonspam.txt') as f:
    content_nonspam = f.read()
with open('../res/email_spam.txt') as f:
    content_spam = f.read()

example_false = mail_to_features.preprocess_mail(content_nonspam)
example_true = mail_to_features.preprocess_mail(content_spam)

# Input has to be an array of feature vectors
predictions = model.predict([example_false, example_true])
print('NonSpam email is : ', predictions[0])
print('Spam email is : ', predictions[1])
