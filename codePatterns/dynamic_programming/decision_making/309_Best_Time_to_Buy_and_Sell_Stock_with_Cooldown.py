"""
? Pattern: Decision Making
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: prices = [1,2,3,0,2]
    Output: 3
    Explanation: transactions = [buy, sell, cooldown, buy, sell]
* Example 2:
    Input: prices = [1]
    Output: 0
"""


def maxProfit(prices: list[int]) -> int:
    total_days = len(prices)
    cache = {}

    def _getMaxProfit(day: int, ownStock: bool) -> int:
        key = (day, ownStock)
        if key in cache:
            return cache[key]

        if day >= total_days:
            return 0

        if ownStock:  # ? HAVE A STOCK
            # * CAN TO SELL or DO NOTHING
            #   ! day +2 as ther's a cooldown period and can't buy next day.
            #   ! and no restriction on transaction thus k is not used
            profit = max(_getMaxProfit(day + 2, False) + prices[day],
                         _getMaxProfit(day + 1, ownStock))
        else:  # ? DON'T HAVE A STOCK
            # * CAN BUY or DO NOTHING
            profit = max(_getMaxProfit(day + 1, True) - prices[day],
                         _getMaxProfit(day + 1, ownStock))

        cache[key] = profit
        return cache[key]
    return _getMaxProfit(0, False)


print(maxProfit(prices=[1, 2, 3, 0, 2]))
print(maxProfit(prices=[1]))
