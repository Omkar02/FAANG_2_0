"""
* Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: 
        [
        [1,1,6],
        [1,2,5],
        [1,7],
        [2,6]
        ]
* Example 2:
    Input: candidates = [2,5,2,1,2], target = 5
    Output: 
        [
        [1,2,2],
        [5]
        ]
"""


def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    n = len(candidates)
    res = []

    def _backtrack(idx: int, curr_arr: list, tar: int):
        if tar == 0:
            res.append(curr_arr[:])
        else:
            prev = -1
            for jdx in range(idx, n):
                if prev == candidates[jdx]:
                    continue
                curr_arr.append(candidates[jdx])
                _backtrack(idx + 1, curr_arr, tar-candidates[jdx])
                curr_arr.pop()
                prev = candidates[jdx]

    _backtrack(0, [], target)
    return res


print(combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
print(combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
