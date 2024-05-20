"""
* TYPE             : Graph
* ALGORITHM        : DFS 

* TIME-COMPLEXITY  : O(M x N)
* SPACE-COMPLEXITY : O(M x N)

* Example 1:
    Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    Output: 5
    Explanation: One way to remove 5 stones is as follows:
        1. Remove stone [2,2] because it shares the same row as [2,1].
        2. Remove stone [2,1] because it shares the same column as [0,1].
        3. Remove stone [1,2] because it shares the same row as [1,0].
        4. Remove stone [1,0] because it shares the same column as [0,0].
        5. Remove stone [0,1] because it shares the same row as [0,0].
        Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
* Example 2:
    Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    Output: 3
    Explanation: One way to make 3 moves is as follows:
        1. Remove stone [2,2] because it shares the same row as [2,0].
        2. Remove stone [2,0] because it shares the same column as [0,0].
        3. Remove stone [0,2] because it shares the same row as [0,0].
        Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
* Example 3:
    Input: stones = [[0,0]]
    Output: 0
    Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
"""


def removeStones(stones: list[list[int]]) -> int:
    """
    * HERE TAKE ALL THE ROWS AND COLS OF STONES WHICH COINSIDE WITH EITHER ROW OR COLS AND MAKE THEM NEIGHBOURS

    * APPLY DFS ON IT AND GROUP THEM TOGETHERE AND SEE HOW MAKY STONE CHUNK A CHUNK IS MORE THAT 1 CELL CAN BE REMOVED

    * AS PER THE STATEMENT ONCE A ROCK IS REMOVED WE CAN'T CONSIDER IT; USE VISITED FOR TRACKING IT.
    """
    stones_len = len(stones)
    visited = set()

    # * CREATE NEIGHBORS FOR ROW AND COL
    rows_neighbours = {}
    cols_neighbours = {}

    for idx, (x, y) in enumerate(stones):
        if x not in rows_neighbours:
            rows_neighbours[x] = []
        rows_neighbours[x].append(idx)

        if y not in cols_neighbours:
            cols_neighbours[y] = []
        cols_neighbours[y].append(idx)

    def _DFS(idx) -> int:
        key = idx
        if key in visited:
            return 0

        visited.add(key)
        row = stones[idx][0]
        col = stones[idx][1]
        # * SETTING COUNT 1 IS SAME AS RETURN 1 + _SOME_FUNCTION, AS HERE ROW'S AND COL'S ARE CALLED SEPERATLY
        count = 1
        if row in rows_neighbours:
            for new_row in rows_neighbours[row]:
                if new_row not in visited:
                    count += _DFS(new_row)
        if col in cols_neighbours:
            for new_col in cols_neighbours[col]:
                if new_col not in visited:
                    count += _DFS(new_col)

        return count

    res = 0
    for idx in range(stones_len):
        if idx not in visited:
            res += _DFS(idx) - 1
    return res


print(removeStones(stones=[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
print(removeStones(stones=[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
print(removeStones(stones=[[0, 0]]))
