"""
* Example 1:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]
* Example 2:
    Input: s = "a"
    Output: [["a"]]
"""


def partition(s: str) -> list[list[str]]:
    res = []
    len_s = len(s)
    def isPali(x): return x == x[::-1]

    def _backtrack(idx: int, partition: list):
        if idx == len_s:
            res.append(partition[:])
            return
        for jdx in range(idx, len_s):
            cur_str = s[idx: jdx + 1]
            if isPali(cur_str):
                partition.append(cur_str)
                _backtrack(jdx + 1, partition)
                partition.pop()

    _backtrack(0, [])
    return res


print(partition(s="aab"))
# print(partition(s="a"))
