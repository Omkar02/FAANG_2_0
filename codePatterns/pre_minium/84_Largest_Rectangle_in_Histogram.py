"""
    * Time Complexity   : O(N)
    * Space Complexity  : O(N)
    * Date              : 4, June 2024
"""


def largestRectangleArea(heights: list[int]) -> int:
    max_area = 0
    stack = []  # (pre_idx, pre_height)

    n = len(heights)
    for cur_idx, cur_height in enumerate(heights):
        start = cur_idx

        # * If next val in decreasing
        while stack and stack[-1][1] > cur_height:
            pre_idx, pre_height = stack.pop()
            max_area = max(max_area, pre_height * (cur_idx - pre_idx))
            start = pre_idx

        stack.append((start, cur_height))

    for pre_idx, pre_height in stack:
        max_area = max(max_area, pre_height * (n - pre_idx))

    return max_area


print(largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]))
print(largestRectangleArea(heights=[2, 4]))
