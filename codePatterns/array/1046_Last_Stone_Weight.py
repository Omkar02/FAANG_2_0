"""
* Example 1:
    Input: stones = [2,7,4,1,8,1]
    Output: 1
    Explanation: 
    We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
    we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
    we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
    we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

* Example 2:
    Input: stones = [1]
    Output: 1
"""

import heapq


def lastStoneWeight(stones: list[int]) -> int:
    """
    The solution here is create a maxHeap and take both stones 
    and crush it together
    """
    # ? a -ve sigh is used as python only has minHeap so to make minHeap function like maxHeap
    max_heap = [-s for s in stones]
    heapq.heapify(max_heap)
    while len(max_heap) > 1:
        first_stone = heapq.heappop(max_heap)
        second_stone = heapq.heappop(max_heap)

        if first_stone != second_stone:
            diff = first_stone - second_stone
            heapq.heappush(max_heap, diff)

    # Return the smallest possible weight of the left stone.
    # ?  If there are no stones left, return 0, for array with even and equal stone weight...
    return abs(max_heap[0]) if max_heap else 0


print(lastStoneWeight(stones=[2, 7, 4, 1, 8]))
print(lastStoneWeight(stones=[1]))
print(lastStoneWeight(stones=[3, 7, 2]))
print(lastStoneWeight(stones=[9, 10, 1, 7, 3]))
