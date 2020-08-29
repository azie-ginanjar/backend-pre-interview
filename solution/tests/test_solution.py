import pytest

from ..solution import split_into_int, retrieve_grid, is_possible


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


def test_is_possible():
    grid = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
            [9, 0, 0, 3, 0, 5, 0, 0, 1],
            [0, 0, 1, 8, 0, 6, 4, 0, 0],
            [0, 0, 8, 1, 0, 2, 9, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 6, 7, 0, 8, 2, 0, 0],
            [0, 0, 2, 6, 0, 9, 5, 0, 0],
            [8, 0, 0, 2, 0, 3, 0, 0, 9],
            [0, 0, 5, 0, 1, 0, 3, 0, 0]]

    # validate this return false if number already in 3x3 box
    assert not is_possible(0, 0, 1, grid)

    # validate this return false if number already in row
    assert not is_possible(0, 0, 3, grid)

    # validate this return false if number already in col
    assert not is_possible(0, 0, 7, grid)

    # validate this return true if number not in col, row, or 3x3 box
    assert is_possible(0, 0, 4, grid)
