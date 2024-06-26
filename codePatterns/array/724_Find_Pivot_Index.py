"""
*_Example 1:.py
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:
    The pivot index is 3.
    Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
    Right sum = nums[4] + nums[5] = 5 + 6 = 11
* Example 2:
    Input: nums = [1,2,3]
    Output: -1
    Explanation:
    There is no index that satisfies the conditions in the problem statement.
* Example 3:
    Input: nums = [2,1,-1]
    Output: 0
    Explanation:
    The pivot index is 0.
    Left sum = 0 (no elements to the left of index 0)
    Right sum = nums[1] + nums[2] = 1 + -1 = 0
"""


def pivotIndex(nums: list[int]) -> int:
    total_sum = sum(nums)
    left_sum = 0
    if left_sum == total_sum - nums[0]:
        return 0

    for idx, n in enumerate(nums):
        if left_sum == (total_sum - left_sum - n):
            return idx
        left_sum += n
    return -1


print(pivotIndex(nums=[1, 7, 3, 6, 5, 6]))
print(pivotIndex(nums=[1, 2, 3]))
print(pivotIndex(nums=[2, 1, -1]))



