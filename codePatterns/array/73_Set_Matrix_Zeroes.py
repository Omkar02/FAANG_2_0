"""
* Example 1:
    Input: matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Output:         [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
* Example 2:
    Input: matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Output:         [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
"""


def setZeroes(matrix: list[list[int]]) -> None:
    row_len, col_len = len(matrix), len(matrix[0])

    row_zeros_idx = []
    col_zeros_idx = []
    for row_idx in range(row_len):
        for col_idx in range(col_len):
            curr_cell = matrix[row_idx][col_idx]
            if not curr_cell:
                row_zeros_idx.append(row_idx)
                col_zeros_idx.append(col_idx)

    for row_idx in row_zeros_idx:
        matrix[row_idx] = [0] * col_len
    for col_idx in col_zeros_idx:
        for row in matrix:
            row[col_idx] = 0

    print(matrix)
    return matrix


assert setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [
    [1, 0, 1], [0, 0, 0], [1, 0, 1]]
assert setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]) == [
    [0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
