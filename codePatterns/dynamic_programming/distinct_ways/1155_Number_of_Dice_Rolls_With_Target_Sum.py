"""
? Pattern: Distinct Ways
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: n = 1, k = 6, target = 3
    Output: 1
    Explanation: You throw one die with 6 faces.
        There is only one way to get a sum of 3.
* Example 2:
    Input: n = 2, k = 6, target = 7
    Output: 6
    Explanation: You throw two dice, each with 6 faces.
        There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
* Example 3:
    Input: n = 30, k = 30, target = 500
    Output: 222616187
    Explanation: The answer must be returned modulo 109 + 7.
"""


def numRollsToTarget(n: int, k: int, target: int) -> int:
    cache = {}
    MOD = 10**9 + 7

    def _getTotalWays(dice: int, cur_target: int) -> int:
        key = (dice, cur_target)
        if key in cache:
            return cache[key]
        if dice == 0 and cur_target == 0:
            return 1
        if dice == 0 or cur_target < 0:
            return 0

        total_ways = 0
        for face in range(1, k + 1):
            total_ways += _getTotalWays(dice - 1, cur_target - face)

        cache[key] = total_ways
        return cache[key]

    return _getTotalWays(n, target) % MOD


print(numRollsToTarget(n=1, k=6, target=3))
print(numRollsToTarget(n=2, k=6, target=7))
print(numRollsToTarget(n=30, k=30, target=500))
