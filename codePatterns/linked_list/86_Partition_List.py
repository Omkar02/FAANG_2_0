"""
! [NOTION] LOCAL RUN FOR LEETCODE SOL SCROLL DOWN
? DataStructure = https://github.com/Omkar02/FAANG_2_0/blob/master/codePatterns/linked_list/DataStructure.py

* Example 1:
    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]
* Example 2:
    Input: head = [2,1], x = 2
    Output: [1,2]
"""
from DataStructure import LinkedList, Node


def partition(head: Node, x: int) -> Node:
    """
    THE IDEA IS SIME CREATE TWO NEW LIST A
    WHICH TRACKS THE LESSER AND GREATER NODE.VAL'S
    """
    left_start = left_end = Node(-1)
    right_start = right_end = Node(-1)

    cur_node = head
    while cur_node:
        _val = cur_node.val

        if _val < x:
            left_end.next = cur_node
            left_end = left_end.next

        else:
            right_end.next = cur_node
            right_end = right_end.next

        cur_node = cur_node.next

    left_end.next = right_start.next

    # * MAKE SURE THAT THE RIGHT_END POINTER MUST POINT TO NONE
    # * AS WE ARE COPYING THE CUR_NDOE AND IT MIGHT HAVE A NEXT VAL
    # * THIS WOULD CAUSE AN ARTIFACT WHICH LEADS TO CYCLES
    right_end.next = None
    return left_start.next


ll: LinkedList = LinkedList([1, 4, 3, 2, 5, 2]).display()
partition(head=ll.getHead(), x=3).traverse()
print("-" * 50)


ll: LinkedList = LinkedList([2, 1]).display()
partition(head=ll.getHead(), x=2).traverse()
print("-" * 50)
