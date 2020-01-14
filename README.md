![TravisCI build status](https://travis-ci.com/blsqr/mytoolz.svg?branch=master)

# The `mytoolz` Package

_Note: This is a dummy project for use in git workshops! It has no actual functionality._

Today is a very good day. :)

`mytoolz` is a Python 3 package that contains some useful tools for my everyday work.

To assert that the tools work as they should, it contains a testing framework.

## Installation Instructions
To install the package, use `pip3 install <link-to-this-repo>`.

## Testing Framework
Tests can be found in the [`test/`](test/) directory and are implemented using the [pytest](https://pytest.org/en/latest/) framework.

All tests are run automatically via the GitLab CI.

To run them locally (e.g. during development), it's recommended to clone the `mytoolz` repository and install it in editable mode, including the test dependencies:

    git clone <repo-url>
    cd mytoolz
    pip install -e .
    pip install -e .[test_deps]

You can subsequently run the tests using the following command:

    python -m pytest -v test/

To monitor test coverage alongside, add the ` --cov=mytoolz --cov-report=term-missing` flags.
