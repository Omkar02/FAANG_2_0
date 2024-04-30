"""
* Example 1:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true
* Example 2:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true
* Example 3:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false
"""


def exist(board: list[list[str]], word: str) -> bool:
    row_range = range(len(board))
    col_range = range(len(board[0]))

    def _backtrack(row: int, col: int, word_idx: int):
        if word_idx == len(word):
            return True
        if row not in row_range or col not in col_range:
            return False
        if board[row][col] != word[word_idx]:
            return False

        pre_val = board[row][col]
        board[row][col] = None

        positions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for x, y in positions:
            new_row, new_col = row + x, col + y
            if _backtrack(new_row, new_col, word_idx + 1):
                return True
        board[row][col] = pre_val
        return False

    for row in row_range:
        for col in col_range:
            if _backtrack(row, col, 0):
                return True
    return False


~print(exist(board=[["A", "B", "C", "E"],
                    ["S", "F", "C", "S"],
                    ["A", "D", "E", "E"]], word="ABCCED"))

print(exist(board=[["A", "B", "C", "E"],
                   ["S", "F", "C", "S"],
                   ["A", "D", "E", "E"]], word="SEE"))

print(exist(board=[["A", "B", "C", "E"],
                   ["S", "F", "C", "S"],
                   ["A", "D", "E", "E"]], word="ABCB"))
