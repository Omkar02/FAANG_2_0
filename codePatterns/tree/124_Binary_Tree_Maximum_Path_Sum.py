from DataStructure import BST, bNode, readyTree


def maxPathSum(root: bNode) -> int:
    if not root:
        return 0
    max_path_sum = root.val

    def _getMaxPathSum(node: bNode) -> int:
        nonlocal max_path_sum
        if not node:
            return 0

        left_max = max(_getMaxPathSum(node.left), 0)
        right_max = max(_getMaxPathSum(node.right), 0)

        max_path_sum = max(max_path_sum, left_max + node.val + right_max)

        # * here max of left and right is taken as only one path can be
        # * taken and that path must be the max_val path
        return node.val + max(left_max, right_max)
    _getMaxPathSum(root)
    return max_path_sum


tree: BST = readyTree.printTree()
print(maxPathSum(root=readyTree.getHead()))
print(6 + 8 + 9 + 10 + 5 + 2 + 3)

"""
*          __6_    
?         /    \   
*         2    8   
?        / \  / \  
*        1 3  7 9_ 
?           \     \
*           5    10

* max_path = 5 -> 3 -> 2 -> 6 -> 8 -> 9 -> 10 
? 43
"""
