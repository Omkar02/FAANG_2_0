"""
! [NOTION] LOCAL RUN FOR LEETCODE SOL SCROLL DOWN
? DataStructure = https://github.com/Omkar02/FAANG_2_0/blob/master/codePatterns/linked_list/DataStructure.py

* Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
* Example 2:
    Input: list1 = [], list2 = []
    Output: []
* Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]
"""

from DataStructure import LinkedList, Node


def traverse(head: Node):
    cur_node = head
    print('-'*50)
    print("RES = ", end=" ")
    while cur_node:
        print(cur_node.val, end=" -> ")
        cur_node = cur_node.next
    print("N")
    print('-'*50)
    print()


def mergeTwoLists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    if not list1:
        return list2
    if not list2:
        return list1
    cur_node = head = Node("-1")

    p1, p2 = list1.getHead(), list2.getHead()

    while p1 and p2:
        if p1.val < p2.val:
            cur_node.next = p1
            p1 = p1.next
        else:
            cur_node.next = p2
            p2 = p2.next
        cur_node = cur_node.next

    cur_node.next = p1 or p2
    return head.next


l1 = LinkedList([1, 2, 4]).display("LL1 = ")
l2 = LinkedList([1, 3, 4]).display("LL2 = ")
traverse(mergeTwoLists(l1, l2))


l1 = LinkedList([]).display("LL1 = ")
l2 = LinkedList([]).display("LL2 = ")
traverse(mergeTwoLists(l1, l2))

l1 = LinkedList([]).display("LL1 = ")
l2 = LinkedList([0]).display("LL2 = ")
traverse(mergeTwoLists(l1, l2))
