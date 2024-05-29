class bNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.nextRight = None

    def __str__(self) -> str:
        return f'VAL = {self.val} | LEFT = {self.left.val if self.left else "None"} | RIGHT = {self.right.val if self.right else "None"}'


class BST():
    def __init__(self):
        self.root = None

    def getHead(self):
        return self.root

    def insert(self, val):
        if self.root is None:
            self.root = bNode(val)
        else:
            self._insertInto(self.root, val)

    def _insertInto(self, node, val):
        if val < node.val:
            if not node.left:
                node.left = bNode(val)
            else:
                self._insertInto(node.left, val)
        else:
            if not node.right:
                node.right = bNode(val)
            else:
                self._insertInto(node.right, val)

    def Serach(self, val):
        actNode = self.root
        while actNode:
            if val < actNode.val:
                if actNode.val == val:
                    print('Found!')
                    return actNode
                else:
                    actNode = actNode.left
            else:
                if actNode.val == val:
                    print('Found!')
                    return actNode
                else:
                    actNode = actNode.right
        print('Nee!')

    def getSubNode(self, val: int):
        node = self.Serach(val)
        try:
            lines, _, _, _ = self._display_aux(node)
            for line in lines:
                print(line)

            return node

        except Exception as e:
            pass

    def printTree(self):
        try:
            lines, _, _, _ = self._display_aux(self.root)
            for line in lines:
                print(line)

        except Exception as e:
            pass

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        try:
            if node.right is None and node.left is None:
                line = '%s' % node.val
                width = len(line)
                height = 1
                middle = int(width // 2)
                return [line], width, height, middle

            # Only left child.
            if node.right is None:
                lines, n, p, x = self._display_aux(node.left)
                s = '%s' % node.val
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if node.left is None:
                lines, n, p, x = self._display_aux(node.right)
                s = '%s' % node.val
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = self._display_aux(node.left)
            right, m, q, y = self._display_aux(node.right)
            s = '%s' % node.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * \
                '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + \
                (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + \
                [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2
        except:
            pass


tree = BST()


readyTree = BST()
array = [6, 2, 1, 3, 5, 8, 7, 9, 10]
# array = [7, 2, 1, 3, 5, 8, 9, 10]
for i in array:
    readyTree.insert(i)
