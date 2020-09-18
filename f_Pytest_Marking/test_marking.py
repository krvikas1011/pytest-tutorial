import pytest
import sys


@pytest.mark.windows
def test_windows1():
    assert sys.platform == 'win32'


@pytest.mark.windows
def test_windows2():
    assert sys.platform == 'win32'


@pytest.mark.mac
def test_mac1():
    assert sys.platform == 'darwin'


@pytest.mark.mac
class TestMac:
    def test_method(self):
        assert sys.platform == 'darwin'
