"""
? Pattern: Decision Making
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
* Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
"""


def maxProfit(prices: list[int]) -> int:
    total_days = len(prices)
    cache = {}

    def _getMaxProfit(day: int, k: int, ownStock: bool) -> int:
        """
        @param day:         the ith day
        @param k:           total transaction possible in a day 
                            #! k is used as only one tansation can be performed single time
        @param ownStock:    if you have a stock or not
        """

        key = (day, ownStock, k)
        if key in cache:
            return cache[key]

        if day == total_days or k == 0:
            return 0

        if ownStock:  # * IF WE OWN STOCK
            # ! WE CAN SELL IT OFF or WE DO NOTHING
            profit = max(_getMaxProfit(day + 1, k - 1,  False) + prices[day],
                         _getMaxProfit(day + 1, k, ownStock))

        else:  # * IF WE DON'T OWN STOCK
            # ! TO BUY IT OFF or WE DO NOTHING
            profit = max(_getMaxProfit(day + 1, k, True) -
                         prices[day], _getMaxProfit(day + 1, k, ownStock))

        cache[key] = profit
        return cache[key]
    return _getMaxProfit(0, 1, False)


print(maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(maxProfit(prices=[7, 6, 4, 3, 1]))
