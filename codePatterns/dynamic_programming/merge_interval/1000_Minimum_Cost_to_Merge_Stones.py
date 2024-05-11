"""
? Pattern: Merge Intervals
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: stones = [3,2,4,1], k = 2
    Output: 20
    Explanation: We start with [3, 2, 4, 1].
        We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
        We merge [4, 1] for a cost of 5, and we are left with [5, 5].
        We merge [5, 5] for a cost of 10, and we are left with [10].
        The total cost was 20, and this is the minimum possible.
* Example 2:
    Input: stones = [3,2,4,1], k = 3
    Output: -1
    Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
* Example 3:
    Input: stones = [3,5,1,2,6], k = 3
    Output: 25
    Explanation: We start with [3, 5, 1, 2, 6].
        We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
        We merge [3, 8, 6] for a cost of 17, and we are left with [17].
        The total cost was 25, and this is the minimum possible.
"""


def mergeStones(stones: list[int], k: int) -> int:
    stones_len = len(stones)
    if (len(stones)-1) % (k-1):
        # ! IMPOSSIBLE AS THERE ARE NOT ENEOUGH PILES..
        return -1
    cache = {}

    def _getMinCost(start: int, end: int) -> int:
        key = (start, end)
        if key in cache:
            return cache[key]
        if end - start < k:
            # * THERE ARE NOT ENEOUGH PILES TO BE MERGED
            return 0

        min_cost = float('inf')
        for mid in range(start + 1, end, k - 1):
            min_cost = min(min_cost,
                           _getMinCost(start, mid) + _getMinCost(mid, end))

        if (end - start - 1) % (k - 1) == 0:
            # * WE GOT THE CORRECT PILE'S LETS MERGE IT...
            min_cost += sum([x for x in stones[start:end]])
        cache[key] = min_cost
        return cache[key]
    return _getMinCost(0, stones_len)


print(mergeStones(stones=[3, 2, 4, 1], k=2))
print(mergeStones(stones=[3, 2, 4, 1], k=3))
print(mergeStones(stones=[3, 5, 1, 2, 6], k=3))
