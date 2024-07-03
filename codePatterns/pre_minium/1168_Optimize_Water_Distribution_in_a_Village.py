"""
    * Time Complexity   : O(N)
    * Space Complexity  : O(N)
    * Date              : 10, June 2024
"""
"""
* Example 1:
    Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
    Output: 3
    Explanation: The image shows the costs of connecting houses using pipes.
        The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.

* Example 2:
    Input: n = 2, wells = [1,1], pipes = [[1,2,1],[1,2,2]]
    Output: 2
    Explanation: We can supply water with cost two using one of the three options:
        Option 1:
        - Build a well inside house 1 with cost 1.
        - Build a well inside house 2 with cost 1.
        The total cost will be 2.
        Option 2:
        - Build a well inside house 1 with cost 1.
        - Connect house 2 with house 1 with cost 1.
        The total cost will be 2.
        Option 3:
        - Build a well inside house 2 with cost 1.
        - Connect house 1 with house 2 with cost 1.
        The total cost will be 2.
        Note that we can connect houses 1 and 2 with cost 1 or with cost 2 but we will always choose the cheapest option. 
"""


class UnionFind:
    def __init__(self):
        self.connections = {}

    def union(self, parent: int, child: int) -> None:
        _parent = self.find(parent)
        _child = self.find(child)

        if _parent != _child:
            self.connections[_child] = _parent
            return True
        return False

    def find(self, child: int) -> int:
        parent = self.connections.get(child, child)
        if parent != child:
            parent = self.find(parent)
            self.connections[child] = parent

        return parent


def minCostToSupplyWater(n: int, wells: list[int], pipes: list[list[int]]) -> int:
    """
        * Implementing the kruskals min-spanning-tree.
    """
    uf = UnionFind()
    # * Step 1: Add virtual node 0, connect all nodes to the virtual one, and set costs from wells
    for i, cost in enumerate(wells):
        pipes.append([0, i + 1, cost])

    # Sorting the pipes for creating a min-spanning tree
    pipes.sort(key=lambda x: x[2])
    res = 0
    for src, dst, cost in pipes:
        if uf.union(src, dst):
            res += cost
    return res


print(minCostToSupplyWater(n=3, wells=[1, 2, 2], pipes=[[1, 2, 1], [2, 3, 1]]))
print(minCostToSupplyWater(n=2, wells=[1, 1], pipes=[[1, 2, 1], [1, 2, 2]]))
