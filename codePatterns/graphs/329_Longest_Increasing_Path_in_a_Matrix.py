"""
* TYPE             : Graph
* ALGORITHM        : DFS 

* TIME-COMPLEXITY  : O(M x N)
* SPACE-COMPLEXITY : O(M x N)

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

* Example 1:
    Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
    Output: 4
    Explanation: The longest increasing path is [1, 2, 6, 9].
* Example 2:
    Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
    Output: 4
    Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
* Example 3:
    Input: matrix = [[1]]
    Output: 1
"""


def longestIncreasingPath(matrix: list[list[int]]) -> int:
    row_range, col_range = range(len(matrix)), range(len(matrix[0]))
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cache = {}  # * HERE WE CAN CACHE THE VAL

    def _getLongestIncreasingPath(row: int, col: int) -> int:
        """
        NOTE: HERE VISITED IS NOT REQUIRED AS THAT IS TAKEN CARE BY 
            * PRE_VAL < CUR_VAL
        * AND NO BASE CONDITIONS AS CHECKING RANGE CONDITIONS IN FOR LOOP.
        """
        key = (row, col)
        if key in cache:
            return cache[key]

        # * IT'S SET TO 1 AS THE MAX CUR IS 1 CONSISTING OF CUR CELL VALUE
        cur_max_path = 1

        cur_val = matrix[row][col]
        for x, y in directions:
            new_row, new_col = x + row, y + col
            if new_row in row_range and new_col in col_range and cur_val < matrix[new_row][new_col]:
                cur_max_path = max(cur_max_path,
                                   1 + _getLongestIncreasingPath(new_row, new_col))

        cache[key] = cur_max_path
        return cache[key]

    max_path = 0
    # * GO THROUGH ALL THE CELLS
    for row in row_range:
        for col in col_range:
            max_path = max(max_path, _getLongestIncreasingPath(row, col))
    return max_path


print(longestIncreasingPath(matrix=[[9, 9, 4], [6, 6, 8], [2, 1, 1]]))  # 4
print(longestIncreasingPath(matrix=[[3, 4, 5], [3, 2, 6], [2, 2, 1]]))  # 4
print(longestIncreasingPath(matrix=[[1]]))  # 1
print(longestIncreasingPath(matrix=[[7, 8, 9], [9, 7, 6], [7, 2, 3]]))  # 6


'''
[[0,0],
[0,1],
[1,0],
[1,2],
[2,1],
[2,2]]

'''
