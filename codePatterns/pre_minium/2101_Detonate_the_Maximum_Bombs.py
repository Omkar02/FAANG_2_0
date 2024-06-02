"""
    * Time Complexity   : O(N ^ 2)
    * Space Complexity  : O(N)
    * Date              : 2, June 2024
"""

"""
* Example 1:
    Input: bombs = [[2,1,3],[6,1,4]]
    Output: 2
    Explanation:
        The above figure shows the positions and ranges of the 2 bombs.
        If we detonate the left bomb, the right bomb will not be affected.
        But if we detonate the right bomb, both bombs will be detonated.
        So the maximum bombs that can be detonated is max(1, 2) = 2.
* Example 2:
    Input: bombs = [[1,1,5],[10,10,5]]
    Output: 1
    Explanation:
        Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.
* Example 3:
    Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
    Output: 5
    Explanation:
        The best bomb to detonate is bomb 0 because:
        - Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
        - Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
        - Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
        Thus all 5 bombs are detonated.
"""




import math
class Solution:
    def __init__(self) -> None:
        self.bomb_locations = None
        self.visited = set()
        self.connected_loc = {}

    def _is_connected(self, a, b):
        xOne, yOne, radiusOne = self.bomb_locations[a]
        xTwo, yTwo, radiusTwo = self.bomb_locations[b]

        dist = math.sqrt((xOne - xTwo) ** 2 + (yOne - yTwo) ** 2)
        return dist <= radiusOne

    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        """
            * The intutions here is to check if two bombs are in overlaping radius if so they are connected
            * Use this knowledge to traverse and get max_path in graph
        """
        self.bomb_locations = bombs

        for loc_one in range(len(bombs)):
            for loc_two in range(len(bombs)):
                if loc_one != loc_two:
                    if self._is_connected(loc_one, loc_two):
                        if loc_one not in self.connected_loc:
                            self.connected_loc[loc_one] = []
                        self.connected_loc[loc_one].append(loc_two)

        # print(self.connected_loc)
        max_detonated_bombs = 1
        self.visited = set()
        for src in self.connected_loc:
            max_detonated_bombs = max(max_detonated_bombs,
                                      self._dfs(src))
            self.visited = set()

        # print('res = ', max_detonated_bombs)
        return max_detonated_bombs

    def _dfs(self, node: int) -> int:
        if node in self.visited:
            return 0
        self.visited.add(node)

        hops = 1
        if node in self.connected_loc:
            for next_node in self.connected_loc[node]:
                hops += self._dfs(next_node)
        return hops


s = Solution().maximumDetonation(bombs=[[2, 1, 3], [6, 1, 4]])

s = Solution().maximumDetonation(bombs=[[1, 1, 5], [10, 10, 5]])

s = Solution().maximumDetonation(bombs=[[1, 2, 3],
                                        [2, 3, 1],
                                        [3, 4, 2],
                                        [4, 5, 3],
                                        [5, 6, 4]])
