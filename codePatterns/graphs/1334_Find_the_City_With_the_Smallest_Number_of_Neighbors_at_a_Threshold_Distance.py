"""
* TYPE             : Graph
* ALGORITHM        : Dijkstra's Algorithm

* Example 1:
    Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
    Output: 3
    Explanation: The figure above describes the graph. 
        The neighboring cities at a distanceThreshold = 4 for each city are:
        City 0 -> [City 1, City 2] 
        City 1 -> [City 0, City 2, City 3] 
        City 2 -> [City 0, City 1, City 3] 
        City 3 -> [City 1, City 2] 
        Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
* Example 2:
    Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
    Output: 0
    Explanation: The figure above describes the graph. 
        The neighboring cities at a distanceThreshold = 2 for each city are:
        City 0 -> [City 1] 
        City 1 -> [City 0, City 4] 
        City 2 -> [City 3, City 4] 
        City 3 -> [City 2, City 4]
        City 4 -> [City 1, City 2, City 3] 
        The city 0 has 1 neighboring city at a distanceThreshold = 2.
"""
import heapq


def findTheCity(n: int, edges: list[list[int]], distanceThreshold: int) -> int:
    graph = {}
    for edge1, edge2, weight in edges:
        if edge1 not in graph:
            graph[edge1] = []
        if edge2 not in graph:
            graph[edge2] = []

        graph[edge1].append((edge2, weight))
        graph[edge2].append((edge1, weight))

    def _BFSDijkstra(city: int) -> int:
        visited = set()
        min_heap = [(0, city)]  # (weight, city)
        while min_heap:
            cur_weight, cur_city = heapq.heappop(min_heap)
            if cur_city not in visited:
                visited.add(cur_city)
                if cur_city not in graph:
                    continue
                for neigh, neigh_weight in graph[cur_city]:
                    total_cost = cur_weight + neigh_weight
                    if total_cost <= distanceThreshold and neigh not in visited:
                        heapq.heappush(min_heap, (total_cost, neigh))
        return len(visited) - 1

    res_city = -1
    min_reachable = float("inf")

    for city in range(n):
        reachable = _BFSDijkstra(city)
        if reachable <= min_reachable:
            min_reachable = reachable
            res_city = city
    return res_city


print(findTheCity(n=4,
                  edges=[[0, 1, 3],
                         [1, 2, 1],
                         [1, 3, 4],
                         [2, 3, 1]],
                  distanceThreshold=4))

print(findTheCity(n=5,
                  edges=[[0, 1, 2],
                         [0, 4, 8],
                         [1, 2, 3],
                         [1, 4, 2],
                         [2, 3, 1],
                         [3, 4, 1]],
                  distanceThreshold=2))
