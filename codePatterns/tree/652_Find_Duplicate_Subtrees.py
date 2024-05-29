from DataStructure import BST, bNode, readyTree


def findDuplicateSubtrees(root: bNode) -> list[list[int]]:
    """
        * THE SOLUTION FROM EVERY NODE CREATE A PATH AND FOR THAT PATH INCREMENT A COUNTR
        * IF THE COUNTER == 2 FOR THAT PATH APPEND THE NODE TO THE RESULTS
    """
    res = []
    seq_count = {}

    def _DFS(node: bNode) -> tuple:
        if not node:
            return '*'
        left = _DFS(node.left)
        right = _DFS(node.right)

        key = (node.val, left, right)
        if key not in seq_count:
            seq_count[key] = 0
        seq_count[key] += 1
        if seq_count[key] == 2:
            res.append(node.val)
        return key
    _DFS(root)
    print(seq_count)
    return res


tree: BST = readyTree.printTree()
print(findDuplicateSubtrees(readyTree.getHead()))


tree: BST = BST()
[tree.insert(x) for x in [3, 2, 4, 2, 2, 4, 4]]
tree.printTree()
print(findDuplicateSubtrees(tree.getHead()))
