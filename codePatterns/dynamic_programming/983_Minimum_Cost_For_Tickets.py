"""
? Pattern: Minimum (Maximum) Path to Reach a Target
? Approach: TOP DOWN | Reccurssion + Memoization
* Example 1:
    Input: days = [1,4,6,7,8,20], costs = [2,7,15]
    Output: 11
    Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
        On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
        On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
        On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
        In total, you spent $11 and covered all the days of your travel.
* Example 2:
    Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
    Output: 17
    Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
        On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
        On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
        In total, you spent $17 and covered all the days of your travel.
"""


def mincostTickets(days: list[int], costs: list[int]) -> int:
    last_day = max(days)
    traveling_days = set(days)
    cache = {}

    def _getMinCostReq(cur_day: int) -> int:
        key = (cur_day)
        if key in cache:
            return cache[key]
        if cur_day > last_day:
            # * BASE CASE
            return 0
        if cur_day not in traveling_days:
            # * FOR DAYS NOT TRAVELING THE COST WOULD BE THE SAME AS PREVIOUS
            # * THUS SKIP IT..
            cache[key] = _getMinCostReq(cur_day + 1)
            return cache[key]

        else:
            # * HERE THERE ARE 3 CHOICES TO TAKE PASS FOR 1, 7 OR 30 DAYS
            cache[key] = min(_getMinCostReq(cur_day + 1) + costs[0],
                             _getMinCostReq(cur_day + 7) + costs[1],
                             _getMinCostReq(cur_day + 30) + costs[2])
            return cache[key]

    return _getMinCostReq(1)


print(mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))
print(mincostTickets(
    days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31],
    costs=[2, 7, 15]
))
