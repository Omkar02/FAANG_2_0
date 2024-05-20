"""
? LINK = https://leetcode.ca/2019-04-28-1245-Tree-Diameter/
* TYPE             : Graph
* ALGORITHM        : 2 DFS

* TIME-COMPLEXITY  : O(N x M)
* SPACE-COMPLEXITY : O(N x M)

* Example 1:
    Input: edges = [[0,1],[0,2]]
    Output: 2
    Explanation: The longest path of the tree is the path 1 - 0 - 2.
* Example 2:
    Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
    Output: 4
    Explanation: The longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
"""


def treeDiameter(edges: list[list[int]]) -> int:
    """
        * THIS IS A TWO DFS SOLUTION WHERE IN
            * 1ST FINDING THE FARTEST NODE FROM ARBIRATART NDOE 
            * 2ND FROM THE FARTEST NODE AGAIN DO A DFS 
    """
    relations = {}
    for src, dst in edges:
        if src not in relations:
            relations[src] = set()
        if dst not in relations:
            relations[dst] = set()
        relations[src].add(dst)
        relations[dst].add(src)

    # print(relations)

    def _DFS(node: int) -> int:
        visited.add(node)
        farthest_node, max_distance = node, 0
        for neigh in relations[node]:
            if neigh not in visited:
                next_node, distance = _DFS(neigh)
                if distance + 1 > max_distance:
                    farthest_node, max_distance = next_node, distance + 1
        visited.remove(node)

        return farthest_node, max_distance

    visited = set()

    # * Step 1: Find the farthest node from an arbitrary starting node (node 0)
    start_node = 0
    farthest_node_from_start, _ = _DFS(start_node)

    # * Step 2: Find the farthest node from the farthest node found in step 1
    _, diameter = _DFS(farthest_node_from_start)

    return diameter


print(treeDiameter(edges=[[0, 1], [0, 2]]))
print(treeDiameter(edges=[[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]))
