"""
* TYPE             : Graph
* ALGORITHM        : DFS or BFS

* TIME-COMPLEXITY  : N x M
* SPACE-COMPLEXITY : N x M


* Example 1:
    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
    !Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
* Example 2:
    Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
    Output: [[0,0,0],[0,0,0]]
    Explanation: The starting pixel is already colored 0, so no changes are made to the image.
"""


def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    # BFS SOLUTION
    if image[sr][sc] == color:
        # NO NEED TO CHANGE AS THE COLOR IS ALREADY APPLIED.
        return image
    row_range, col_range = range(len(image)), range(len(image[0]))
    color_to_change = image[sr][sc]
    visited = set()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = [(sr, sc)]

    while len(q) > 0:
        # * SINCE THIS IS A BFS 0th ELEMENT IS POPED FROM QUEUE
        # * F.I.F.O -> FIRST IN FIRST OUT
        row, col = q.pop(0)
        for x, y in directions:
            new_row, new_col = row + x, col+y
            if new_row in row_range and new_col in col_range and \
                    image[new_row][new_col] == color_to_change and \
                    (new_row, new_col) not in visited:

                image[new_row][new_col] = color
                q.append((new_row, new_col))
                visited.add((new_row, new_col))
    return image


def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    # DFS SOLUTION
    if image[sr][sc] == color:
        # NO NEED TO CHANGE AS THE COLOR IS ALREADY APPLIED.
        return image
    row_range, col_range = range(len(image)), range(len(image[0]))
    color_to_change = image[sr][sc]
    visited = set()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def _DFS(row, col):
        # * THIS IS A DFS SOLUTION WHERE IN A STACK IS USED
        # * SINCE THE SOL. IS RECURSSIVE -> STACK IS THE UDERLINE DS HERE
        # * L.I.F.O -> LAST IN FIRST OUT
        key = (row, col)
        if key in visited:
            return
        if row not in row_range or col not in col_range:
            return
        if image[row][col] != color_to_change:
            return

        image[row][col] = color
        visited.add(key)

        for x, y in directions:
            new_row, new_col = row + x, col + y
            _DFS(new_row, new_col)
    _DFS(sr, sc)
    return image


[print(x) for x in floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]],
                             sr=1, sc=1, color=2)]
print()
[print(x) for x in floodFill(image=[[0, 0, 0], [0, 0, 0]],
                             sr=0, sc=0, color=0)]
