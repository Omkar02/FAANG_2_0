"""
! [NOTION] LOCAL RUN FOR LEETCODE SOL SCROLL DOWN
? DataStructure = https://github.com/Omkar02/FAANG_2_0/blob/master/codePatterns/linked_list/DataStructure.py

* Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
* Example 2
    Input: head = [1], n = 1
    Output: []
* Example 3
    Input: head = [1,2], n = 1
    Output: [1]
"""

from DataStructure import LinkedList, Node


def removeNthFromEnd(head: Node, n: int) -> Node:
    p1 = p2 = head
    # * MAKE P1 TRAVERSE THE FIRST N-1 STEPS
    for _ in range(n):
        p1 = p1.next

    if not p1:
        # * WE HAVE SURPASSED THE NTH POINT
        return head.next

    while p1 and p1.next:
        # * USING P1 AND P1.NEXT SO WE LAND -1 TO THE NODE
        # * AND WE CAN UPDATE IT NEXT POINTER TO SKIP THE NEXT ONE
        p1 = p1.next
        p2 = p2.next

    p2.next = p2.next.next
    return head


ll: LinkedList = LinkedList([1, 2, 3, 4, 5]).display()
removeNthFromEnd(ll.getHead(), 2)


print('-' * 50)

ll: LinkedList = LinkedList([1]).display()
removeNthFromEnd(ll.getHead(), 1)


print('-' * 50)

ll: LinkedList = LinkedList([1, 2]).display()
removeNthFromEnd(ll.getHead(), 1)
