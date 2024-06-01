"""
* Example 1:
    Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]
* Example 2:
    Input: board = [["a","b"],["c","d"]], words = ["abcb"]
    Output: []
"""


class Trie:
    def __init__(self) -> None:
        self.word_mapping = {}
        self.end_word = '*'

    def insert(self, words: list[str]) -> 'Trie':
        for word in words:
            cur_map = self.word_mapping
            for w in word:
                if w not in cur_map:
                    cur_map[w] = {}
                cur_map = cur_map[w]
            cur_map[self.end_word] = word

        return self.get_mapping()

    def get_mapping(self) -> dict:
        return self.word_mapping


class Solution:
    def __init__(self) -> None:
        self.visited = set()
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        self.board = None
        self.row_range = None
        self.col_range = None

        self.res = set()

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        self.board = board
        self.row_range = range(len(board))
        self.col_range = range(len(board[0]))

        trie_map = Trie().insert(words=words)

        for row in self.row_range:
            for col in self.col_range:
                cur_letter = self.board[row][col]
                if cur_letter in trie_map:
                    self._dfs(row, col, trie_map, "")
        return self.res

    def _dfs(self, row: int, col: int, w_map: dict, w_temp: str) -> None:
        key = (row, col)
        if row not in self.row_range or col not in self.col_range or key in self.visited:
            return

        cur_letter = self.board[row][col]
        if cur_letter not in w_map:
            return
        # ---------- MAIN LOGIN ----------

        self.visited.add(key)
        w_temp += cur_letter
        w_map = w_map[cur_letter]

        # --------------------------------
        for x, y in self.directions:
            new_row, new_col = row + x, col + y
            self._dfs(new_row, new_col, w_map, w_temp)

        # ---------- LOGIN FOR FINDING THE NODE ----------
        if "*" in w_map and w_map["*"] == w_temp:
            self.res.add(w_temp)
        self.visited.remove(key)
        # -----------------------------------------------


s: Solution = Solution()
print(s.findWords(board=[["o", "a", "a", "n"],
                         ["e", "t", "a", "e"],
                         ["i", "h", "k", "r"],
                         ["i", "f", "l", "v"]], words=["oath", "pea", "eat", "rain"]))

s: Solution = Solution()
print(s.findWords(board=[["a", "b"],
                         ["c", "d"]], words=["abcb"]))


s: Solution = Solution()
# Expected = ["abcd", "abc"]
print(s.findWords(board=[["a", "b", "c", "e"],
                         ["x", "x", "c", "d"],
                         ["x", "x", "b", "a"]], words=["abc", "abcd"]))


s: Solution = Solution()
# Exptected = ["oath","eat","hklf","hf"]
print(s.findWords(board=[["o", "a", "a", "n"],
                         ["e", "t", "a", "e"],
                         ["i", "h", "k", "r"],
                         ["i", "f", "l", "v"]], words=["oath", "pea", "eat", "rain", "hklf", "hf"]))
