"""
* TYPE             : Graph
* ALGORITHM        : Minimum Spanning Tree problems


* Example 1:
    Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    Output: 20
    Explanation: We can connect the points as shown above to get the minimum cost of 20.
        Notice that there is a unique path between every pair of points.
* Example 2:
    Input: points = [[3,12],[-2,5],[-4,1]]
    Output: 18
"""
import heapq


def minCostConnectPoints(points: list[list[int]]) -> int:
    """
    THIS IS A GREADY APPROCH WHERE IN WE TAKE THE NEXT LOWEST COST PATH
    """
    def getManhattanDist(x, y): return abs(x[0] - y[0]) + abs(x[1] - y[1])
    len_points = len(points)
    heap = [(0, 0)]

    # * MANTAINING THE COST IS AN OPTIMIZATION, WHEREN IN ONLY TO
    # * PUSH POINT IN THE HEAP IF IT'S COST IS LESS THAN PREVIOS
    # * CALCULATED....
    dist_from_origin = [float("inf") for _ in range(len_points)]

    total_cost = 0
    visited = set()
    while heap:
        cost, point = heapq.heappop(heap)
        if point in visited:
            continue
        visited.add(point)
        total_cost += cost
        for nxt_point in range(len_points):
            if nxt_point in visited:
                continue

            new_cost = getManhattanDist(points[point],
                                        points[nxt_point])

            # * OPTIMIZATION AS SAID ABOVE
            if new_cost < dist_from_origin[nxt_point]:
                dist_from_origin[nxt_point] = new_cost
                heapq.heappush(heap, (new_cost, nxt_point))

    return total_cost


print(minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
print(minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]))
