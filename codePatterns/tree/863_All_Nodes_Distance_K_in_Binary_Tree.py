from DataStructure import BST, bNode, readyTree


class Solution:
    def __init__(self) -> None:
        self.parent_map = {}

    def distanceK(self, root: bNode, target: int, k: int) -> int:
        """
            * THE SOL. IS TO MAKE IT A GRAPH PROBLEM AND DO BFS
        """
        self._constructParentMap(root, None)
        # print(self.parent_map)
        return self._BFS(target, k)

    def _constructParentMap(self, node: bNode | None, parent: bNode | None):
        # * CREATE MAPPING OF THE CHILD TO PARENT LINK
        if not node:
            return

        if parent:
            self.parent_map[node.val] = parent

        self._constructParentMap(node.left, node)
        self._constructParentMap(node.right, node)

    def _BFS(self, target: bNode, k: int) -> list:
        """
            * THIS MAKE A TREE PROBLEM INTO GRAPH PROBLEM
            * WHERE IN A NODE IS CONNECTED TO 3 NODE'S
                * PARENT NODE [USING PARENT_MAP]
                * LEFT CHILD NODE
                * RIGHT CHILD NODE
        """
        q = [(target, 0)]  # (node, cur_level)
        k_nodes = []
        visited = set()
        while q:
            cur_node, cur_level = q.pop(0)
            if cur_node.val not in visited:
                visited.add(cur_node.val)

                if cur_node.val in self.parent_map:
                    q.append((self.parent_map.get(cur_node.val), cur_level + 1))
                if cur_node.left:
                    q.append((cur_node.left, cur_level + 1))
                if cur_node.right:
                    q.append((cur_node.right, cur_level + 1))
            else:
                continue
            if cur_level == k:
                k_nodes.append(cur_node.val)

        return k_nodes


tree: BST = readyTree.printTree()
s = Solution()
target: bNode = readyTree.Serach(2)
print(s.distanceK(root=readyTree.getHead(), target=target, k=2))
