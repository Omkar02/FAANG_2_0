
from DataStructure import BST, bNode, readyTree


def rob(root: bNode) -> int:

    def _getMaxRobery(node: bNode) -> tuple[int]:
        if not node:
            return (0, 0)  # * (rob_cur, skip_cur)
        left = _getMaxRobery(node.left)
        right = _getMaxRobery(node.right)

        # * if robbing curNode then add the skip sum of left and right sub-tree
        rob_cur = node.val + left[1] + right[1]
        # * if skipping the curNode then take the max of left and add it with max of right
        skip_cur = max(left) + max(right)

        return (rob_cur, skip_cur)

    # * return the max robery that can be done
    return max(_getMaxRobery(root))


tree: BST = readyTree.printTree()
print(rob(root=readyTree.getHead()))
