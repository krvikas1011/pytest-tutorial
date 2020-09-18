from c_Introduction_to_pytest.project_structuring_and_test_discovery_demo.src.math.math_functions import multiply


def test_numbers_3_4():
    assert 12 == multiply(3, 4)


def test_strings_a_3():
    assert 'aaa' == multiply('a', 3)


def amIATest():
    assert 'aab' == multiply('a', 3)


class TestMath:
    """This is considered as test"""

    def test_numbers_2_4(self):
        assert 8 == multiply(2, 4)


class MathsTest:
    """This is not considered as test"""

    def test_numbers_3_7(self):
        assert 8 == multiply(3, 7)
