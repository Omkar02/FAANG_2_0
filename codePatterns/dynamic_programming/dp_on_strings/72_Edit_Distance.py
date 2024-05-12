"""
? Pattern: DP on string
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation: 
        horse -> rorse (replace 'h' with 'r')
        rorse -> rose (remove 'r')
        rose -> ros (remove 'e')
* Example 2:
    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation: 
        intention -> inention (remove 't')
        inention -> enention (replace 'i' with 'e')
        enention -> exention (replace 'n' with 'x')
        exention -> exection (replace 'n' with 'c')
        exection -> execution (insert 'u')
"""


def minDistance(word1: str, word2: str) -> int:
    word1_len = len(word1)
    word2_len = len(word2)

    cache = {}

    def _getMinChanges(idx_one: int, idx_two: int) -> int:
        key = (idx_one, idx_two)
        if key in cache:
            return cache[key]

        if not idx_one:
            return idx_two
        if not idx_two:
            return idx_one

        if word1[idx_one - 1] == word2[idx_two - 1]:
            cache[key] = _getMinChanges(idx_one - 1, idx_two - 1)
            return cache[key]

        # ? INSERT OPERATION  = IDX_ONE - 1, IDX_TWO
        # ? DELETE OPERATION  = IDX_ONE, IDX_TWO - 1
        # ? REPLACE OPERATION = IDX_ONE - 1, IDX_TWO -1

        cache[key] = 1 + min(_getMinChanges(idx_one - 1, idx_two),
                             _getMinChanges(idx_one, idx_two - 1),
                             _getMinChanges(idx_one - 1, idx_two - 1))
        return cache[key]

    return _getMinChanges(word1_len, word2_len)


print(minDistance(word1="horse", word2="ros"))
print(minDistance(word1="intention", word2="execution"))
