"""
* Example 1:
    Input: k = 3, n = 7
    Output: [[1,2,4]]
    Explanation:
        1 + 2 + 4 = 7
        There are no other valid combinations.
* Example 2:
    Input: k = 3, n = 9
    Output: [[1,2,6],[1,3,5],[2,3,4]]
    Explanation:
        1 + 2 + 6 = 9
        1 + 3 + 5 = 9
        2 + 3 + 4 = 9
        There are no other valid combinations.
* Example 3:
    Input: k = 4, n = 1
    Output: []
    Explanation: There are no valid combinations.
        Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

"""


def combinationSum3(k: int, n: int) -> list[list[int]]:
    res = []

    def _backtrack(idx, curr_arr):
        if len(curr_arr) > k or sum(curr_arr) > n:
            return
        if len(curr_arr) == k and sum(curr_arr) == n:
            # print(curr_arr)
            res.append(curr_arr[:])
        else:
            for jdx in range(idx, 10):
                curr_arr.append(jdx)
                _backtrack(jdx + 1, curr_arr)
                curr_arr.pop()

    _backtrack(1, [])
    return res


print(combinationSum3(k=3, n=7))
print(combinationSum3(k=3, n=9))
print(combinationSum3(k=4, n=1))
