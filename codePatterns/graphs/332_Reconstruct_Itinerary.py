"""
* TYPE             : Graph
* ALGORITHM        : DFS 

* TIME-COMPLEXITY  : O(M x N)
* SPACE-COMPLEXITY : O(M x N)

* Example 1:
    Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    Output: ["JFK","MUC","LHR","SFO","SJC"]
* Example 2:
    Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    Explanation: Another possible reconstruction is 
        ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

* Example 3:
    Input: tickets=[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    Output: ["JFK","NRT","JFK","KUL"]
"""


def findItinerary(tickets: list[list[str]]) -> list[str]:
    relation_graph = {}

    # * ---- CONSTRUCTING THE RELATIONSHIP GRAPH & SORTING IT LEXILOGICALLY ----
    for src, dest in sorted(tickets, reverse=True):
        if src not in relation_graph:
            relation_graph[src] = []
        relation_graph[src].append(dest)
    # * ------------------------------------------------------------------------

    def _DFS(node):
        """
        * We enter a loop that continues until we find an airport that has no more destinations left to visit. 

        * This is done by checking the adjacency list for each airport and popping the last element (which is the smallest in lexical order).
        """

        if node in relation_graph:
            while relation_graph[node]:
                next_node = relation_graph[node].pop()
                _DFS(next_node)

        # * ONLY ADD TO ITENARY IF NO NODES ARE LEFT
        itenary.append(node)

    itenary = []

    _DFS(node="JFK")
    return itenary[::-1]


print(findItinerary(tickets=[["MUC", "LHR"],
                             ["JFK", "MUC"],
                             ["SFO", "SJC"],
                             ["LHR", "SFO"]]))

print(findItinerary(tickets=[["JFK", "SFO"],
                             ["JFK", "ATL"],
                             ["SFO", "ATL"],
                             ["ATL", "JFK"],
                             ["ATL", "SFO"]]))

print(findItinerary(tickets=[["JFK", "KUL"],
                             ["JFK", "NRT"],
                             ["NRT", "JFK"]]))
