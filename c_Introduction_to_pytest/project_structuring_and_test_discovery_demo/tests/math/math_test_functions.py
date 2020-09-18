from c_Introduction_to_pytest.project_structuring_and_test_discovery_demo.src.math.math_functions import multiply


def test_numbers_3_4():
    assert 12 == multiply(3, 4)


def test_strings_a_3():
    assert 'bbb' == multiply('a', 3)
