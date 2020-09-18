def add(num1, num2):
    return num1 + num2


def greet(name):
    return 'Hi {}'.format(name)


def reverse_a_list(my_list):
    my_list.reverse()
    return my_list


def get_list_from_0_to_10():
    my_list = [x for x in range(1, 11)]
    return my_list


def test_add():
    a, b = 5, 10  # Arrange
    sum_value = add(a, b)  # Act
    assert 15 == sum_value  # Assert


# *************************************************** Tests Section ***************************************************


def test_greet():
    # Arrange
    person1 = {'name': 'John'}
    person2 = {'name': 'Mike'}

    # Act
    greeting1 = greet(person1.get('name'))
    greeting2 = greet(person2.get('name'))

    # Assert
    assert 'Hi John' == greeting1
    assert 'Hi Mike' == greeting2


def test_reverse_list():
    # Arrange
    demo_list = [1, 3, 2, 4]

    # Act
    reversed_list = reverse_a_list(demo_list)

    # Assert
    assert [4, 2, 3, 1] == reversed_list


def test_get_list_from_0_to_10():
    # Arrange
    expected_list_size = 10

    # Act
    result_list = get_list_from_0_to_10()

    # Assert
    assert isinstance(result_list, list)
    assert expected_list_size == len(result_list)
    assert 1 == result_list[0]
    assert 10 == result_list[-1]
