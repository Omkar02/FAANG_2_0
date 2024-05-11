"""
? Pattern: Distinct Ways
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2
    Explanation: There is one obstacle in the middle of the 3x3 grid above.
                There are two ways to reach the bottom-right corner:
                1. Right -> Right -> Down -> Down
                2. Down -> Down -> Right -> Right
* Example 2:
    Input: obstacleGrid = [[0,1],[0,0]]
    Output: 1
"""


def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    row_range = range(len(obstacleGrid))
    col_range = range(len(obstacleGrid[0]))

    cache = {}

    def _getAllPaths(row: int, col: int):
        key = (row, col)
        if key in cache:
            return cache[key]
        if row == row_range[-1] and col == col_range[-1]:
            return 1
        if row not in row_range or col not in col_range:
            return 0
        if obstacleGrid[row][col] == 1:
            return 0

        down = _getAllPaths(row + 1, col)
        right = _getAllPaths(row, col + 1)

        cache[key] = down + right
        return cache[key]
    return _getAllPaths(0, 0)


print(uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(uniquePathsWithObstacles(obstacleGrid=[[0, 1], [0, 0]]))
