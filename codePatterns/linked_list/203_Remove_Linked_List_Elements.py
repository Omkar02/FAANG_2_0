"""
! [NOTION] LOCAL RUN FOR LEETCODE SOL SCROLL DOWN
? DataStructure = https://github.com/Omkar02/FAANG_2_0/blob/master/codePatterns/linked_list/DataStructure.py

* Example 1:
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]
* Example 2:
    Input: head = [], val = 1
    Output: []
* Example 3:
    Input: head = [7,7,7,7], val = 7
    Output: []
"""

from DataStructure import LinkedList, Node


def removeElements(head: Node, val: int) -> Node:
    dummy_node = cur_node = Node(-1)
    dummy_node.next = head

    while cur_node and cur_node.next:
        if cur_node.next.val == val:
            cur_node.next = cur_node.next.next
        else:
            cur_node = cur_node.next

    dummy_node.traverse('\t Res = ')
    print()
    return dummy_node.next


ll = LinkedList([1, 2, 6, 3, 4, 5, 6]).display()
removeElements(head=ll.getHead(), val=6)

ll = LinkedList([]).display()
removeElements(head=ll.getHead(), val=1)

ll = LinkedList([7, 7, 7, 7]).display()
removeElements(head=ll.getHead(), val=7)
