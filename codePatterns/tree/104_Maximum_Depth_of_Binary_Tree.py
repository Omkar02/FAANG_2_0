"""
* Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
* Example 2:
    Input: root = [1,null,2]
    Output: 2

"""

from DataStructure import readyTree, BST, bNode


def maxDepth(root: bNode) -> bNode:
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))


tree: BST = readyTree.printTree()
print(maxDepth(readyTree.getHead()))
