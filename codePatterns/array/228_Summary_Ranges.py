"""
* Example 1:
    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: The ranges are:
        [0,2] --> "0->2"
        [4,5] --> "4->5"
        [7,7] --> "7"
* Example 2:
    Input: nums = [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: The ranges are:
        [0,0] --> "0"
        [2,4] --> "2->4"
        [6,6] --> "6"
        [8,9] --> "8->9"

"""


def summaryRanges(nums: list[int]) -> list[str]:
    if not nums:
        return []
    range_groups = []
    for n in nums:
        if not range_groups or range_groups[-1][-1] + 1 != n:

            range_groups.append([])
        range_groups[-1].append(n)

    return [f'{x[0]}->{x[-1]}' if len(x) > 1 else f"{x[0]}" for x in range_groups]


print(summaryRanges(nums=[0, 1, 2, 4, 5, 7]))
print(summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))
