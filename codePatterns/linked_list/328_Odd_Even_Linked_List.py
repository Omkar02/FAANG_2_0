"""
! [NOTION] LOCAL RUN FOR LEETCODE SOL SCROLL DOWN
? DataStructure = https://github.com/Omkar02/FAANG_2_0/blob/master/codePatterns/linked_list/DataStructure.py

* Example 1:
    Input: head = [1,2,3,4,5]
    Output: [1,3,5,2,4]
* Example 2:
    Input: head = [2,1,3,5,6,4,7]
    Output: [2,3,6,7,1,5,4]
"""

from DataStructure import LinkedList, Node


def oddEvenList(head: Node) -> Node:
    odd = head
    even = temp_start = odd.next

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = temp_start
    return head


ll: LinkedList = LinkedList([1, 2, 3, 4, 5]).display()
oddEvenList(ll.getHead()).traverse()

print('-' * 50)

ll: LinkedList = LinkedList([2, 1, 3, 5, 6, 4, 7]).display()
oddEvenList(ll.getHead()).traverse()
