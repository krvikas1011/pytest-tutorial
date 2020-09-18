def add(value_1, value_2):
    return value_1 + value_2


def subtract(value_1, value_2):
    return value_1 - value_2


def multiply(value_1, value_2):
    return value_1 * value_2


def divide(value_1, value_2):
    return value_1 / value_2


def test_add():
    a, b = 6, 3
    sum_value = add(a, b)
    assert 9 == sum_value
    assert isinstance(sum_value, int)


def test_subtract():
    a, b = 6, 3
    diff_value = subtract(a, b)
    assert 3 == diff_value
    assert isinstance(diff_value, int)


def test_multiply():
    a, b = 6, 3
    product_value = multiply(a, b)
    assert 18 == product_value
    assert isinstance(product_value, int)


def test_divide():
    a, b = 6, 3
    division_value = divide(a, b)
    assert 2.0 == division_value
    assert isinstance(division_value, float)
