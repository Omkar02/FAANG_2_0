"""
? Pattern: Decision Making
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: cost = [10,15,20]
    Output: 15
    Explanation: You will start at index 1.
        - Pay 15 and climb two steps to reach the top.
    The total cost is 15.
* Example 2:
        Input: cost = [1,100,1,1,1,100,1,1,100,1]
        Output: 6
        Explanation: You will start at index 0.
            - Pay 1 and climb two steps to reach index 2.
            - Pay 1 and climb two steps to reach index 4.
            - Pay 1 and climb two steps to reach index 6.
            - Pay 1 and climb one step to reach index 7.
            - Pay 1 and climb two steps to reach index 9.
            - Pay 1 and climb one step to reach the top.
        The total cost is 6.
"""


def minCostClimbingStairs(cost: list[int]) -> int:
    len_cost = len(cost)

    def _getMinCost(idx: int) -> int:
        if idx < 2:
            return cost[idx]

        return cost[idx] + min(_getMinCost(idx - 1),
                               _getMinCost(idx - 2))

    return min(_getMinCost(len_cost - 1), _getMinCost(len_cost - 2))


print(minCostClimbingStairs(cost=[10, 15, 20]))
print(minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
