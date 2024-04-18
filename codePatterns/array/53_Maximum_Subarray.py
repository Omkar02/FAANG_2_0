"""
* Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.
* Example 2:
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.
* Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""


def maxSubArray(nums: list[int]) -> int:
    curr_val, max_val = 0, float("-inf")
    for n in nums:
        curr_val += n
        max_val = max(max_val, curr_val)
        if curr_val < 0:
            curr_val = 0
    return max_val


print(maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray(nums=[1]))
print(maxSubArray(nums=[5, 4, -1, 7, 8]))
