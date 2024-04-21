"""
* Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        The distinct triplets are [-1,0,1] and [-1,-1,2].
    ! Notice that the order of the output and the order of the triplets does not matter.
* Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.
* Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.
"""


def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = set()
    target = 0
    nums_len = len(nums)
    for idx in range(len(nums) - 2):
        left = idx + 1
        right = nums_len - 1

        while left < right:
            curr_sum = nums[idx] + nums[left] + nums[right]
            if curr_sum == target:
                res.add((nums[idx], nums[left], nums[right]))
                left += 1
                right -= 1

            elif curr_sum > target:
                right -= 1

            else:
                left += 1
    return [list(x) for x in res]


print(threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(threeSum(nums=[0, 1, 1]))
print(threeSum(nums=[0, 0, 0]))
