"""
    * Time Complexity   : O(V + E)
    * Space Complexity  : O(V + E)
    * Date              : 9, June 2024
"""

"""
* Example 1:
    Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    Output: false
    Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
* Example 2:
    Input: graph = [[1,3],[0,2],[1,3],[0,2]]
    Output: true
    Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
"""


def isBipartite(graph: list[list[int]]) -> bool:
    """
        What is Bipartite graph?
            - cur_node's, neighbour must node be in the same group
                - [-1, 1, -1, 1] for this question.
    """
    len_graph = len(graph)

    # The maintaining a set of partition even and odd
    parity_set = [0 for _ in range(len_graph)]  # even = -1 | odd = 1

    def dfs(node, node_set):
        if parity_set[node] != 0:
            return parity_set[node] == node_set
        parity_set[node] = node_set
        for neigh in graph[node]:
            if not dfs(neigh, -1 * node_set):
                return False
        return True

    for node in range(len_graph):
        if parity_set[node] == 0 and not dfs(node, -1):
            return False
    print(parity_set)
    return True


print(isBipartite(graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(isBipartite(graph=[[1, 3], [0, 2], [1, 3], [0, 2]]))
