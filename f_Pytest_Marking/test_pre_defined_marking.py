import pytest
import sys


@pytest.mark.skip("Skipped for all scenarios")
def test_windows():
    assert False


@pytest.mark.skipif(sys.platform == 'darwin', reason='This only runs for windows')
def test_win():
    assert sys.platform == 'win32'


@pytest.mark.skipif(sys.platform != 'darwin', reason='This only runs for mac')
def test_mac():
    assert sys.platform == 'darwin'
