rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = set(range(rows))
valid_cols = set(range(cols))


while True:
    command, *indices = [int(x) if x.isdigit() else x for x in input().split()]

    if command == 'END':
        break

    command_is_valid = False

    if len(indices) == 4 and command == 'swap' and {indices[1], indices[3]}.issubset(valid_cols) and {indices[0], indices[2]}.issubset(valid_rows):
        command_is_valid = True

    if command_is_valid:
        row1, col1, row2, col2 = indices
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print('Invalid input!')


