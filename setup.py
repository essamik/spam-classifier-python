from setuptools import setup, find_packages

config = {
    'name': 'spamclassifier',
    'description': 'A working example of a spam classifier',
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
    'entry_points': {
        'console_scripts': [
            'spamclassifier=spamclassifier:main',
        ],
    },
}

setup(**config)
