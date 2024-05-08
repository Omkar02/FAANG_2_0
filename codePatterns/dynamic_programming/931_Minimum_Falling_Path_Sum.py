"""
? Pattern: Minimum (Maximum) Path to Reach a Target
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
    Output: 13
    Explanation: There are two falling paths with a minimum sum as shown.
* Example 2:
    Input: matrix = [[-19,57],[-40,-5]]
    Output: -59
    Explanation: The falling path with a minimum sum is shown.
"""


def minFallingPathSum(matrix: list[list[int]]) -> int:
    min_path_sum = float('inf')
    row_len, col_len = len(matrix), len(matrix[0])
    cache = {}

    def _getMinPathSum(row: int, col: int) -> int:
        key = (row, col)
        if key in cache:
            return cache[key]

        if row not in range(row_len) or col not in range(col_len):
            # * BASE CONDITION TO NOT GO OUT OF BOUND
            return float('inf')

        if row == row_len - 1:
            # * RETURNS THE LAST ROW, N COLUMN VALUE
            return matrix[row][col]

        # * THERE ARE 3 PATH WE CAN GO AND WE WANT THE MIN OF IT...
        cache[key] = matrix[row][col] + min(_getMinPathSum(row + 1, col),
                                            _getMinPathSum(row + 1, col - 1),
                                            _getMinPathSum(row + 1, col + 1))
        return cache[key]

    for col in range(col_len):
        min_path_sum = min(min_path_sum, _getMinPathSum(row=0, col=col))

    return min_path_sum


print(minFallingPathSum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
print(minFallingPathSum(matrix=[[-19, 57], [-40, -5]]))
