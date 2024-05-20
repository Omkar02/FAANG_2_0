"""
? LINK = https://www.youtube.com/watch?v=4oXYucLRIzo&ab_channel=KacyCodes
* TYPE             : Graph
* ALGORITHM        : Tarjans Algo + DFS

* Example 1:
    Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
    Output: [[1,3]]
    Explanation: [[3,1]] is also accepted.
* Example 2:
    Input: n = 2, connections = [[0,1]]
    Output: [[0,1]]
"""


def criticalConnections(n: int, connections: list[list[int]]) -> list[list[int]]:
    graph = {}

    # * SINCE IT'S AN BI-DIRECTIONAL GRAPH
    for u, v in connections:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    def _DFS(cur_node: int, pre_node: int, cur_depth: int) -> int:
        visited.add(cur_node)
        lowest_depth[cur_node] = cur_depth

        for neigh in graph[cur_node]:
            if pre_node == neigh:
                continue
            if neigh not in visited:
                _DFS(neigh, cur_node, cur_depth + 1)

            # * THIS IS PROPOGATING THE LOWEST VALUE
            #   * IF THERE EXITS A CYCLIC / REDUDANT CONNECTION WHOLE CONNECTED GRAPH WILL HAVE SAME DEPTH
            lowest_depth[cur_node] = min(lowest_depth[cur_node],
                                         lowest_depth[neigh])

            # * IF DEPTH OF NEIGH >= CUR_DEPTH + 1
            #   * MEANS WE WON'T BE ABLE TO GET TO THE NEIGH ANY OTHER WAY; WITHOUT THIS CON / BRIDGE
            if lowest_depth[neigh] >= cur_depth + 1:
                critical_connections.append([cur_node, neigh])

    # print(graph)
    lowest_depth = [idx for idx in range(n)]
    critical_connections = []
    visited = set()

    _DFS(cur_node=0, pre_node=-1, cur_depth=0)
    return critical_connections


print(criticalConnections(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]]))
print(criticalConnections(n=2, connections=[[0, 1]]))
print(criticalConnections(n=6, connections=[
      [0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]))
