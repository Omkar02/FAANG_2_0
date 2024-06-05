"""
    * Time Complexity   : O(N^3)
    * Space Complexity  : O(N)
    * Date              : 4, June 2024
"""
"""
* Example 1:
    Input: points = [[1,2],[2,1],[1,0],[0,1]]
    Output: 2.00000
    Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
* Example 2:
    Input: points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
    Output: 1.00000
    Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
* Example 3:
    Input: points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
    Output: 0
    Explanation: There is no possible rectangle to form from these points.
"""


def minAreaFreeRect(points: list[list[int]]) -> float:
    def edulineDist(x1, x2, y1, y2): return (x2 - x1)**2 + (y2 - y1)**2
    def powSqRoot(x1, x2, y1, y2): return edulineDist(x1, y1, x2, y2)**0.5

    lookup = {(x, y) for x, y in points}
    n = len(points)
    res = float("inf")
    for p1 in range(n):
        for p2 in range(p1 + 1, n):
            for p3 in range(p2 + 1, n):
                x1, y1 = points[p1]
                x2, y2 = points[p2]
                x3, y3 = points[p3]

                # * Now using the 3 points we need to find the x4 point
                x4, y4 = (x3 + (x2 - x1)), (y3 + (y2 - y1))

                if (x4, y4) in lookup:
                    # * Now check if all 4 point together form a rectangle
                    if edulineDist(x1, x2, y1, y3) == edulineDist(x2, x4, y2, y4):
                        # * If both the diagnols are equal
                        area = powSqRoot(x1, x2, y1, y2) * \
                            powSqRoot(x3, x4, y3, y4)
                        res = min(res, area)
    return res if res != float("inf") else 0.0


print(minAreaFreeRect(points=[[1, 2], [2, 1], [1, 0], [0, 1]]))
print(minAreaFreeRect(points=[[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]]))
print(minAreaFreeRect(points=[[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]]))
