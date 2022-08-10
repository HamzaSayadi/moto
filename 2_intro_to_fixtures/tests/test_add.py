import pytest
from main import add, substract
import mock


@pytest.fixture(scope='function')
def mock_get_random_numbers():
    """Mock get random number."""
    with mock.patch('main.get_random_numbers', return_value=(7, 6)):
        yield


def test_add(mock_get_random_numbers):
    # given
    expected_result = 13

    # when
    result = add()

    # then
    assert result == expected_result


def test_substract(mock_get_random_numbers):
    # given
    expected_result = 1

    # when
    result = substract()

    # then
    assert result == expected_result
