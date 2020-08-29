import pytest

from ..solution import split_into_int, retrieve_grid


def test_split_into_int():
    chars = '89167'

    result = split_into_int(chars)

    assert result == [8, 9, 1, 6, 7]

    # chars should not contains non numeric character, or it should raise value error
    with pytest.raises(ValueError):
        result = split_into_int('asdasds')


def test_retrieve_grid():
    grid = retrieve_grid()

    assert grid[0][0] == [0, 0, 3, 0, 2, 0, 6, 0, 0]
