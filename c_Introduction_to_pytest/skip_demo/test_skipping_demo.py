import pytest
import sys


@pytest.mark.skip
def test_fail():
    assert 3 == 4


def test_pass():
    assert 4 == 4


def test_windows_function():
    if not sys.platform.startswith("win"):
        pytest.skip("unsupported configuration")
    else:
        assert 3 == 4


@pytest.mark.skipif(sys.platform != "win32", reason='This only runs for windows')
class TestSomething:

    def test_one(self):
        assert 3 == 4

    def test_two(self):
        assert 3 == 5
