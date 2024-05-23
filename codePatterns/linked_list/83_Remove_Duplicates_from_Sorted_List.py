"""
! [NOTION] LOCAL RUN FOR LEETCODE SOL SCROLL DOWN
? DataStructure = https://github.com/Omkar02/FAANG_2_0/blob/master/codePatterns/linked_list/DataStructure.py

* Example 1:
    Input: head = [1,1,2]
    Output: [1,2]
* Example 2:
    Input: head = [1,1,2,3,3]
    Output: [1,2,3]
"""

from DataStructure import LinkedList, Node


def deleteDuplicates(head: Node) -> Node:
    dummy_node = cur_node = Node(None)
    dummy_node.next = head

    # * CHECKING IF CUR_NODE AND CUR_NODE.NEXT ARE NOT NONE
    while cur_node and cur_node.next:
        if cur_node.val == cur_node.next.val:
            # * IF SO WE UPDATE THE POINTER OF THE PREV TO POINT TO NEXT.NEXT
            cur_node.next = cur_node.next.next
        else:
            # * OR MOVE ON...
            cur_node = cur_node.next

    dummy_node.next.traverse('\tres = ')
    return dummy_node.next


ll = LinkedList([1, 1, 2]).display()
deleteDuplicates(head=ll.getHead())

ll = LinkedList([1, 1, 2, 3, 3]).display()
deleteDuplicates(head=ll.getHead())
