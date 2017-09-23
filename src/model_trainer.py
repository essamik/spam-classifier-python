from scipy.io import loadmat
from sklearn import svm
import numpy as np


def train_svm():
    # 1. Load the feature vectors of 4000 labeled mails
    data_train = loadmat('../res/spamTrain.mat')
    X = data_train['X']
    y = data_train['y'].ravel()

    # 2. Train a linear SVM model
    print('Start training the Linear SVM classifier model with', len(y), 'entries...')
    classifier_model = svm.LinearSVC()
    classifier_model.fit(X, y)

    print('Training done !')
    evaluate_model(classifier_model)

    return classifier_model


def evaluate_model(classifier_model):
    data_train = loadmat('../res/spamTrain.mat')
    X = data_train['X']
    y = data_train['y'].ravel()

    print('\nEvaluating the trained Linear SVM on the training set ...')
    predictions = classifier_model.predict(X)
    score = np.mean(predictions == y)
    print('Score on training dataset: ', score * 100, '%')

    print('\nEvaluating the trained Linear SVM on a test set ...')

    data_test = loadmat('../res/spamTest.mat')
    X_test = data_test['Xtest']
    y_test = data_test['ytest'].ravel()

    predictions = classifier_model.predict(X_test)
    score = np.mean(predictions == y_test)
    print('Score on test dataset: ', score * 100, '%')
