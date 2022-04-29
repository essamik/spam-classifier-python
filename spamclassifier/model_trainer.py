import logging
from pathlib import Path

from scipy.io import loadmat


def train_svm():
    # 1. Load the feature vectors of 4000 labeled mails
    dataset_train = loadmat(str(Path(__file__) / '../data/dataset/spamTrain.mat'))
    X_train = dataset_train['X']
    y_train = dataset_train['y'].ravel()  # ravel() flattens the array [[1], [0]] -> [1, 0]

    # 2. Train a linear SVM model
    logging.info('Start training the Linear SVM classifier model with %d entries...', len(y_train))
    # TODO Train a model https://scikit-learn.org/stable/modules/svm.html#svm-classification
    raise NotImplementedError
    classifier_model = None

    logging.info('Training done !')
    evaluate_model(classifier_model, X_train, y_train)

    return classifier_model


def evaluate_model(classifier_model, X_train, y_train):
    logging.info('Evaluating the trained Linear SVM on a test set ...')

    dataset_test = loadmat(str(Path(__file__) / '../data/dataset/spamTest.mat'))
    X_test = dataset_test['Xtest']
    y_test = dataset_test['ytest'].ravel()

    # TODO Use the model to predict the classes of X_test
    raise NotImplementedError
    predictions = []

    # TODO Compare your predictions to y_test, get the percentage of correct predictions
    raise NotImplementedError
    score = 0.0

    # TODO Could you also run an evaluation on the training set ?

    logging.info('Score on test dataset: %.3f%%', score * 100)
