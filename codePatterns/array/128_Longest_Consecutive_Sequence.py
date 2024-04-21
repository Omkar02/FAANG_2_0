"""
* Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is[1, 2, 3, 4]. Therefore its length is 4.
* Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9
"""


def longestConsecutive(nums: list[int]) -> int:
    max_len = float('-inf')
    lookup = set(nums)
    for n in nums:
        if n - 1 not in lookup:
            cur_num = n
            seq_len = 1
            while cur_num + 1 in lookup:
                seq_len += 1
                cur_num += 1
            max_len = max(max_len, seq_len)
    return max_len


print(longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
print(longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
