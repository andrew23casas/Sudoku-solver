grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solver(gr):
    empty = empty_cell(gr)
    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1, 10):
        if is_valid(gr, i, (row, col)):
            gr[row][col] = i

            if solver(gr):
                return True

            gr[row][col] = 0
    return False


def is_valid(gr, num, pos) -> bool:
    # row
    for i in range(len(gr)):
        if gr[pos[0]][i] == num and pos[1] != i:
            return False
    # column
    for i in range(len(gr)):
        if gr[i][pos[1]] == num and pos[0] != i:
            return False
    # box
    box_row = pos[1] // 3
    box_col = pos[0] // 3

    for i in range(box_col * 3, (box_col * 3) + 3):
        for j in range(box_row * 3, (box_row * 3) + 3):
            if grid[i][j] == num:
                return False
    return True


def print_grid(gr):
    for i in range(len(gr)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - -")
        for j in range(len(gr[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(gr[i][j])
            else:
                print(str(gr[i][j]) + " ", end="")


def empty_cell(gr):
    for i in range(len(gr)):
        for j in range(len(gr[0])):
            if gr[i][j] == 0:
                return i, j
    return None
