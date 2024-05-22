"""
* TYPE             : Graph
* ALGORITHM        : Dijkstra's Algo

* Example 1:
    Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Output: 2
* Example 2:
    Input: times = [[1,2,1]], n = 2, k = 1
    Output: 1
* Example 3:
    Input: times = [[1,2,1]], n = 2, k = 2
    Output: -1
"""

import heapq


def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    graph = {}
    for src, dst, weight in times:
        if src not in graph:
            graph[src] = []
        graph[src].append((dst, weight))

    min_heap = [(0, k)]  # (delay, start_node)
    delays = {}

    while min_heap:
        cur_delay, cur_node = heapq.heappop(min_heap)
        if cur_node in delays:
            continue

        delays[cur_node] = cur_delay
        if cur_node in graph:
            for neigh, neigh_delay in graph[cur_node]:
                total_delay = neigh_delay + cur_delay
                if neigh not in delays:
                    heapq.heappush(min_heap, (total_delay, neigh))
    return max(delays.values()) if len(delays) == n else -1


print(networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
print(networkDelayTime(times=[[1, 2, 1]], n=2, k=1))
print(networkDelayTime(times=[[1, 2, 1]], n=2, k=2))
