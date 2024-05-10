"""
? Pattern: Minimum (Maximum) Path to Reach a Target
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11
    Explanation: The triangle looks like:
           2
          3 4
         6 5 7
        4 1 8 3
        The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
* Example 2:
    Input: triangle = [[-10]]
    Output: -10
"""


def minimumTotal(triangle: list[list[int]]) -> int:
    cache = {}
    end = len(triangle) - 1

    def _getMinPath(row: int, col: int) -> int:
        key = (row, col)
        if key in cache:
            return cache[key]
        # * As based on triangle[i].length == triangle[i - 1].length + 1
        # * Anytime len(triangle) == len(triangle[n])
        if row > end:
            return float("inf")
        if row == end:
            return triangle[row][col]

        cache[key] = triangle[row][col] + min(_getMinPath(row + 1, col),
                                              _getMinPath(row + 1, col + 1))
        return cache[key]

    return _getMinPath(0, 0)


print(minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(minimumTotal(triangle=[[-10]]))
