"""
* Example 1:
    Input: root = [1,null,2,3]
    Output: [1,3,2]
* Example 2:
    Input: root = []
    Output: []
* Example 3:
    Input: root = [1]
    Output: [1]
"""
from DataStructure import readyTree, BST, bNode


def inorderTraversal(root: bNode) -> list[int]:
    res = []

    def _traverse(node: bNode) -> None:
        if not node:
            return

        res.append(node.val)
        _traverse(node.left)
        _traverse(node.right)
    _traverse(root)
    return res


tree: BST = readyTree.printTree()
print(inorderTraversal(readyTree.getHead()))
