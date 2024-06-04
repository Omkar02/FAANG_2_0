"""
    * Time Complexity   : O(N)
    * Space Complexity  : O(N)
    * Date              : 3, June 2024
"""
"""
* Example 1:
    Input
        ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
        [[], [[3, 10]], [[11, 2]], [[3, 2]], [
            [11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
    Output
        [null, null, null, null, 1, 0, null, 2]

    Explanation
        DetectSquares detectSquares = new DetectSquares();
        detectSquares.add([3, 10]);
        detectSquares.add([11, 2]);
        detectSquares.add([3, 2]);
        detectSquares.count([11, 10]);  - return 1. You can choose:
                                        - The first, second, and third points

        detectSquares.count([14, 8]);   - return 0. The query point cannot form a square with any points in the data structure.
        detectSquares.add([11, 2]);     - Adding duplicate points is allowed.

        detectSquares.count([11, 10]);  - return 2. You can choose:
                                        - The first, second, and third points
                                        - The first, third, and fourth points
"""


class DetectSquares:
    def __init__(self) -> None:
        # Maintaining the points count i.e if there are diplicates
        self.points = {}

    def add(self, point: list[int]) -> None:
        # * TIME COMPLEXITY: O(1)
        point = tuple(point)
        if point not in self.points:
            self.points[point] = 0
        self.points[point] += 1

    def count(self, point: list[int]) -> int:
        # * TIME COMPLEXITY: O(N)
        square_count = 0
        x_one, y_one = point

        for (x_two, y_two), cnt in self.points.items():
            dist_x, dist_y = abs(x_one - x_two), abs(y_one - y_two)

            if dist_x == dist_y and dist_x > 0:
                # * Length wise they stasified the square criteria
                # * Now checck if the conrner exists in the self.points
                corner_one = (x_one, y_two)
                corner_two = (x_two, y_one)

                if corner_one in self.points and corner_two in self.points:
                    square_count = cnt * \
                        self.points[corner_one] * self.points[corner_two]
        return square_count


detectSquares: DetectSquares = DetectSquares()
assert detectSquares.add([3, 10]) == None
assert detectSquares.add([11, 2]) == None
assert detectSquares.add([3, 2]) == None
assert detectSquares.count([11, 10]) == 1

assert detectSquares.count([14, 8]) == 0
assert detectSquares.add([11, 2]) == None

assert detectSquares.count([11, 10]) == 2
