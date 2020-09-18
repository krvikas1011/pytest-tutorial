from unittest import mock
from unittest.mock import Mock


class SumCalculator:

    @staticmethod
    def sum_values(value_arr):
        total = 0
        for value in value_arr:
            total += value
        return total


class AverageCalculator:

    @staticmethod
    def calculate_average(value_arr, sum_calculator):
        total_sum = sum_calculator.sum_values(value_arr)
        return total_sum / len(value_arr)


def test_calculate_average():
    sum_calculator = SumCalculator()
    avg = AverageCalculator.calculate_average([1, 2, 3, 4, 5], sum_calculator)
    assert 3 == avg

    sum_calculator_mock = Mock()
    sum_calculator_mock.sum_values.return_value = 5
    avg = AverageCalculator.calculate_average([1, 2, 3, 4, 5], sum_calculator_mock)
    assert 1 == avg

    sum_calculator_mock.sum_values.assert_called_once()
    sum_calculator_mock.sum_values.assert_called_once_with([1, 2, 3, 4, 5])


@mock.patch("i_Mocking.test_mock.SumCalculator.sum_values", return_value=5, autospec=True)
def test_calculate_average_patch(mock_sum):
    sum_calculator = SumCalculator()
    avg = AverageCalculator.calculate_average([1, 2, 3, 4, 5], sum_calculator)
    assert 1 == avg
