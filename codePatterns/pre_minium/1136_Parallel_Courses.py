"""
    * Time Complexity   : O(N)
    * Space Complexity  : O(N)
    * Date              : 8, June 2024
"""
from collections import defaultdict
"""
* Example 1:
    Input: n = 3, relations = [[1,3],[2,3]]
    Output: 2
    Explanation: The figure above represents the given graph.
        In the first semester, you can take courses 1 and 2.
        In the second semester, you can take course 3.
* Example 2:
    Input: n = 3, relations = [[1,2],[2,3],[3,1]]
    Output: -1
    Explanation: No course can be studied because they are prerequisites of each other.
"""


def minimumSemesters(n: int, relations: list[list[int]]) -> int:
    # * Step 1: creat a relations graph
    graphs = defaultdict(list)
    for pre_course, next_course in relations:
        graphs[pre_course].append(next_course)

    print(f'Graph = {graphs}')

    # * Step 3: Use topological sort to compute the depth and find a loop
    def topological_sort_dfs(node: int) -> int:
        if node in node_depth:
            return node_depth[node]
        node_depth[node] = -1  # mark it as visiting

        max_depth = 0
        for next_course in graphs[node]:
            cur_depth = topological_sort_dfs(next_course)
            if cur_depth == -1:
                # ! found a loop
                return -1
            max_depth = max(max_depth, cur_depth)

        node_depth[node] = 1 + max_depth
        return node_depth[node]

    # * Step 2: Traverse through all the courses
    node_depth = {}  # used to track 2 things visiting and max node - depth
    for course in range(1, n + 1):
        depth = topological_sort_dfs(course)
        if depth == -1:
            return -1

    print(node_depth)
    return max(node_depth.values())


print(minimumSemesters(n=3, relations=[[1, 3], [2, 3]]))
print(minimumSemesters(n=3, relations=[[1, 2], [2, 3], [3, 1]]))

