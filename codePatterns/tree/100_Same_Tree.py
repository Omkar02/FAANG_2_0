from DataStructure import BST, bNode


def isSameTree(p: bNode, q: bNode) -> bool:
    """
    * THE INTUTION HERE IS TO CHECK ALL THE LEFT AND RIGHT SIDE IN THE SAME DFS CALL
    * THIS WILL COMPARE THE VAL AND THE STRUCTURE OF BOTH TREE
    """
    def _is_same(nodeOne: bNode, nodeTwo: bNode) -> bool:
        if not nodeOne and not nodeTwo:
            # * THIS IS THE TRUE CASE WHERE IN BOTH HAVE REACHED TO A NONE NODE.
            return True
        if not nodeOne or not nodeTwo:
            # * IF EITHER NODE_ONE OR NODE_TWO IS NULL MEANS THERE'S A MISMATCH IN STRUCTURE
            return False

        if nodeOne.val != nodeTwo.val:
            return False

        return _is_same(nodeOne.left, nodeTwo.left) and _is_same(nodeOne.right, nodeTwo.right)
    return _is_same(p, q)


# ? -------------------- Same -------------------
treeOne = BST()
[treeOne.insert(x) for x in [5, 2, 3, 4, 1, 6]]
treeOne.printTree()

treeTwo: BST = BST()
[treeTwo.insert(x) for x in [5, 2, 3, 4, 1, 6]]
treeTwo.printTree()

assert isSameTree(treeOne.getHead(), treeTwo.getHead()) == True
print("-" * 50)
# ? ------------------ Not Same ------------------
treeOne = BST()
[treeOne.insert(x) for x in [1, 2, 3, 4, 1, 6]]
treeOne.printTree()

treeTwo: BST = BST()
[treeTwo.insert(x) for x in [5, 2, 3, 4, 1, 6]]
treeTwo.printTree()

assert isSameTree(treeOne.getHead(), treeTwo.getHead()) == False
