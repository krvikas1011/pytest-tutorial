from b_Pytest_vs_unittest.math_functions import multiply


def test_numbers_3_4():
    assert 12 == multiply(3, 4)


def test_strings_a_3():
    assert 'aaa' == multiply('a', 3)


"""
The immediately noticeable thing is that pytest uses a plain assert statement, 
which is much easier to remember and use compared to the numerous assertSomething functions 
found in unittest.
"""
