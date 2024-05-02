"""
? Pattern: Minimum (Maximum) Path to Reach a Target
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: dungeon = [[-2, -3, 3],
                      [-5, -10, 1],
                      [10, 30, -5]]
    Output: 7
    Explanation: The initial health of the knight must be at least 7
                 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
* Example 2:
    Input: dungeon = [[0]]
    Output: 1
"""


def calculateMinimumHP(dungeon: list[list[int]]) -> int:
    cache = {}
    row_len, col_len = len(dungeon) - 1, len(dungeon[0]) - 1

    def _getMinHealth(row, col):
        """
            * For the Ex.1 two possible path
                -2 -> -3 -> 3 -> 1 -> -5     | cost = -6  <--- this is selected
                -2 -> -5 -> 10 -> 30 -> -5   | cost = 18

                * Case1: From above can understand we need to min value to take the next hop
                    -2 -> -3   ---> -3 is selected
                    -5         ---> insted of -5
                * Case2: Making sure the next hop is not very low 
                    eg.: -1 -50 ---> -50 cannot be selected 
                          ↓
                         -10    ---> here -10 needs to be selected 
                ? Thus we take a max(min(0, down)+ min(0, right))
        """
        key = (row, col)
        if key in cache:
            return cache[key]

        if row > row_len or col > col_len:
            # ? As at the end we take a max...
            return float('-inf')
        if row == row_len and col == col_len:
            return dungeon[row][col]

        """
            !TLDR: 
                ! the inner min help to go too MAX 
                !the outter max helps to go too MIN
        """
        cache[key] = dungeon[row][col] + max(min(0, _getMinHealth(row + 1, col)),
                                             min(0, _getMinHealth(row, col + 1)))

        return cache[key]

    """
    ? returning 1 or 
    ? -_getMinHealth + 1  ---> this makes the _getMinHealth +ve if -ve and vise-versa
    ?     Handling both case
              * dungeon=[[0]] and dungeon=[[100]] must return 1
    """
    return max(1, -_getMinHealth(0, 0) + 1)


print(calculateMinimumHP(dungeon=[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
print(calculateMinimumHP(dungeon=[[0]]))
print(calculateMinimumHP(dungeon=[[100]]))
