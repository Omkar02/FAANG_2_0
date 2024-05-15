"""
* TYPE             : Graph
* ALGORITHM        : DFS or UNION-FIND

* TIME-COMPLEXITY  :
* SPACE-COMPLEXITY :


* Example 1:
    Input: grid = [
                    ["1","1","1","1","0"],
                    ["1","1","0","1","0"],
                    ["1","1","0","0","0"],
                    ["0","0","0","0","0"]
                ]
    Output: 1
* Example 2:
    Input: grid = [
                    ["1","1","0","0","0"],
                    ["1","1","0","0","0"],
                    ["0","0","1","0","0"],
                    ["0","0","0","1","1"]
                ]
    Output: 3
"""


# def numIslands(grid: list[list[str]]) -> int:
#     # * DFS SOLUTION
#     row_range, col_range = range(len(grid)), range(len(grid[0]))
#     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     visited = set()

#     def _DFS(row, col):
#         key = (row, col)
#         if key in visited:
#             return
#         if row not in row_range or col not in col_range:
#             return

#         if grid[row][col] == "0":
#             return

#         visited.add(key)
#         for x, y in directions:
#             new_row, new_col = row+x, col+y
#             _DFS(new_row, new_col)

#     island_count = 0
#     for row in row_range:
#         for col in col_range:
#             if (row, col) not in visited and grid[row][col] == "1":
#                 _DFS(row, col)
#                 island_count += 1
#     return island_count

class UnionFind:
    def __init__(self):
        self.represents = {}

    def findParent(self, node: int):
        # * HERE IF THE NODE IS PRESENT IN REPRESENTS RETURN IT
        # * OR USE SAME NODE.
        parent = self.represents.get(node, node)
        if node != parent:
            parent = self.findParent(parent)
            self.represents[node] = parent

        return parent

    def union(self, p_node: int, c_node: int) -> None:
        _parent = self.findParent(p_node)
        _child = self.findParent(c_node)
        self.represents[_child] = _parent


def numIslands(grid: list[list[str]]) -> int:
    row_range, col_range = range(len(grid)), range(len(grid[0]))
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    UF = UnionFind()

    for row in row_range:
        for col in col_range:
            if grid[row][col] == "1":
                for x, y in directions:
                    new_row, new_col = row + x, col + y
                    if new_row in row_range and new_col in col_range and grid[new_row][new_col] == "1":
                        # * AS UNION-FIND WORKS ON 1-D ARR AND NOT 2-D GRIDS
                        # * BELOW STEP IS TO FLATTEN / ENCODE THE VALUE IN..
                        parent = (row, col)
                        child = (new_row, new_col)
                        UF.union(parent, child)

    groups = set()
    for row in row_range:
        for col in col_range:
            if grid[row][col] == "1":
                key = (row, col)
                parent = UF.findParent(key)
                groups.add(parent)
    return len(groups)


print(numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
print(numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
