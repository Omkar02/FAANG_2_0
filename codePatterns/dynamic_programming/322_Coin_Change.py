"""
? Pattern: Minimum (Maximum) Path to Reach a Target
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1
* Example 2:
    Input: coins = [2], amount = 3
    Output: -1
* Example 3:
    Input: coins = [1], amount = 0
    Output: 0
"""


# def coinChange(coins: list[int], amount: int) -> int:
#     coins_len = len(coins)
#     coins.sort(reverse=True)

#     cache = {}

#     def _minCoinReq(idx: int, cur_coins: list) -> int:
#         key = (idx, len(cur_coins), sum(cur_coins))
#         if key in cache:
#             print('-' * 20)
#             return cache[key]
#         if idx > coins_len or sum(cur_coins) > amount:
#             return float("inf")

#         if sum(cur_coins) == amount:
#             return len(cur_coins)

#         min_coins_req = float("inf")
#         for jdx in range(idx, coins_len):
#             cur_coins.append(coins[jdx])
#             min_coins_req = min(min_coins_req, _minCoinReq(jdx, cur_coins))
#             cur_coins.pop()

#         cache[key] = min_coins_req
#         print(min_coins_req)
#         return cache[key]
#     total_coins_req = _minCoinReq(0, [])
#     return total_coins_req if total_coins_req != float("inf") else -1

# This is faster than above...
def coinChange(coins: list[int], amount: int) -> int:
    coins_len = len(coins)
    coins.sort(reverse=True)

    cache = {}

    def _minCoinReq(idx: int, cur_amt: list) -> int:
        key = (idx, cur_amt)
        if key in cache:
            return cache[key]
        if idx > coins_len or cur_amt < 0:
            return float("inf")

        if cur_amt == 0:
            return 0

        min_coins_req = float("inf")
        for jdx in range(idx, coins_len):
            min_coins_req = min(min_coins_req,
                                1 + _minCoinReq(jdx, cur_amt-coins[jdx]))  # ? HERE

        cache[key] = min_coins_req
        return cache[key]

    total_coins_req = _minCoinReq(0, amount)
    return total_coins_req if total_coins_req != float("inf") else -1


print(coinChange(coins=[1, 2, 5], amount=11))
print(coinChange(coins=[2], amount=3))
print(coinChange(coins=[1], amount=0))
print(coinChange(coins=[3, 7, 405, 436], amount=8839))
