import pytest


def divide(x):
    return 11 / x


def test_passes():
    with pytest.raises(ZeroDivisionError) as e_info:
        divide(0)


def test_passes_without_info():
    with pytest.raises(ZeroDivisionError):
        divide(0)


def test_fails():
    with pytest.raises(ZeroDivisionError) as e_info:
        divide(5)


def test_fails_without_info():
    with pytest.raises(ZeroDivisionError):
        divide(5)


# Even if the appropriate exception is caught, it is bad style,
# because the test result is less informative
# than it would be with pytest.raises(e)
# (it just says pass or fail.)


def test_passes_but_bad_style():
    try:
        divide(0)
        assert False
    except ZeroDivisionError:
        assert True
