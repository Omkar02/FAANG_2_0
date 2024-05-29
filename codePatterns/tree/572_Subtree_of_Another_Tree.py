from DataStructure import BST, bNode


def isSubtree(root: bNode, subRoot: bNode) -> bool:
    """
        * GO THROUGHT ALL THE NODE IN A ROOT TREE 
            * IF THE VALUE OF ROOT NODE AND SUB-ROOT-NODE IS EQUAL USE THE SAME-TREE LOGIC
            * COMPARING THE STRUCTURE AND THE VALUE
    """
    def is_same(node: bNode, sub_node: bNode) -> bool:
        if not node and not sub_node:
            return True
        if not node or not sub_node:
            return False

        if node.val != sub_node.val:
            return False

        return is_same(node.left, sub_node.left) and is_same(node.right, sub_node.right)

    # ------------------------ Main Code ------------------------
    if not root:
        return False
    if root.val == subRoot.val and is_same(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


# ? -------------------- Same -------------------
tree = BST()
[tree.insert(x) for x in [5, 2, 3, 4, 1, 6]]
tree.printTree()
subRoot = tree.getSubNode(2)
assert isSubtree(tree.getHead(), subRoot) == True
print("-" * 50)
# # ? ------------------ Not Same ------------------
tree = BST()
[tree.insert(x) for x in [5, 2, 3, 4, 1, 6]]
tree.printTree()

subtree = BST()
[subtree.insert(x) for x in [4, 2, 3, 5, 1, 6]]
subtree.printTree()

assert isSubtree(tree.getHead(), subtree.getHead()) == False
print("-" * 50)
