"""This tests the initialization of the mytoolz package works properly"""

import pytest

# -----------------------------------------------------------------------------

def test_init():
    """Tests if the initialization of the mytoolz package works and the main
    components are properly available to a user.
    """
    import mytoolz as mt

    assert mt.__version__
