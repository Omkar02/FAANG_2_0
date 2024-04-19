"""
* Example 1:
    Input: nums = [3,1,2,4]
    Output: [2,4,3,1]
    Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
* Example 2:
    Input: nums = [0]
    Output: [0]
"""


def sortArrayByParity(nums: list[int]) -> list[int]:
    left_p, right_p = 0, len(nums) - 1
    def isEven(x): return x % 2 == 0
    while left_p < right_p:
        if isEven(nums[left_p]):
            left_p += 1
            continue
        if not isEven(nums[right_p]):
            right_p -= 1
            continue
        nums[left_p], nums[right_p] = nums[right_p], nums[left_p]
        left_p += 1
        right_p -= 1
    return nums


print(sortArrayByParity(nums=[3, 1, 2, 4]))
print(sortArrayByParity(nums=[0]))
