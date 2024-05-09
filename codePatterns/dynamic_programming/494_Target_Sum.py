"""
? Pattern: Distinct Ways
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: nums = [1,1,1,1,1], target = 3
    Output: 5
    Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
        -1 + 1 + 1 + 1 + 1 = 3
        +1 - 1 + 1 + 1 + 1 = 3
        +1 + 1 - 1 + 1 + 1 = 3
        +1 + 1 + 1 - 1 + 1 = 3
        +1 + 1 + 1 + 1 - 1 = 3
* Example 2:
    Input: nums = [1], target = 1
    Output: 1
"""


def findTargetSumWays(nums: list[int], target: int) -> int:
    nums_len = len(nums)
    cache = {}

    def _getAllWays(idx: int, cur_target: int) -> int:
        key = (idx, cur_target)
        if key in cache:
            return cache[key]

        if idx == nums_len and cur_target == 0:
            return 1
        if idx >= nums_len:
            return 0

        adding = _getAllWays(idx + 1, cur_target + nums[idx])
        subtracting = _getAllWays(idx + 1, cur_target - nums[idx])

        cache[key] = adding + subtracting
        return cache[key]

    return _getAllWays(0, target)


print(findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
print(findTargetSumWays(nums=[1], target=1))
