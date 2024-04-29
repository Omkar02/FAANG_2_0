"""
* Example 1:
    Input: n = 4, k = 2
    Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    Explanation: There are 4 choose 2 = 6 total combinations.
    ! Note that combinations are unordered, i.e., 
    ! [1,2] and [2,1] are considered to be the same combination.
* Example 2:
    Input: n = 1, k = 1
    Output: [[1]]
    Explanation: There is 1 choose 1 = 1 total combination.
"""


def combine(n: int, k: int) -> list[list[int]]:
    res = []

    def backTrack(idx, cur_arr):
        if len(cur_arr) == k:
            res.append(cur_arr[:])
        else:
            for jdx in range(idx, n + 1):
                cur_arr.append(jdx)
                backTrack(jdx + 1, cur_arr)
                cur_arr.pop()

    backTrack(1, [])
    return res


print(combine(n=4, k=2))
print(combine(n=1, k=1))
