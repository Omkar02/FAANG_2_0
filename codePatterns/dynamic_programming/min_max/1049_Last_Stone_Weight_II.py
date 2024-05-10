"""
? Pattern: Minimum (Maximum) Path to Reach a Target
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: stones = [2,7,4,1,8,1]
    Output: 1
    Explanation:
        We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
        we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
        we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
        we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.
* Example 2:
    Input: stones = [31,26,33,21,40]
    Output: 5
"""


def lastStoneWeightII(stones: list[int]) -> int:
    """
    * Recurssion Tree
        dp(0, 0)
        |-- dp(1, 2)  # Take the first stone
        |   |-- dp(2, 9)  # Take the second stone
        |   |-- dp(2, -5)  # Don't take the second stone
        |-- dp(1, -2)  # Don't take the first stone
            |-- dp(2, 5)  # Take the second stone
            |-- dp(2, -5)  # Don't take the second stone
    """
    len_stones = len(stones)
    cache = {}

    def _getLastStone(idx, sum_stone):
        key = (idx, sum_stone)
        if key in cache:
            return cache[key]
        if idx == len_stones:
            return sum_stone

        take = _getLastStone(idx + 1, abs(sum_stone + stones[idx]))
        not_take = _getLastStone(idx + 1, abs(sum_stone - stones[idx]))

        cache[key] = min(take, not_take)
        return cache[key]
    return _getLastStone(0, 0)


print(lastStoneWeightII(stones=[2, 7, 4, 1, 8, 1]))
print(lastStoneWeightII(stones=[31, 26, 33, 21, 40]))
