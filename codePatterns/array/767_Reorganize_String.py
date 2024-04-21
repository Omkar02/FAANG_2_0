"""
* Example 1:
    Input: s = "aab"
    Output: "aba"
* Example 2:
    Input: s = "aaab"
    Output: ""
"""

import heapq


def reorganizeString(s: str) -> str:
    """
    Explaination:
        * Pop the top two characters from the max heap (i.e., the ones with the highest frequency).
        * Append these two characters to the result string.
        * Decrement their frequencies and re-insert them back into the max heap.
    To Rembember:
        ! If only one character remains in the heap, make sure it doesn't exceed half of the 
        ! string length, otherwise, return an empty string.
    """
    max_heap = [(-s.count(val), val) for val in set(s)]
    # ! Check if there's a possible solution..

    if any(-char_count > (len(s) + 1) / 2 for char_count, _ in max_heap):
        return ""
    heapq.heapify(max_heap)
    ans = []
    while len(max_heap) >= 2:
        char_count_one, char_one = heapq.heappop(max_heap)
        char_count_two, char_two = heapq.heappop(max_heap)
        ans.extend([char_one, char_two])

        if char_count_one + 1:
            heapq.heappush(max_heap, (char_count_one+1, char_one))
        if char_count_two + 1:
            heapq.heappush(max_heap, (char_count_two+1, char_two))

    return "".join(ans) + (max_heap[0][1] if max_heap else "")


print(reorganizeString(s="aabcc"))
print(reorganizeString(s="aaab"))
print(reorganizeString(s="abbabbaaab"))
