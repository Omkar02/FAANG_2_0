from DataStructure import BST, bNode, readyTree


class Codec:

    def serialize(self, root: bNode) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return " ".join(self._encode(root, []))

    def _encode(self, node: bNode, path: list) -> str:
        if not node:
            path.append("#")
            return path
        path.append(str(node.val))

        self._encode(node.left, path)
        self._encode(node.right, path)

        return path

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        return self._decode(iter(data.split(" ")))

    def _decode(self, data: iter) -> bNode:
        cur_node = next(data)
        if cur_node == '#':
            return
        new_node = bNode(int(cur_node))
        new_node.left = self._decode(data)
        new_node.right = self._decode(data)

        return new_node


tree: BST = readyTree.printTree()

c = Codec()
encoded = c.serialize(root=readyTree.getHead())
print(f'Encoded = {encoded}')

decoded: bNode = c.deserialize(data=encoded)
print(decoded)


