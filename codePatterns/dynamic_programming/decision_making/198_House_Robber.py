"""
? Pattern: Decision Making
? Approach: TOP DOWN | Reccurssion + Memoization


* Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
        Total amount you can rob = 1 + 3 = 4.
* Example 2:

    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
        Total amount you can rob = 2 + 9 + 1 = 12.
"""


def rob(nums: list[int]) -> int:
    nums_len = len(nums)
    cache = {}

    def _getMaxAmmount(idx):
        key = idx
        if key in cache:
            return cache[key]
        if idx == 0:
            return nums[0]
        if idx == 1:
            return max(nums[0], nums[1])

        # * THERE ARE TO OPTIONS EITHER TO SELECT THE ADJUCENT OR TO SKIP ALTOGETHER
        #   * IDX - 1 IS TO SKIP AND MOVE ON
        #   * IDX - 2 + NUMS[IDX] IS TO SELECT THE ADJUCENT...
        cache[key] = max(_getMaxAmmount(idx - 1),
                         _getMaxAmmount(idx-2) + nums[idx])
        return cache[key]
    return _getMaxAmmount(nums_len - 1)


print(rob(nums=[1, 2, 3, 1]))
print(rob(nums=[2, 7, 9, 3, 1]))
