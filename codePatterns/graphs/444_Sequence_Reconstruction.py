"""
* TYPE             : Graph
* ALGORITHM        : Topological Sort [DFS]

! THIS IS SIMILAR TO 210.COURSE_SCHEDULE 2

* Example 1:
    Input: nums = [1,2,3], sequences = [[1,2],[1,3]]
    Output: false
    Explanation: There are two possible supersequences: [1,2,3] and [1,3,2].
        The sequence [1,2] is a subsequence of both: [1,2,3] and [1,3,2].
        The sequence [1,3] is a subsequence of both: [1,2,3] and [1,3,2].
        Since nums is not the only shortest supersequence, we return false.
* Example 2:
    Input: nums = [1,2,3], sequences = [[1,2]]
    Output: false
    Explanation: The shortest possible supersequence is [1,2].
        The sequence [1,2] is a subsequence of it: [1,2].
        Since nums is not the shortest supersequence, we return false.
* Example 3:
    Input: nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]
    Output: true
    Explanation: The shortest possible supersequence is [1,2,3].
        The sequence [1,2] is a subsequence of it: [1,2,3].
        The sequence [1,3] is a subsequence of it: [1,2,3].
        The sequence [2,3] is a subsequence of it: [1,2,3].
        Since nums is the only shortest supersequence, we return true.
* Example 4:
    Input: org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
    Output: true
"""


def sequenceReconstruction(nums: list[int], sequences: list[list[int]]) -> bool:
    # * CONSTRUCTING THE GRAPH
    graph = {}
    for seq in sequences:
        for idx in range(len(seq) - 1):
            # * AS THE SEQ MAY CONTAIN MORE THAN 2 VALUES SO WE CHAIN THEM
            #   * SRC = IDX , DST = IDX + 1 | IDX IN RANGE(LEN(SEQ) - 1)
            node = seq[idx]
            if node not in graph:
                graph[node] = set()
            graph[node].add(seq[idx + 1])

    # ? FOR Eg.4 graph = {5: {2}, 2: {6}, 6: {3}, 4: {1}, 1: {5}}
    # print(graph)

    # * INIT THE VISITING AND VISITED
    visiting = set()
    visited = set()
    # * COMPUTE THE SEQUENCE
    computed_seq = []

    def _DFS(node: int) -> bool:
        if node in visiting:
            return False
        if node in visited:
            return True

        visiting.add(node)
        if node in graph:
            for neigh in graph[node]:
                if not _DFS(neigh):
                    return False

        visiting.remove(node)
        visited.add(node)

        computed_seq.append(node)
        return True

    for node in range(1, len(nums) + 1):
        if not _DFS(node):
            return False

    return nums == computed_seq[::-1]


print(sequenceReconstruction(nums=[1, 2, 3], sequences=[[1, 2], [1, 3]]))
print(sequenceReconstruction(nums=[1, 2, 3], sequences=[[1, 2]]))
print(sequenceReconstruction(nums=[1, 2, 3],
      sequences=[[1, 2], [1, 3], [2, 3]]))
print(sequenceReconstruction(nums=[4, 1, 5, 2, 6, 3],
                             sequences=[[5, 2, 6, 3], [4, 1, 5, 2]]))
