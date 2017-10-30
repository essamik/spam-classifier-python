from setuptools import setup, find_packages

config = {
    'name': 'spamclassifier-python',
    'description': 'A working example of a small spam classifier based on the ML Coursera lesson',
    'author': 'Karim Es-Sami, Julien Wolflisberg',
    'version': '0.1a',
    'install_requires': [
        'numpy',
        'scipy',
        'sklearn',
        'stemming',
    ],
    'extras_require': {
        'dev': [
            'nose',
            'coverage',
            'tissue'
        ]
    },
    'package_data': {
        'spamclassifier': ['data/spamTest.mat',
                           'data/spamTrain.mat',
                           'data/vocab.txt'],
        'tests': ['data/email_nonspam.txt',
                  'data/email_spam.txt'],
    },
    'test_suite': 'nose.collector',
    'packages': find_packages(),
}

setup(**config)
