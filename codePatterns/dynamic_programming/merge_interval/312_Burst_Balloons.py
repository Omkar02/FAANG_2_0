"""
? Pattern: Merge Intervals
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: nums = [3,1,5,8]
    Output: 167
    Explanation:
        nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
        coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
* Example 2:
    Input: nums = [1,5]
    Output: 10
"""


def maxCoins(nums: list[int]) -> int:
    # ? PADDING THE ARRAY WITH 1'S
    nums = [1] + nums + [1]
    nums_len = len(nums) - 1
    cache = {}

    def _getMaxCoins(left_idx: int, right_idx: int) -> int:
        key = (left_idx, right_idx)
        if key in cache:
            return cache[key]

        max_coins = 0
        for idx in range(left_idx + 1, right_idx):
            cur_coins = nums[left_idx] * nums[idx] * nums[right_idx]
            left_coins = _getMaxCoins(left_idx, idx)
            right_coins = _getMaxCoins(idx, right_idx)

            max_coins = max(max_coins, left_coins + cur_coins + right_coins)

        cache[key] = max_coins
        return cache[key]
    return _getMaxCoins(0, nums_len)


print(maxCoins(nums=[3, 1, 5, 8]))
print(maxCoins(nums=[1, 5]))
