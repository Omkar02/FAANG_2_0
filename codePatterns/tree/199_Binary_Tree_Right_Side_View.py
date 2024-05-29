from DataStructure import BST, bNode, readyTree


def rightSideView(root: bNode) -> list[list[int]]:
    """
        * THIS IS A LEVEL ORDER SOLUTION WHERE IN WE STORE THE LAST VAL
    """
    if not root:
        return []
    q = [root]
    res = []
    while q:
        q_len = len(q)
        last_val = None
        for _ in range(q_len):
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            last_val = node.val
        res.append(last_val)
    return res


tree: BST = readyTree.printTree()
print(rightSideView(readyTree.getHead()))
