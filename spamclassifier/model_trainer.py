from os.path import dirname as dn, join as jp
import logging
import sys

from scipy.io import loadmat
from sklearn import svm
import numpy as np

log = logging.getLogger('spamclassifier.model_trainer')
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)


def train_svm():
    # 1. Load the feature vectors of 4000 labeled mails
    data_train = loadmat(jp(dn(__file__), 'data', 'spamTrain.mat'))
    X = data_train['X']
    y = data_train['y'].ravel()

    # 2. Train a linear SVM model
    log.info('Start training the Linear SVM classifier model with %d entries...', len(y))
    classifier_model = svm.LinearSVC()
    classifier_model.fit(X, y)

    log.info('Training done !')
    evaluate_model(classifier_model)

    return classifier_model


def evaluate_model(classifier_model):
    data_train = loadmat(jp(dn(__file__), 'data', 'spamTrain.mat'))
    X = data_train['X']
    y = data_train['y'].ravel()

    log.info('Evaluating the trained Linear SVM on the training set ...')
    predictions = classifier_model.predict(X)
    score = np.mean(predictions == y)
    log.info('Score on training dataset: %.3f%%', score * 100.0)

    log.info('Evaluating the trained Linear SVM on a test set ...')

    data_test = loadmat(jp(dn(__file__), 'data', 'spamTest.mat'))
    X_test = data_test['Xtest']
    y_test = data_test['ytest'].ravel()

    predictions = classifier_model.predict(X_test)
    score = np.mean(predictions == y_test)
    log.info('Score on test dataset: %.3f%%', score * 100)