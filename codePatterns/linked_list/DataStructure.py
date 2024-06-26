import time


class Node:
    def __init__(self, val: int | str) -> None:
        self.val = val
        self.next = None

    def traverse(self, prefix=None):
        # THIS WOULD TRAVERSE FOR THE CUR_POINT
        cur_node = self
        if prefix:
            print(prefix, end=" ")
        while cur_node:
            print(cur_node.val, end=" -> ")
            cur_node = cur_node.next
        print('Null')
        return self

    def __str__(self):
        string = f"NodeValue = {self.val}"
        if self.next:
            string += f" | NextNode = {self.next.val}"
        return string


class LinkedList:
    def __init__(self, arr: list) -> None:
        self.head = None
        self._create_list(arr)

    def getHead(self) -> Node: return self.head
    def setHead(self, node: Node) -> None: self.head = node

    def _create_list(self, arr: list) -> None:
        pre_node = None
        for v in arr:
            node = Node(v)
            if not self.head:
                pre_node = node
                self.head = node
            else:
                pre_node.next = node
                pre_node = node
        return self

    def insertLoop(self, loopNodeVal: int):
        # * GETTING THE LAST NODE
        cur_node = self.head
        while cur_node and cur_node.next:
            cur_node = cur_node.next

        cur_node.next = self.getNodeWithVal(loopNodeVal)
        return self

    def getNodeWithVal(self, val: int) -> Node:
        cur_node = self.head
        while cur_node:
            if cur_node.val == val:
                return cur_node
            cur_node = cur_node.next

    def display(self, prefix=None, delay=0) -> None:
        cur_node = self.head
        if prefix:
            print(prefix, end=" ")
        while cur_node:
            print(cur_node.val, end=" -> ")
            cur_node = cur_node.next
            time.sleep(delay)
        print('Null')
        return self


if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5]
    l = LinkedList(arr)
    l.display()
