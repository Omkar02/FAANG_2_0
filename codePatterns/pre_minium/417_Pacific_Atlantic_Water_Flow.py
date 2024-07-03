"""
    * Time Complexity   : O(N x M)
    * Space Complexity  : O(N x M)
    * Date              : 10, June 2024
"""


def pacificAtlantic(matrix: list[list[int]]) -> list[list[int]]:
    row_range = range(len(matrix))
    col_range = range(len(matrix[0]))

    pacfic_visited = set()
    atlantic_visited = set()

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(row, col, visited):
        key = (row, col)
        if key in visited:
            return

        visited.add(key)
        for x, y in directions:
            new_row, new_col = x + row, y + col
            if new_row in row_range and new_col in col_range and \
                    matrix[new_row][new_col] >= matrix[row][col]:
                dfs(new_row, new_col, visited)

    # Iterate from Left border and Right border
    for row in row_range:
        dfs(row, 0, pacfic_visited)
        dfs(row, col_range[-1], atlantic_visited)

    # Iterate from Top border and Bottom border
    for col in col_range:
        dfs(0, col, pacfic_visited)
        dfs(row_range[-1], col, atlantic_visited)

    return list(pacfic_visited.intersection(atlantic_visited))


print(pacificAtlantic(matrix=[[1, 2, 2, 3, 5],
                              [3, 2, 3, 4, 4],
                              [2, 4, 5, 3, 1],
                              [6, 7, 1, 4, 5],
                              [5, 1, 1, 2, 4]]))
# Output = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
