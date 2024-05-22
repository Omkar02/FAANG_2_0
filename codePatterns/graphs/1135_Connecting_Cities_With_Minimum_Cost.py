"""
* TYPE             : Graph
* ALGORITHM        : Kruskal's Algorithm To find Min Spanning Tree -> Union Find


* Example 1:
    Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
    Output: 6
    Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.
* Example 2:
    Input: n = 4, connections = [[1,2,3],[3,4,4]]
    Output: -1
    Explanation: There is no way to connect all cities even if all edges are used.
"""


class UnionFind:
    def __init__(self) -> None:
        self._relations = {}

    def union(self, parent: int, child: int):
        _parent_node = self.find(parent)
        _child_node = self.find(child)
        self._relations[_child_node] = _parent_node

    def find(self, child: int) -> int:
        parent = self._relations.get(child, child)
        if parent != child:
            parent = self.find(parent)
            self._relations[child] = parent
        return parent


def minimumCost(n: int, connections: list[list[int]]) -> int:
    UF = UnionFind()
    total_cost = 0
    connections.sort(key=lambda x: x[2])
    for src, dst, cost in connections:
        if UF.find(src) != UF.find(dst):
            UF.union(src, dst)
            total_cost += cost
    # * CHECK IF ALL VERTEX ARE CONNECTED AND ARE PART OF ONE SINGLE GRAPH
    root = UF.find(1)
    for city in range(2, n + 1):
        if UF.find(city) != root:
            return -1
    return total_cost


print(minimumCost(n=3, connections=[[1, 2, 5], [1, 3, 6], [2, 3, 1]]))
print(minimumCost(n=4, connections=[[1, 2, 3], [3, 4, 4]]))
