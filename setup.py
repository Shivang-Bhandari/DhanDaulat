"""Packaging settings."""

from dhandaulat import __version__
from setuptools import Command, find_packages, setup


setup(
    name='dhandaulat',
    version=__version__,
    description='A Currency converter command line program in Python.',
    url='https://github.com/Shivang-Bhandari/DhanDaulat',
    author='Shivang Bhandari',
    author_email='pump382156@gmail.com',
    license='UNLICENSE',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='cli',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['docopt'],
    entry_points={
        'console_scripts': [
            'dhandaulat=dhandaulat.paisa:main',
        ],
    },
)
