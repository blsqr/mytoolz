#!/usr/bin/env python3

from setuptools import setup, find_packages

# Dependency lists ............................................................
install_deps = []
test_deps = ['pytest>=3.4', 'pytest-cov>=2.5.1', 'tox>=3.1.2']

# .............................................................................

# A function to extract version number from __init__.py
def find_version(*file_paths) -> str:
    """Tries to extract a version from the given path sequence"""
    import os, re, codecs

    def read(*parts):
        """Reads a file from the given path sequence, relative to this file"""
        here = os.path.abspath(os.path.dirname(__file__))
        with codecs.open(os.path.join(here, *parts), 'r') as fp:
            return fp.read()

    # Read the file and match the __version__ string
    file = read(*file_paths)
    match = re.search(r"^__version__\s?=\s?['\"]([^'\"]*)['\"]", file, re.M)
    if match:
        return match.group(1)
    raise RuntimeError("Unable to find version string in " + str(file_paths))


# .............................................................................
setup(
    name='mytoolz',
    #
    # Set the version from dantro.__version__
    version=find_version('mytoolz', '__init__.py'),
    #
    # Project info
    description="A collection of useful everyday python tools",
    long_description=("This is a DUMMY project for the SIAM Tools Seminar."),
    author="Yunus Sevinchan",
    author_email=("Yunus Sevinchan <Yunus.Sevinchan@iup.uni.heidelberg.de>"),
    licence='MIT',
    url='https://ts-gitlab.iup.uni-heidelberg.de/yunus/mytoolz',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities'
    ],
    #
    # Distribution details, dependencies, ...
    packages=find_packages(exclude=["tests.*", "tests"]),
    install_requires=install_deps
    tests_require=test_deps,
    test_suite='py.test',
    extras_require=dict(test_deps=test_deps)
)
