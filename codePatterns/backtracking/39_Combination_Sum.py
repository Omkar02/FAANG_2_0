"""
* Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
        2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
        7 is a candidate, and 7 = 7.
        These are the only two combinations.
* Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]
* Example 3:
    Input: candidates = [2], target = 1
    Output: []
"""


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    candidates_len = len(candidates)

    def _backtrack(idx: int, cur_arr: list):
        # print(cur_arr)
        if idx > candidates_len or sum(cur_arr) > target:
            return
        if sum(cur_arr) == target:
            res.append(cur_arr[:])
            return

        for jdx in range(idx, candidates_len):
            cur_arr.append(candidates[jdx])
            _backtrack(jdx, cur_arr)
            cur_arr.pop()
        # print()
    _backtrack(0, [])
    return res


print(combinationSum(candidates=[2, 3, 6, 7], target=7))
print(combinationSum(candidates=[2, 3, 5], target=8))
print(combinationSum(candidates=[2], target=1))
