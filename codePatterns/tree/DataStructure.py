class bNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.nextRight = None


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


class aNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

        self.height = 0


val = []


class AVL():
    def __init__(self):
        self.root = None

    def _calHeight(self, node):
        if not node:
            return -1
        return node.height

    def _calBalance(self, node):
        if not node:
            return 0
        return self._calHeight(node.left) - self._calHeight(node.right)

    def _rotateRight(self, node):
        print(f'Rotating node {node.val} to right!')
        templeftChild = node.left
        t = templeftChild.right

        templeftChild.right = node
        node.left = t

        node.height = max(self._calHeight(node.left),
                          self._calHeight(node.right)) + 1
        templeftChild.height = max(self._calHeight(
            templeftChild.left), self._calHeight(templeftChild.right)) + 1

        return templeftChild

    def _rotateLeft(self, node):
        print(f'Rotating node {node.val} to left!')
        tempRightChild = node.right
        t = tempRightChild.left

        tempRightChild.left = node
        node.right = t

        node.height = max(self._calHeight(node.left),
                          self._calHeight(node.right)) + 1
        tempRightChild.height = max(self._calHeight(
            tempRightChild.left), self._calHeight(tempRightChild.right)) + 1

        return tempRightChild

    def iAvl(self, val):
        self.root = self._insertA(val, self.root)

    def _insertA(self, val, node):
        if not node:
            return aNode(val)
        if val < node.val:
            node.left = self._insertA(val, node.left)
        if val > node.val:
            node.right = self._insertA(val, node.right)

        node.height = max(self._calHeight(node.left),
                          self._calHeight(node.right)) + 1
        return self._checkViolation(val, node)
        # return node

    def _checkViolation(self, val, node):
        balance = self._calBalance(node)

        # case1: it is a left-left heavy situation
        if balance > 1 and val < node.left.val:
            print('left-left heavy situation | Rotating right..')
            return self._rotateRight(node)

        # case2: it is a right right heavy situation
        if balance < -1 and val > node.right.val:
            print('right-right heavy situation | Rotating left')
            return self._rotateLeft(node)

        # case3: it is a left right heavy situation
        if balance > 1 and val > node.left.val:
            print('left-right heavy situation | Rotating left-right')
            node.left = self._rotateLeft(node.left)
            return self._rotateRight(node)

        # case4: it is a right left heavy situation
        if balance < -1 and val < node.right.val:
            print('right left heavy situation | Rotating right-left')
            node.right = self._rotateRight(node.right)
            return self._rotateLeft(node)

        return node

    def _removeViolation(self, node):
        if not node:
            return node

        node.height = max(self._calHeight(node.left),
                          self._calHeight(node.right)) + 1
        balance = self._calBalance(node)

        # case1: it is a left-left heavy situation
        if balance > 1 and self._calBalance(node.left) >= 0:
            print('left-left heavy situation | Rotating right..')
            return self._rotateRight(node)

        # case2: it is a right right heavy situation
        if balance < -1 and self._calBalance(node.right) <= 0:
            print('right-right heavy situation | Rotating left')
            return self._rotateLeft(node)

        # case3: it is a left right heavy situation
        if balance > 1 and self._calBalance(node.left) < 0:
            print('left-right heavy situation | Rotating left-right')
            node.left = self._rotateLeft(node.left)
            return self._rotateRight(node)

        # case4: it is a right left heavy situation
        if balance < -1 and self._calBalance(node.right) > 0:
            print('right left heavy situation | Rotating right-left')
            node.right = self._rotateRight(node.right)
            return self._rotateLeft(node)

        return node

    def remove(self, val):
        if self.root:
            self.root = self._removeNode(val, self.root)

    def _removeNode(self, val, node):
        if not node:
            return node

        if val < node.val:
            node.left = self._removeNode(val, node.left)

        elif val > node.val:
            node.right = self._removeNode(val, node.right)

        else:
            if not node.left and not node.right:
                print('Deleting Leaf node!')
                del node
                return None

            if not node.left:
                print('Deleting right child!')
                tempnode = node.right
                del node
                return tempnode

            if not node.right:
                print('Deleting left child!')
                tempnode = node.left
                del node
                return tempnode

            print('Deleting node with Two  child!')
            print(node.left.val)
            tempnode = self._getPredsessor(node.left)
            # print(tempnode,'============')
            node.val = tempnode.val
            node.left = self._removeNode(tempnode.val, node.left)

        # if not node:

        return self._removeViolation(node)  # MAGIC
        # return node

    def _getPredsessor(self, node):
        if node.right:
            return self._getPredsessor(node.right)
        return node

    def traverse(self):
        if self.root:
            self._traInter(self.root)

    def _traInter(self, node):
        if node.left:
            self._traInter(node.left)

        # print(node.val)
        val.append(node.val)

        if node.right:
            self._traInter(node.right)

    def printTree(self):
        try:
            lines, _, _, _ = self._display_aux(self.root)
            for line in lines:
                print(line)
            return self

        except Exception as e:
            pass

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
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


avl = AVL()


# array = [21, 26, 30, 9, 4, 14, 28]
# for i in array:
#     avl.iAvl(i)


# avl.printTree()
