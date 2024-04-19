"""
* Example 1:
    Input: nums = [8,1,2,2,3]
    Output: [4,0,1,1,3]
    Explanation: 
        For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
        For nums[1]=1 does not exist any smaller number than it.
        For nums[2]=2 there exist one smaller number than it (1). 
        For nums[3]=2 there exist one smaller number than it (1). 
        For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
* Example 2:
    Input: nums = [6,5,4,8]
    Output: [2,1,0,3]
* Example 3:
    Input: nums = [7,7,7,7]
    Output: [0,0,0,0]
"""


def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    lookup = {val: idx for idx, val in enumerate(sorted(nums, reverse=True))}
    nums_len = len(nums)
    return [nums_len - lookup[val] - 1 for val in nums]


print(smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]))
print(smallerNumbersThanCurrent(nums=[6, 5, 4, 8]))
print(smallerNumbersThanCurrent(nums=[7, 7, 7, 7]))
