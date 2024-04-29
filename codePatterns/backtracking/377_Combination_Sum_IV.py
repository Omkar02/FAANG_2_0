"""
* Example 1:
    Input: nums = [1,2,3], target = 4
    Output: 7
    Explanation:
        The possible combination ways are:
        (1, 1, 1, 1)
        (1, 1, 2)
        (1, 2, 1)
        (1, 3)
        (2, 1, 1)
        (2, 2)
        (3, 1)
        Note that different sequences are counted as different combinations.
* Example 2:
    Input: nums = [9], target = 3
    Output: 0
"""


def combinationSum4(nums: list[int], target: int) -> int:
    _cache = {}

    def _backtrack(currSum: int):
        if currSum in _cache:
            return _cache[currSum]
        if currSum == target:
            return 1
        if currSum > target:
            return 0

        total_val = 0
        for n in nums:
            total_val += _backtrack(currSum + n)

        _cache[currSum] = total_val
        return _cache[currSum]
    return _backtrack(0)


print(combinationSum4(nums=[1, 2, 3], target=4))
print(combinationSum4(nums=[9], target=3))
