"""
? Pattern: Minimum (Maximum) Path to Reach a Target
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    Output: 4
* Example 2:
    Input: matrix = [["0","1"],["1","0"]]
    Output: 1
* Example 3:
    Input: matrix = [["0"]]
    Output: 0
"""


"""
! |------*** EXPLAINATION ***------|
    INPUT : ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]


    PASS 1: ["1", "0", "1", "0", "0"],
            ["1", "0", "0", "0", "0"],
            ["1", "0", "0", "0", "0"],
            ["1", "0", "0", "0", "0"]
    
    PASS 2: ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],  mat[1][1] = 0 # due to the val is 0 
            ["1", "0", "0", "0", "0"],  mat[1][2] = 1 + min(0, 0, 1) # cell val is 1
            ["1", "0", "0", "0", "0"]

    PASS 3 & 4: ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "2", "2"], here there are two sq with length of 2 with all one's
                ["1", "0", "0", "0", "0"]

"""


def maximalSquare(matrix: list[list[str]]) -> int:
    cache = {}
    row_len, col_len = len(matrix), len(matrix[0])

    def _getMaxSquare(row: int, col: int) -> int:
        key = (row, col)
        if key in cache:
            return cache[key]
        if row >= row_len or col >= col_len or matrix[row][col] == "0":
            return 0

        cache[key] = 1 + min(_getMaxSquare(row + 1, col),
                             _getMaxSquare(row, col + 1),
                             _getMaxSquare(row + 1, col + 1))

        return cache[key]

    max_square = 0
    for row in range(row_len):
        for col in range(col_len):
            max_square = max(max_square, _getMaxSquare(row, col))
    return max_square**2


print(maximalSquare(matrix=[["1", "0", "1", "0", "0"],
                            ["1", "0", "1", "1", "1"],
                            ["1", "1", "1", "1", "1"],
                            ["1", "0", "0", "1", "0"]]))

print(maximalSquare(matrix=[["0", "1"],
                            ["1", "0"]]))

print(maximalSquare(matrix=[["0"]]))
