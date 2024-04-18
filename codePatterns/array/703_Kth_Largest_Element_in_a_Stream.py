"""
* Example 1:
    Input
        ["KthLargest", "add", "add", "add", "add", "add"]
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    
    Output
        [null, 4, 5, 5, 8, 8]

    Explanation
        KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
        kthLargest.add(3);   // return 4
        kthLargest.add(5);   // return 5
        kthLargest.add(10);  // return 5
        kthLargest.add(9);   // return 8
        kthLargest.add(4);   // return 8
"""

import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.nums = nums
        self.k = k

        heapq.heapify(self.nums)  # this is a minHeap...

        while len(nums) > self.k:
            heapq.heappop(self.nums)
            print(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        print(self.nums[0])
        return self.nums[0]


kthLargest = KthLargest(3, [4, 5, 8, 2])
kthLargest.add(3)   # return 4
kthLargest.add(5)   # return 5
kthLargest.add(10)  # return 5
kthLargest.add(9)   # return 8
kthLargest.add(4)   # return 8
