"""
* Example 1:
    Input: nums = [1, 2, 3]
    Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
* Example 2:
    Input: nums = [0, 1]
    Output: [[0, 1], [1, 0]]
* Example 3:
    Input: nums = [1]
    Output: [[1]]
"""


def permute(nums: list[int]) -> list[list[int]]:
    permutations = []
    _helper(0, nums, permutations)
    return permutations


def swap(n1, n2, nums):  nums[n1], nums[n2] = nums[n2], nums[n1]


def _helper(idx, nums, permutations):
    if idx == len(nums) - 1:
        permutations.append(nums[:])
    else:
        for jdx in range(idx, len(nums)):
            swap(idx, jdx, nums)
            _helper(idx + 1, nums, permutations)
            swap(idx, jdx, nums)


print(permute(nums=[1, 2, 3]))
print(permute(nums=[0, 1]))
print(permute(nums=[1]))
