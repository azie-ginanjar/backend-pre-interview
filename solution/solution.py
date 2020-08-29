def split_into_int(chars):
    return [int(char) for char in chars]


def retrieve_grid():
    f = open("sudoku.txt", "r")

    sudoku_grid = []
    for x in f:
        if 'Grid' not in x.rstrip('\n'):
            sudoku_grid[len(sudoku_grid) - 1].append(split_into_int(x.rstrip('\n')))
        else:
            sudoku_grid.append([])

    return sudoku_grid


if __name__ == '__main__':
    grid = retrieve_grid()
    print(grid)
