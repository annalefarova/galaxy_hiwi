from setuptools import setup, find_packages

setup(
    name='mztab_processing',
    version='0.0.1',
    url='https://github.com/annalefarova/galaxy_hiwi',
    author='Anna Lefarova',
    author_email='annalefarova@gmail.com',
    description='Utilities for processing .mzTab files using Pandas and Pyteomics.',
    packages=find_packages(),    
    install_requires=['pandas >= 1.1.5', 'pyteomics >= 4.4.0'],
)