"""
    * Time Complexity   : O(N)
    * Space Complexity  : O(N)
    * Date              : 7, June 2024
"""
from TreeDataStructure import readyTree, BST, bNode


def printTree(root: bNode) -> list[list[str]]:
    # Step 1: Get the height of the tree.
    def get_height(node: bNode) -> int:
        if not node:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))

    height = get_height(root)
    # Step 2: Get the width of the tree.
    width = 2 ** height - 1
    print(f'Height = {height} | Width = {width}')

    # Step 3: compute the print matrix
    def compute(node: bNode, lo: int, hi: int, depth: int) -> None:
        if not node:
            return
        mid = (lo + hi) // 2
        mat[depth][mid] = str(node.val)

        compute(node.left, lo, mid, depth + 1)
        compute(node.right, mid, hi, depth + 1)

    mat = [[" " for _ in range(width)] for _ in range(height)]
    compute(root, 0, width, 0)
    return mat


t: BST = readyTree.printTree()
[print(x) for x in printTree(t.getHead())]
