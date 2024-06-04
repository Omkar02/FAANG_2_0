"""
    * Time Complexity   : O(N)
    * Space Complexity  : O(N)
    * Date              : 3, June 2024
"""

"""
* Example 1:
    Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
    Output: 20190301
    Explanation: 
        The first event occurs at timestamp = 20190101, and after 0 and 1 become friends, we have the following friendship groups [0,1], [2], [3], [4], [5].
        The second event occurs at timestamp = 20190104, and after 3 and 4 become friends, we have the following friendship groups [0,1], [2], [3,4], [5].
        The third event occurs at timestamp = 20190107, and after 2 and 3 become friends, we have the following friendship groups [0,1], [2,3,4], [5].
        The fourth event occurs at timestamp = 20190211, and after 1 and 5 become friends, we have the following friendship groups [0,1,5], [2,3,4].
        The fifth event occurs at timestamp = 20190224, and as 2 and 4 are already friends, nothing happens.
        The sixth event occurs at timestamp = 20190301, and after 0 and 3 become friends, we all become friends.
* Example 2:
    Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
    Output: 3
    Explanation: At timestamp = 3, all the persons (i.e., 0, 1, 2, and 3) become friends.
"""


class UnionFind:
    def __init__(self):
        self.groups = {}
        self.connected_node = 0

    def union(self, child: int, parent: int) -> None:
        _child = self.find(child)
        _parent = self.find(parent)
        if _child != _parent:
            self.groups[_child] = _parent
            self.connected_node += 1

    def find(self, child: int) -> int:
        parent = self.groups.get(child, child)
        if parent != child:
            parent = self.find(parent)
            self.groups[child] = parent
        return parent


def earliestAcq(logs: list[list[int]], n: int) -> int:
    """
        * THE intution here is to sort in asc order all the timestamps
        * And check if whats the minimum timestam that joinst all the 
        * nodes.
    """
    logs.sort(key=lambda x: x[0])
    uf = UnionFind()

    for timestamp, src, dst in logs:
        uf.union(src, dst)
        if uf.connected_node == n - 1:
            return timestamp
    return -1


print(earliestAcq(logs=[[20190101, 0, 1],
                        [20190104, 3, 4],
                        [20190107, 2, 3],
                        [20190211, 1, 5],
                        [20190224, 2, 4],
                        [20190301, 0, 3],
                        [20190312, 1, 2],
                        [20190322, 4, 5]], n=6))

print(earliestAcq(logs=[[0, 2, 0],
                        [1, 0, 1],
                        [3, 0, 3],
                        [4, 1, 2],
                        [7, 3, 1]], n=4))
