"""
? Pattern: Minimum (Maximum) Path to Reach a Target
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
    Output: 7
    Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
* Example 2:
    Input: grid = [[1,2,3],[4,5,6]]
    Output: 12
"""


def minPathSum(grid: list[list[int]]) -> int:
    row_end, col_end = len(grid)-1, len(grid[0])-1
    cache = {}

    def _getPath(row: int, col: int):
        key = (row, col)
        if key in cache:
            return cache[key]

        if row > row_end or col > col_end:
            return float("inf")

        if row == row_end and col == col_end:
            return grid[row][col]

        cache[key] = grid[row][col] + min(_getPath(row + 1, col),
                                          _getPath(row, col+1))
        return cache[key]

    return _getPath(0, 0)


print(minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(minPathSum(grid=[[1, 2, 3], [4, 5, 6]]))
print(minPathSum(grid=[[1, 2, 3], [4, 5, 6]]))
