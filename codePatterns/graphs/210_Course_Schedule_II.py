"""
* TYPE             : Graph
* ALGORITHM        : Topological Sort [DFS] && Topological Sort [BFS]


* Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: [0,1]
    Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
* Example 2:
    Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3]
    Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
        ! So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
* Example 3:
    Input: numCourses = 1, prerequisites = []
    Output: [0]
"""


from collections import defaultdict


def findOrderDFS(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = {}
    for src, dst in prerequisites:
        if src not in graph:
            graph[src] = []
        graph[src].append(dst)

    def _DFS(node: int) -> bool:
        if node in visiting:
            # * IT'S USED TO DETECT A CYCLE.
            return False
        if node in visited:
            # * THE NODE IS ALREADY COMPUTED.
            return True

        visiting.add(node)
        if node in graph:
            for neigh in graph[node]:
                if not _DFS(neigh):
                    return False

        visiting.remove(node)
        visited.add(node)

        # * APPENDING THE NODE IF ALL ABOVE IS TRUE
        constructed_seq.append(node)
        return True

    constructed_seq = []
    visited = set()
    visiting = set()
    for node in range(numCourses):
        if not _DFS(node):
            return []
    return constructed_seq


print("-" * 20, " DFS ", "-" * 20)
print(findOrderDFS(numCourses=2, prerequisites=[[1, 0]]))

print(findOrderDFS(numCourses=4,
                   prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))

print(findOrderDFS(numCourses=1, prerequisites=[]))

# ----------------------------------------------------------------------------------------


def findOrderBFS(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = {}
    # * DEPEDENDANT_COUNT IS USED TO KEEP A TRACK OF NO. OF DEPENDENCIES
    depedendant_count = {}
    for src, dst in prerequisites:
        if src not in graph:
            graph[src] = []
        if dst not in depedendant_count:
            depedendant_count[dst] = 0

        graph[src].append(dst)
        depedendant_count[dst] += 1

    # * SELECTING THE NODE WHICH HAD 0 DEPENDENCIES
    q = [x for x in range(numCourses) if depedendant_count.get(x, 0) == 0]

    constructed_seq = []
    while q:
        # * pop(0) AS THIS IS AN BFS SOLUTION
        cur_node = q.pop(0)
        constructed_seq.append(cur_node)

        if cur_node in graph:
            for neigh in graph[cur_node]:
                depedendant_count[neigh] -= 1
                if depedendant_count[neigh] == 0:
                    q.append(neigh)

    if len(constructed_seq) == numCourses:
        return constructed_seq[::-1]
    else:
        return []


print("-" * 20, " BFS ", "-" * 20)
print(findOrderBFS(numCourses=2, prerequisites=[[1, 0]]))

print(findOrderBFS(numCourses=4,
                   prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))

print(findOrderBFS(numCourses=1, prerequisites=[]))
