"""
? Pattern: Distinct Ways
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: n = 2, rollMax = [1,1,2,2,2,3]
    Output: 34
    Explanation: There will be 2 rolls of die, if there are no constraints on the die, 
                there are 6 * 6 = 36 possible combinations. In this case, looking at 
                rollMax array, the numbers 1 and 2 appear at most once consecutively, 
                therefore sequences (1,1) and (2,2) cannot occur, 
                so the final answer is 36-2 = 34.
* Example 2:
    Input: n = 2, rollMax = [1,1,1,1,1,1]
    Output: 30
* Example 3:
    Input: n = 3, rollMax = [1,1,1,2,2,3]
    Output: 181
"""


def dieSimulator(n: int, rollMax: list[int]) -> int:
    MOD = 1000000007
    roll_face = range(6)

    def _getDistinctSequence(steps: int, pre_val: int, prev_freq: int) -> int:
        if not steps:
            # * this means we have found a vaild sequence
            return 1

        res = 0
        for cur_val in roll_face:
            if cur_val != pre_val:
                # * this is we seeing it for the first time thus freq is 1
                res += _getDistinctSequence(steps - 1, cur_val, 1)
            elif prev_freq + 1 <= rollMax[cur_val]:
                # * this is we seeing repeteated sequence like `1, 1`
                res += _getDistinctSequence(steps - 1, cur_val, prev_freq + 1)
        return res

    return sum(_getDistinctSequence(n - 1, idx, 1) for idx in roll_face) % MOD


print(dieSimulator(n=2, rollMax=[1, 1, 2, 2, 2, 3]))
print(dieSimulator(n=2, rollMax=[1, 1, 1, 1, 1, 1]))
print(dieSimulator(n=3, rollMax=[1, 1, 1, 2, 2, 3]))
