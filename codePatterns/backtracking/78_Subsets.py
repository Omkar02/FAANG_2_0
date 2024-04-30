"""
* Example 1:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
* Example 2:
    Input: nums = [0]
    Output: [[],[0]]
"""


def subsets(nums: list[int]) -> list[list[int]]:
    res = []
    n = len(nums)

    def _backtrack(idx, curr_arr):

        res.append(curr_arr[:])

        for jdx in range(idx, n):
            # print(f'\tJDX = {jdx} | IDX = {idx}')
            curr_arr.append(nums[jdx])
            _backtrack(jdx+1, curr_arr)
            curr_arr.pop()
        # print(res)
    _backtrack(0, [])
    return res


print(subsets(nums=[1, 2, 3]))
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

print(subsets(nums=[0]))
[[], [0]]


"""
        JDX = 0 | IDX = 0
        JDX = 1 | IDX = 1
        JDX = 2 | IDX = 2
[[], [1], [1, 2], [1, 2, 3]]
[[], [1], [1, 2], [1, 2, 3]]
        JDX = 2 | IDX = 1
[[], [1], [1, 2], [1, 2, 3], [1, 3]]
[[], [1], [1, 2], [1, 2, 3], [1, 3]]
        JDX = 1 | IDX = 0
        JDX = 2 | IDX = 2
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
        JDX = 2 | IDX = 0
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
"""
