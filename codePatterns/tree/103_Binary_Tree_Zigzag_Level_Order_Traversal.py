from DataStructure import BST, bNode, readyTree


def zigzagLevelOrder(root: bNode) -> list[list[int]]:
    """
        * THIS IS A LEVEL ORDER TRAVERSAL
        * HERE A FLAG IS MAINTAIN TO KEEP TRACK OF DIRECTIONS
    """
    res = []
    q = [root]
    to_reverse = False
    while q:
        q_len = len(q)
        temp = []
        for _ in range(q_len):
            node = q.pop(0)
            temp.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        temp = temp[::-1] if to_reverse else temp
        res.append(temp)

        to_reverse = not to_reverse
    return res


tree: BST = readyTree.printTree()
print(zigzagLevelOrder(readyTree.getHead()))
