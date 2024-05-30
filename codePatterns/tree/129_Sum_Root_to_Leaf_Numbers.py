

from DataStructure import bNode


def sumNumbers(root: bNode) -> int:
    """
        * THIS IS A DFS AND STORING ALL THE PATH
        * THEN CONVERTING THE STR TO INT AND ADDING ALL
    """
    all_path = []

    def _dfs(node: bNode, path: str):
        if not node:
            return

        path += str(node.val)

        _dfs(node.left, path)
        _dfs(node.right, path)

        if not node.left and not node.right:
            # * THIS IS THE PLACE WHERE WE ADD THE PATH TO ALL_PATH AS DFS IS COMPLETED HERE.
            all_path.append(path)

    _dfs(root, "")
    sum_val = 0
    for num in all_path:
        sum_val += int(num)
    return sum_val


head = bNode(1)
head.left = bNode(2)
head.right = bNode(3)
print(sumNumbers(root=head))


def sumNumbers(root: bNode) -> int:
    def _dfs(node: bNode, val: int) -> int:
        if not node:
            return 0
        val = (val * 10) + node.val
        if not node.left and not node.right:
            return val
        return _dfs(node.left, val) + _dfs(node.right, val)
    return _dfs(root, 0)


head = bNode(1)
head.left = bNode(2)
head.right = bNode(3)
print(sumNumbers(root=head))
