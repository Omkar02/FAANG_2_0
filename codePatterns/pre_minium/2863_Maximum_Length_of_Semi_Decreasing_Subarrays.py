"""
    * Time Complexity   : O(N)
    * Space Complexity  : O(N)
    * Date              : 4, June 2024
"""
"""
* Example 1:
    Input: nums = [7,6,5,4,3,2,1,6,10,11]
    Output: 8
    Explanation: Take the subarray [7,6,5,4,3,2,1,6].
        The first element is 7 and the last one is 6 so the condition is met.
        Hence, the answer would be the length of the subarray or 8.
        It can be shown that there aren't any subarrays with the given condition with a length greater than 8.
* Example 2:
    Input: nums = [57,55,50,60,61,58,63,59,64,60,63]
    Output: 6
    Explanation: Take the subarray [61,58,63,59,64,60].
        The first element is 61 and the last one is 60 so the condition is met.
        Hence, the answer would be the length of the subarray or 6.
        It can be shown that there aren't any subarrays with the given condition with a length greater than 6.
* Example 3:
    Input: nums = [1,2,3,4]
    Output: 0
    Explanation: Since there are no semi-decreasing subarrays in the given array, the answer is 0.

"""


def maxSubarrayLength(nums: list[int]) -> int:
    # Stack Approach
    len_nums = len(nums)
    res = 0
    stack = []
    for idx in reversed(range(len_nums)):
        # * HAVING ALL THE MIN VALUES FROM THE REVERSED
        # * FOR EG.2:
        # *         STACK = [63, 60, 59, 58, 50]
        if not stack or nums[idx] < nums[stack[-1]]:
            stack.append(idx)

    # print([nums[i] for i in stack])
    for i in range(len_nums):
        while stack and nums[i] > nums[stack[-1]]:
            # * COMPERAING ALL THE POINTS WHICH
            # * SATISFY semi-decreasing subarray CRITERIA
            res = max(res, stack.pop() - i + 1)

    return res


print(maxSubarrayLength(nums=[7, 6, 5, 4, 3, 2, 1, 6, 10, 11]))
print(maxSubarrayLength(nums=[57, 55, 50, 60, 61, 58, 63, 59, 64, 60, 63]))
print(maxSubarrayLength(nums=[1, 2, 3, 4]))
