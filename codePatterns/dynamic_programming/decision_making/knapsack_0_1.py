"""
* You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 

* Note that we have only one quantity of each item.

* In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. 

* Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or dont pick it (0-1 property).

* Example 1:
    Input: N = 3, W = 4, values = {1,2,3}, weight = {4,5,1}
    Output: 3
    Explanation: Choose the last item that weighs 1 unit and holds a value of 3. 
* Example 2:
    Input: N = 3, W = 3, values = {1,2,3}, weight = {4,5,6}
    Output: 0
    Explanation: Every item has a weight exceeding the knapsack's capacity (3).

? Your Task:
    ? Complete the function knapSack() which takes maximum capacity W, weight array wt[], value array val[], and the number of items n as a parameter and returns the maximum possible value you can get.
"""


def knapSack(N: int, W: int, values: list[int], weight: list[int]) -> int:
    """
    @param N:           len of values and weight
    @param W:           knapsack capacity
    @param values:      items value
    @param weight:      items weight

    @return:            sum of values in the knapsack of given capacity W
    """
    cache = {}

    def _getMaxValue(idx: int, curr_weight: int) -> int:
        key = (idx, curr_weight)
        if key in cache:
            return cache[key]

        if curr_weight < 0 or idx == N:
            # * IF THERE IS NOT ENEOUGH CAP or
            # * IDX HAS REACHED THE END
            return 0

        if weight[idx] > curr_weight:
            # * IF CURRENT WEIGHT/VALUE CAN BE FITTED IN THE REMAINING CAP SKIP IT
            return _getMaxValue(idx + 1, curr_weight)

        # * THRE ARE 2 DESICION
        # *     1. TO TAKE THE VALUE
        # *     2. NOT TO TAKE THE VALUE AND MOVE ON..
        taking = values[idx] + _getMaxValue(idx + 1, curr_weight - weight[idx])
        not_taking = _getMaxValue(idx + 1, curr_weight)

        cache[key] = max(taking, not_taking)
        return cache[key]

    return _getMaxValue(0, W)


print(knapSack(N=3, W=4, values=[1, 2, 3], weight=[4, 5, 1]))
print(knapSack(N=3, W=3, values=[1, 2, 3], weight=[4, 5, 6]))
