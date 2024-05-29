from DataStructure import readyTree, BST, bNode


def isBalanced(root: bNode) -> bool:
    """
    * INTUTIONS HERE IS TO FIND THE HEIGHT OF LEFT_CHILD AND RIGHT_CHILD
    * AND MAKE SURE THE DIFFERENCE IS AT-MOST 1 i.e >= 1
    * ALSO CHECK THE THE LEFT SIDE AND THE RIGHT SIDE IS THAT EQUAL
    """

    def _isBalanced(node: bNode) -> list[bool, int]:
        if not node:
            return [True, 0]

        left, right = _isBalanced(node.left), _isBalanced(node.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balanced, 1 + max(left[1], right[1])]

    return _isBalanced(root)[0]


tree: BST = readyTree.printTree()
print(isBalanced(readyTree.getHead()))
