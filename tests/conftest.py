import os

import pytest


@pytest.fixture
def path():
    return os.path.dirname(os.path.realpath(__file__)) + "/data"
