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


def is_possible(row, col, n, grid):
    # validate that n not appeared yet in rows
    if n in grid[row]:
        return False

    # validate that n not appeared yet in cols
    for i in range(0, 9):
        if grid[i][col] == n:
            return False

    # validate that n not appeared yet on box

    # define start coordinate of box in 9x9 grid
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[box_row+i][box_col+j] == n:
                return False

    return True


if __name__ == '__main__':
    grid = retrieve_grid()
    print(grid)
