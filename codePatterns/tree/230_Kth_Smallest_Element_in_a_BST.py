from DataStructure import BST, bNode, readyTree


def kthSmallest(root: bNode, k: int) -> int:
    """
        * THIS IS A FLAVOUR OF INORDER TRAVERSAL [FOR BST IS SORTED FROM SMALLER TO BIGGER]
        * WHEREIN THE CUR_IDX TRACK THE INDEX TO GET THE KTH

    """
    res = 0
    cur_idx = 0

    def _getKthSmallest(node: bNode) -> None:
        nonlocal res, cur_idx
        if not node or (cur_idx > k):
            return
        _getKthSmallest(node.left)
        cur_idx += 1
        if cur_idx == k:
            res = node.val
        _getKthSmallest(node.right)

    _getKthSmallest(root)
    return res


tree: BST = readyTree.printTree()
print(kthSmallest(root=readyTree.getHead(), k=4))
