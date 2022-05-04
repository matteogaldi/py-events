from setuptools import setup, find_packages
from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

setup(
    name='py-events',
    version='0.1.0',
    description='A simple event emitter for Python',
    long_description=open(path.join(HERE, 'README.md'), encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/matteogaldi/py-eventemitter',
    author='Matteo Galdi',
    license='MIT',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)
