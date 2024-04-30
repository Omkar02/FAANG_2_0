"""
* Example 1:

    Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
    Output: 24
    Explanation:
        [[0,6,0],
        [5,8,7],
        [0,9,0]]
        Path to get the maximum gold, 9 -> 8 -> 7.
* Example 2:
    Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    Output: 28
    Explanation:
        [[1,0,7],
        [2,0,6],
        [3,4,5],
        [0,3,0],
        [9,0,20]]
        Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

"""


def getMaximumGold(grid: list[list[int]]) -> int:
    row_range = range(0, len(grid))
    col_range = range(0, len(grid[0]))

    def backtrack(row, col):
        if row not in row_range or col not in col_range or not grid[row][col]:
            """
                * Check if both row and col are in range 
                * Respective cell is not visited...
            """
            return 0

        # saving the current cell value
        temp_cell_val = grid[row][col]

        # mark the cell as visited..
        grid[row][col] = 0
        ans = temp_cell_val + max(backtrack(row+1, col),
                                  backtrack(row, col+1),
                                  backtrack(row-1, col),
                                  backtrack(row, col-1))

        # revert the cell value
        grid[row][col] = temp_cell_val

        return ans

    max_gold = 0
    for row in row_range:
        for col in col_range:
            max_gold = max(max_gold, backtrack(row, col))

    return max_gold


print(getMaximumGold(grid=[[0, 6, 0],
                           [5, 8, 7],
                           [0, 9, 0]]))

print(getMaximumGold(grid=[[1, 0, 7],
                           [2, 0, 6],
                           [3, 4, 5],
                           [0, 3, 0],
                           [9, 0, 20]]))
