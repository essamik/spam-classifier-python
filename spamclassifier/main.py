from .model_trainer import train_svm
from .mail_to_features import preprocess_mail

# Get them modlz
model = train_svm()

# Test with a sample spam and a sample non spam mail
with open('../res/email_nonspam.txt') as f:
    content_nonspam = f.read()
with open('../res/email_spam.txt') as f:
    content_spam = f.read()

example_false = preprocess_mail(content_nonspam)
example_true = preprocess_mail(content_spam)

print('\nPrediction on some test mails from the resources')
# Input has to be an array of feature vectors
predictions = model.predict([example_false, example_true])
print('NonSpam email is : ', predictions[0])
print('Spam email is : ', predictions[1])
