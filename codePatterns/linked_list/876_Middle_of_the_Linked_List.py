"""
! [NOTION] LOCAL RUN FOR LEETCODE SOL SCROLL DOWN
? DataStructure = https://github.com/Omkar02/FAANG_2_0/blob/master/codePatterns/linked_list/DataStructure.py

* Example 1:
    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.
* Example 2:
    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

"""

from DataStructure import LinkedList, Node


def middleNode(head: Node) -> LinkedList:
    p1 = p2 = head
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
    return p1


ll = LinkedList([1, 2, 3, 4, 5]).display()
print(middleNode(ll.getHead()))

print()

ll = LinkedList([1, 2, 3, 4, 5, 6]).display()
print(middleNode(ll.getHead()))
