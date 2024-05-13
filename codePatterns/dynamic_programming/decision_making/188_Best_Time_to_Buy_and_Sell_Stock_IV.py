"""
? Pattern: Decision Making
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: k = 2, prices = [2,4,1]
    Output: 2
    Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
* Example 2:
    Input: k = 2, prices = [3,2,6,5,0,3]
    Output: 7
    Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. 
        Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""


def maxProfit(k: int, prices: list[int]) -> int:
    total_days = len(prices)
    cache = {}

    def _getMaxProfit(day: int, k: int, ownStock: bool) -> int:
        key = (day, k, ownStock)
        if key in cache:
            return cache[key]

        if day == total_days or k == 0:
            return 0

        if ownStock:  # SELL OR DO-NOTHING
            profit = max(
                _getMaxProfit(day + 1, k - 1, False) + prices[day],
                _getMaxProfit(day + 1, k, ownStock)
            )
        else:  # BUY OR DO-NOTHING
            profit = max(
                _getMaxProfit(day + 1, k, True) - prices[day],
                _getMaxProfit(day + 1, k, ownStock)
            )

        cache[key] = profit
        return cache[key]

    return _getMaxProfit(0, k, False)


print(maxProfit(k=2, prices=[2, 4, 1]))
print(maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))
