"""
    * Time Complexity   : O(N)
    * Space Complexity  : O(N)
    * Date              : 4, June 2024
"""

"""
* Example 1:
    Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    Output: 6
    Explanation: The maximal rectangle is shown in the above picture.
* Example 2:
    Input: matrix = [["0"]]
    Output: 0
* Example 3:
    Input: matrix = [["1"]]
    Output: 1
"""


def largestRectangleArea(heights: list[int]) -> int:
    max_area = 0
    stack = []  # (pre_idx, pre_height)
    n = len(heights)

    for cur_idx, cur_height in enumerate(heights):
        start = cur_idx
        # * Check inf next height is decreasing.
        # * As we cannot extent the same height to right anymore
        while stack and stack[-1][1] > cur_height:
            pre_idx, pre_height = stack.pop()
            max_area = max(max_area, pre_height * (cur_idx - pre_idx))
            # * Pulling back the (start) val as we can extend the cur_height to left
            # * direction in order to compute the area
            start = pre_idx

        stack.append((start, cur_height))

    # * We have traversed the entire heights array
    # * But there will be pairs left in stack which area is not computed
    for pre_idx, pre_height in stack:
        # * The wigth is (n - pre_idx) as we are at the last index
        max_area = max(max_area, pre_height * (n - pre_idx))

    return max_area


def maximalRectangle(matrix: list[list[str]]) -> int:
    """
        Intutions: To convert the matrix as a barchart and apply leetcode 84 solution
                   that find largest rectangle in a graph.
    """
    bar_chart = []
    row_range = range(len(matrix))
    col_range = range(len(matrix[0]))

    for row in row_range:
        if row == 0:
            # Converting the str's to int
            bar_chart.append(list(map(int, matrix[row])))
        else:
            for col in col_range:
                if matrix[row][col] == "1":
                    matrix[row][col] = int(
                        matrix[row][col]) + int(matrix[row - 1][col])
                else:
                    matrix[row][col] = int(matrix[row][col])

            bar_chart.append(matrix[row])

    # [print(x) for x in bar_chart]
    # * [1, 0, 1, 0, 0]
    # * [2, 0, 2, 1, 1]
    # * [3, 1, 3, 2, 2]
    # * [4, 0, 0, 3, 0]

    max_rectangel = 0
    for heights in bar_chart:
        max_rectangel = max(max_rectangel, largestRectangleArea(heights))
    return max_rectangel


print(maximalRectangle(matrix=[["1", "0", "1", "0", "0"],
                               ["1", "0", "1", "1", "1"],
                               ["1", "1", "1", "1", "1"],
                               ["1", "0", "0", "1", "0"]]))

print(maximalRectangle(matrix=[["0"]]))

print(maximalRectangle(matrix=[["1"]]))
