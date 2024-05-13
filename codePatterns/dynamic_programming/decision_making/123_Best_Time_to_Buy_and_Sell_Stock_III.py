"""
? Pattern: Decision Making
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: prices = [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
    Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
* Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
* Example 3:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


def maxProfit(prices: list[int]) -> int:
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

    # ! HERE THE TRANACTION THAT CAN BE PERFORMED IS 2
    return _getMaxProfit(0, 2, False)


print(maxProfit(prices=[3, 3, 5, 0, 0, 3, 1, 4]))
print(maxProfit(prices=[1, 2, 3, 4, 5]))
print(maxProfit(prices=[7, 6, 4, 3, 1]))
