from DataStructure import BST, bNode, readyTree


def levelOrder(root: bNode) -> list[list[int]]:
    if not root:
        return
    q = [root]
    res = []
    while q:
        q_len = len(q)
        temp = []
        for _ in range(q_len):
            cur_node = q.pop(0)
            temp.append(cur_node.val)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        res.append(temp)
    return res


tree: BST = readyTree.printTree()
print(levelOrder(readyTree.getHead()))
