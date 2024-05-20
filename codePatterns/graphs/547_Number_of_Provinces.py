"""
* TYPE             : Graph
* ALGORITHM        : Union Find

* Example 1:
    Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2
* Example 2:
    Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3
"""


class UnionFind:
    def __init__(self):
        self._relations = {}

    def union(self, parent: int, child: int) -> None:
        _parent_node = self.find(parent)
        _child_node = self.find(child)

        self._relations[_child_node] = _parent_node

    def find(self, child: int) -> int:
        # * IF NO PARENT TO A CHILD CHILD IS THE PARENT
        parent = self._relations.get(child, child)
        if child != parent:
            parent = self.find(parent)
            self._relations[child] = parent
        return parent


def findCircleNum(isConnected: list[list[int]]) -> int:
    graph = {}
    for city_idx, adj_matrix in enumerate(isConnected):
        for neigh_idx, connected in enumerate(adj_matrix):
            if connected == 1 and city_idx != neigh_idx:
                if city_idx not in graph:
                    graph[city_idx] = []
                graph[city_idx].append(neigh_idx)

    total_cities = len(isConnected)
    UF = UnionFind()

    for city in range(total_cities):
        if city in graph:
            for neigh in graph[city]:
                UF.union(city, neigh)

    return len(set([UF.find(x) for x in range(total_cities)]))


print(findCircleNum(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(findCircleNum(isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
