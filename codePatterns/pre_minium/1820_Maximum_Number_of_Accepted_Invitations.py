"""
    * Time Complexity   : O(N*M)
    * Space Complexity  : O(N*M)
    * Date              : 9, June 2024
"""

"""
* Example 1:
    Input: grid = [[1,1,1],
                   [1,0,1],
                   [0,0,1]]
    Output: 3
    Explanation: The invitations are sent as follows:
    - The 1st boy invites the 2nd girl.
    - The 2nd boy invites the 1st girl.
    - The 3rd boy invites the 3rd girl.
* Example 2:
    Input: grid = [[1,0,1,0],
                   [1,0,0,0],
                   [0,0,1,0],
                   [1,1,1,0]]
    Output: 3
    Explanation: The invitations are sent as follows:
    -The 1st boy invites the 3rd girl.
    -The 2nd boy invites the 1st girl.
    -The 3rd boy invites no one.
    -The 4th boy invites the 2nd girl.
"""


def maximumInvitations(grid: list[list[int]]) -> int:
    # The problem can be modeled as a bipartite graph
    row_range = range(len(grid))
    col_range = range(len(grid[0]))

    def dfs(row):
        for col in col_range:
            if grid[row][col] and col not in visited:
                visited.add(col)
                if match[col] is None or dfs(match[col]):
                    match[col] = row
                    return True
        return False

    match = [None for _ in col_range]
    count = 0
    for row in row_range:
        visited = set()

        if dfs(row):
            count += 1
    return count


print(maximumInvitations(grid=[[1, 1, 1],
                               [1, 0, 1],
                               [0, 0, 1]]))  # 3

print(maximumInvitations(grid=[[1, 0, 1, 0],
                               [1, 0, 0, 0],
                               [0, 0, 1, 0],
                               [1, 1, 1, 0]]))  # 3


print(maximumInvitations(grid=[[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                               [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                               [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]]))  # 9
