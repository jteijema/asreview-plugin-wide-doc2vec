from setuptools import setup
from setuptools import find_namespace_packages

setup(
    name='asreview-plugin-wide-doc2vec',
    version='0.1',
    description='A plugin that adds a wider doc2vec',
    url='https://github.com/JTeijema/asreview-plugin-wide-doc2vec/',
    author='ASReview team, Jelle Teijema',
    author_email='j.j.teijema@gmail.com',
    classifiers=[
        'Development Status :: 1 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='systematic review',
    packages=find_namespace_packages(include=['asreviewcontrib.*']),
    python_requires='~=3.6',
    install_requires=[
        'scikit-learn',
        'asreview>=0.13',
        'tensorflow',
        'scipy'
    ],
    entry_points={
        'asreview.models.classifiers': [
        ],
        'asreview.models.feature_extraction': [
            'wide_doc2vec = asreviewcontrib.models.wide_doc2vec:wide_doc2vec',
        ],
        'asreview.models.balance': [
            # define balance strategy algorithms
        ],
        'asreview.models.query': [
            # define query strategy algorithms
        ]
    },
    project_urls={
        'Bug Reports': 'https://github.com/JTeijema/asreview-plugin-wide-doc2vec//issues',
        'Source': 'https://github.com/JTeijema/asreview-plugin-wide-doc2vec/',
    },
)
