"""
! LEETCODE SOLUTIONS ON DOWN BELOW [THIS IS LOCAL MACHINE SOL]
* Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
* Example 2:
    Input: root = [1,null,2]
    Output: 2

"""

from DataStructure import readyTree, BST, bNode


def diameterOfBinaryTree(root: bNode) -> bNode:
    """
    ! As it turns out, the maximum diameter of a given tree need not 
    ! involve the root node of the tree. 
    """
    diameter = 0

    def get_depth(node: bNode) -> int:
        """
        This function needs to do the following:
            * Calculate the maximum depth of the left and right sides of the given node
            * Determine the diameter at the given node and check if its the maximum
        """

        nonlocal diameter
        if not node:
            return 0
        left = get_depth(node.left)
        right = get_depth(node.right)

        diameter = max(diameter, left + right)
        return 1 + max(left, right)
    get_depth(root)
    return diameter


tree: BST = readyTree.printTree()
print(diameterOfBinaryTree(readyTree.getHead()))
