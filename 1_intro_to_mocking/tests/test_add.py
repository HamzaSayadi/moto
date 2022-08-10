import pytest
from main import add
import mock

def test_add():
    # given
    expected_result = 11

    # when
    with mock.patch('main.get_random_numbers', return_value=(5, 6)):
        result = add()

    # then
    assert result == expected_result
