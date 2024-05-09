"""
? Pattern: Distinct Ways
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: n = 3, k = 2, row = 0, column = 0
    Output: 0.06250
    Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
        From each of those positions, there are also two moves that will keep the knight on the board.
        The total probability the knight stays on the board is 0.0625.
* Example 2:
    Input: n = 1, k = 0, row = 0, column = 0
    Output: 1.00000
"""


def knightProbability(n: int, k: int, row: int, column: int) -> float:
    row_range = col_range = range(n)
    # ? THERE ARE 8 DIFFERENT MOVES A KNIGHT CAN TAKE THUS THE PROBABLIT IS 1 / 8
    PROBABLITY = float(1/8)
    ALL_PATH = [
        (1, -2), (2, -1), (2, 1), (1, 2),
        (-1, 2), (-2, 1), (-2, -1), (-1, -2)
    ]
    CACHE = {}

    def isValid(row, col): return row in row_range and col in col_range

    def _getKinghtProbablity(row: int, col: int, cur_k: int):
        key = (row, col, cur_k)
        if key in CACHE:
            return CACHE[key]
        if cur_k == 0:
            return 1
        if not isValid(row, col):
            return 0

        cur_prob = 0
        for pos_x, pos_y in ALL_PATH:
            new_x, new_y = row + pos_x, col + pos_y

            if not isValid(new_x, new_y):
                continue

            cur_prob += PROBABLITY * \
                _getKinghtProbablity(new_x, new_y, cur_k-1)
        CACHE[key] = cur_prob
        return CACHE[key]

    return _getKinghtProbablity(row, column, k) if k != 0 else float(isValid(row, column))


print(knightProbability(n=3, k=2, row=0, column=0))
print(knightProbability(n=1, k=0, row=0, column=0))

print(knightProbability(n=8, k=30, row=6, column=4))  # 0.00019
