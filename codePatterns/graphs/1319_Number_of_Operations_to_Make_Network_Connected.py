"""
* TYPE             : Graph
* ALGORITHM        : Union Find

* Example 1:
    Input: n = 4, connections = [[0,1],[0,2],[1,2]]
    Output: 1
    Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
* Example 2:
    Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
    Output: 2
* Example 3:
    Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
    Output: -1
    Explanation: There are not enough cables.
"""


class UnionFind:
    def __init__(self, n):
        self._relations = {}
        self.count = n

    def union(self, parent: int, child: int) -> None:
        _parent_node = self.find(parent)
        _child_node = self.find(child)
        if _parent_node != _child_node:
            # * THIS IS TO IGNORE THE REDUDANT CONNECTIONS / SAME
            # print(_parent_node, _child_node)
            self._relations[_child_node] = _parent_node
            self.count -= 1

    def find(self, child: int) -> int:
        # * IF NO PARENT TO A CHILD CHILD IS THE PARENT
        parent = self._relations.get(child, child)
        if child != parent:
            parent = self.find(parent)
            self._relations[child] = parent
        return parent


def makeConnected(n: int, connections: list[list[int]]) -> int:
    if len(connections) < n - 1:
        # * THERE ARE NOT ENEOUGH CABLES.
        return -1

    UF = UnionFind(n)
    for src, dst in connections:
        UF.union(src, dst)
    return UF.count - 1


print(makeConnected(n=4, connections=[[0, 1], [0, 2], [1, 2]]))
print(makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))
print(makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2]]))
