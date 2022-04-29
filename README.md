# Simple Spam Classifier in Python

## Description
A working example of a small SVM spam classifier based on the ML Coursera lesson of Andrew Ng.

The code is separated in 3 files:
* **text_normalizer.py**: Parse an email and normalize/clean/tokenize/stemm its text.
* **mail_to_features.py**: Wrap up the normalization step and map each word to a index of a vocabulary list as a feature vector matrix.
* **model_trainer**: Train a SVM model with a set of preprocessed labeled data.

### Frameworks used
* numpy
* scipy
* sklearn
* stemming

## Deployment & Installation
* Create your own virtual environment: `python -m venv venv`
* Activate it `.\venv\Scripts\activate`
* Install the requirements with `pip install`

### Prerequisites
* Python 3

### Run
From the CLI: `python .\spamclassifier\main.py`