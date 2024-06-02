"""
    * Time Complexity   : O(NLogN)
    * Space Complexity  : O(N)
    * Date              : 2, June 2024
"""

# * ---------------------------------------------------------------------------------------------------------------------------------------------
"""
* Example 1:
    Input
        ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
        [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]

    Output
        [null, null, null, true, false, true]

    Explanation
        RangeModule rangeModule = new RangeModule();
        rangeModule.addRange(10, 20);
        rangeModule.removeRange(14, 16);
        rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
        rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
        rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
"""

# ? WHAT IS BISECT = https://www.youtube.com/watch?v=o6QlOJCWwg0&ab_channel=AndreyIvanov%7CPython




import bisect
class RangeModule:

    def __init__(self):
        self.interval = []

    def addRange(self, left: int, right: int) -> None:
        # * Time Complexity   : O(NLogN)
        #                       Where N is len(self.interval)
        # * Space Complexity  : O(N)
        """
            * AS THE SELF.INTERVALS MAINTAINSED IS IN SORTED ORDER 
                * 1. WE CAN USE BINARY SEARCH TO INSERT NEW INTERVAL (BISECT.INSORT())
                * 2. POST INSERTION TAKE CARE OF OVERLAPS.
        """
        bisect.insort(self.interval, [left, right])

        # Taking care of overlaps in self.intervals
        res = [self.interval[0]]
        for start, end in self.interval:
            if res[-1][1] >= start:
                # Overlap found
                # eg. 1
                #   * res = [1, 10]  | start,end = [2, 3]
                #   * max(10, 3) -> 10
                # eg. 2
                #   * res = [1, 10]  | start,end = [2, 20]
                #   * max(10, 20) -> 20
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append((start, end))

        self.interval = res
        print(self.interval)

    def queryRange(self, left: int, right: int) -> bool:
        # * Time Complexity   : O(LogN)
        #                       Where N is len(self.interval)
        # this is an bisect_right operation
        # where_in it returns the right_most idx of left value.
        bs_right_idx = bisect.bisect(self.interval, [left, float("inf")])

        if bs_right_idx == 0 or not self.interval:
            return False

        # bisect gives + 1 idx to composate it -1
        # checking if the given right is in the bisect_right value if so returning true
        return self.interval[bs_right_idx - 1][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        # * Time Complexity   : O(N)
        #                       Where N is len(self.interval)
        res = []
        for start, end in self.interval:
            if right <= start or left >= end:
                # No overlap so good to append the cur_interval to res
                # Eg.
                #   start, end  = [10, 20]   |  left, right = [30, 40] --> for condition `left >= end`
                #   start, end  = [50, 60]   |  left, right = [30, 40] --> for condition `right <= start`
                res.append([start, end])
            else:
                # there is an overlap between the cur_interval
                # and the interval to be removed
                if start < left:
                    res.append([start, left])
                if right < end:
                    res.append([right, end])
        self.interval = res


rangeModule: RangeModule = RangeModule()    # --> None
rangeModule.addRange(10, 20)                # --> None
rangeModule.removeRange(14, 16)             # --> None
rangeModule.queryRange(10, 14)              # --> True
rangeModule.queryRange(13, 15)              # --> False
rangeModule.queryRange(16, 17)              # --> True
