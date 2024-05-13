"""
? Pattern: Decision Making
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: prices = [1,3,2,8,4,9], fee = 2
    Output: 8
    Explanation: The maximum profit can be achieved by:
        - Buying at prices[0] = 1
        - Selling at prices[3] = 8
        - Buying at prices[4] = 4
        - Selling at prices[5] = 9
        The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
* Example 2:
    Input: prices = [1,3,7,5,10,3], fee = 3
    Output: 6
"""


def maxProfit(prices: list[int], fee: int) -> int:
    total_days = len(prices)
    cache = {}

    def _getMaxProfit(day: int, ownStock: bool) -> int:
        key = (day, ownStock)
        if key in cache:
            return cache[key]

        if day == total_days:
            return 0

        if ownStock:  # SELL OR DO-NOTHING
            profit = max(
                _getMaxProfit(day + 1, False) - fee + prices[day],
                _getMaxProfit(day + 1, ownStock)
            )
        else:  # BUY OR DO-NOTHING
            profit = max(
                _getMaxProfit(day + 1, True) - prices[day],
                _getMaxProfit(day + 1, ownStock)

            )
        cache[key] = profit
        return cache[key]
    return _getMaxProfit(0, False)


print(maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
print(maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3))
