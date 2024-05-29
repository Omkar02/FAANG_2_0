from DataStructure import BST, bNode, readyTree


def lowestCommonAncestor(root: bNode, p: int, q: int) -> bNode:
    def _dfs(node: bNode) -> bNode | None:
        if not node:
            return None
        if node.val == p or node.val == q:
            # * THIS CONDITION IS TO POPULATE THRE LEFT AND RIGHT VAR BELOW..
            return node
        left = _dfs(node.left)
        right = _dfs(node.right)

        if left and right:
            # * WE HAVE FOUND THE ANCESTORT NODE.
            return node

        # * IF THE A-NODE IS NOT IN LEFT SIDE RETURN RIGHT AND VISE-VERSA
        return left or right
    return _dfs(root)


tree: BST = readyTree.printTree()
print(lowestCommonAncestor(readyTree.getHead(), 1, 9))
