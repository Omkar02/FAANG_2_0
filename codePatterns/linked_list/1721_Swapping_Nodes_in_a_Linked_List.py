"""
! [NOTION] LOCAL RUN FOR LEETCODE SOL SCROLL DOWN
? DataStructure = https://github.com/Omkar02/FAANG_2_0/blob/master/codePatterns/linked_list/DataStructure.py

* Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [1,4,3,2,5]
* Example 2:
    Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
    Output: [7,9,6,6,8,7,3,0,9,5]

"""
from DataStructure import LinkedList, Node


def swapNodes(head: Node, k: int) -> Node:
    right_idx = second = head

    for _ in range(k - 1):
        # * TILL THE 0TH IDX KTH POINT SO K - 1 AND RANGE ALSO INGNORING THE LAST VAL
        second = second.next

    # * SAVING THE second POINTER AS IT'S THE right_idx POINT
    left_idx = second

    while second and second.next:
        right_idx = right_idx.next
        second = second.next

    left_idx.val, right_idx.val = right_idx.val, left_idx.val

    return head


ll: LinkedList = LinkedList([1, 2, 3, 4, 5]).display()
swapNodes(ll.getHead(), 2).traverse('res = ')
print("-" * 50)

ll: LinkedList = LinkedList([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]).display()
swapNodes(ll.getHead(), 5).traverse('res = ')
print("-" * 50)
