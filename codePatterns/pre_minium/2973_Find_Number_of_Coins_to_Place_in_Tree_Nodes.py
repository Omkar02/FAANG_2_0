"""
    * Time Complexity   : O(NLogN)
    * Space Complexity  : O(N)
    * Date              : 7, June 2024
"""

"""
* Example 1:
    Input: edges = [[0,1],[0,2],[0,3],[0,4],[0,5]], cost = [1,2,3,4,5,6]
    Output: [120,1,1,1,1,1]
    Explanation: For node 0 place 6 * 5 * 4 = 120 coins. All other nodes are leaves with subtree of size 1, place 1 coin on each of them.
* Example 2:
    Input: edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]], cost = [1,4,2,3,5,7,8,-4,2]
    Output: [280,140,32,1,1,1,1,1,1]
    Explanation: The coins placed on each node are:
    - Place 8 * 7 * 5 = 280 coins on node 0.
    - Place 7 * 5 * 4 = 140 coins on node 1.
    - Place 8 * 2 * 2 = 32 coins on node 2.
    - All other nodes are leaves with subtree of size 1, place 1 coin on each of them.
* Example 3:
    Input: edges = [[0,1],[0,2]], cost = [1,2,-2]
    Output: [0,1,1]
    Explanation: Node 1 and 2 are leaves with subtree of size 1, place 1 coin on each of them. For node 0 the only possible product of cost is 2 * 1 * -2 = -4. Hence place 0 coins on node 0.
"""


def placedCoins(edges: list[list[int]], cost: list[int]) -> list[int]:
    # * DFS with POST ORDER computations
    # Step 1: Creating a graph
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

        if v not in graph:
            graph[v] = []
        graph[v].append(u)

    # Step 2: Doing a DFS on in and having the conin computed in the
    #         post order traversal.
    def DFS(node: int) -> list[int]:
        if cost[node] == 0:
            return

        coins = [cost[node]]
        cost[node] = 0  # Using to track visited node.

        if node in graph:
            for next_node in graph[node]:
                sub_tree_coins = DFS(next_node)
                if sub_tree_coins:
                    coins.extend(sub_tree_coins)

        print(f'Cur Node = {node} | Coins = {coins}')

        coins.sort()  # Sorting the coins to know the largest and smallest

        # * Now there are 2 desions can be made for coins
        if len(coins) >= 3:
            # * Desicion 1: if the length of coins array i.e sub-tree is >= 3
            # *             return an array of len 5 such that
            # *             [-2ve_num, -1ve_num, +3ve_num, +2ve_num, +1ve_num]
            n1, n2 = coins[:2]
            p3, p2, p1 = coins[-3:]
            # print(0, [n1, n2, p1], [p3, p2, p1])
            res[node] = max(0,
                            n1 * n2 * p1,  # as two smallest i.e -ve can make a huge coinProduct
                            p1 * p2 * p3)

        if len(coins) <= 5:
            # * Desicion 2: if the length of coins array i.e sub-tree is if <= 5
            return coins

        return [n1, n2, p3, p2, p1]

    # * Init with 1 so to take case of all node who's subtree is <3
    res = [1 for _ in range(len(cost))]
    DFS(0)
    return res


print("res = ", placedCoins(edges=[[0, 1],
                                   [0, 2],
                                   [0, 3],
                                   [0, 4],
                                   [0, 5]], cost=[1, 2, 3, 4, 5, 6]))
print()
print("res = ", placedCoins(edges=[[0, 1],
                                   [0, 2],
                                   [1, 3],
                                   [1, 4],
                                   [1, 5],
                                   [2, 6],
                                   [2, 7],
                                   [2, 8]], cost=[1, 4, 2, 3, 5, 7, 8, -4, 2]))
print()
print("res = ", placedCoins(edges=[[0, 1],
                                   [0, 2]], cost=[1, 2, -2]))
