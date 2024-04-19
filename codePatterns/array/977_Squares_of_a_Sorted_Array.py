"""
* Example 1:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
                 After sorting, it becomes [0,1,9,16,100].
* Example 2:
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

"""


def sortedSquares(nums: list[int]) -> list[int]:
    left_idx, right_idx = 0, len(nums)-1
    curr_idx = right_idx
    res = [None for _ in nums]
    while left_idx <= right_idx:
        left_val, right_val = nums[left_idx]**2, nums[right_idx]**2

        if left_val > right_val:
            res[curr_idx] = left_val
            left_idx += 1
        else:
            res[curr_idx] = right_val
            right_idx -= 1

        curr_idx -= 1
    return res


print(sortedSquares(nums=[-4, -1, 0, 3, 10]))
print(sortedSquares(nums=[-7, -3, 2, 3, 11]))
