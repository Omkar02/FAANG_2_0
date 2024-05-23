"""
! [NOTION] LOCAL RUN FOR LEETCODE SOL SCROLL DOWN
? DataStructure = https://github.com/Omkar02/FAANG_2_0/blob/master/codePatterns/linked_list/DataStructure.py

* Example 1:
    Input: head = [1,2,2,1]
    Output: true
* Example 2:
    Input: head = [1,2]
    Output: false
"""
from DataStructure import LinkedList, Node


def isPalindrome(head: Node) -> bool:
    if not head:
        return True

    # * FIND THE MIDDLE OF THE LINKED-LIST
    m1 = m2 = head
    while m2 and m2.next:
        m1 = m1.next
        m2 = m2.next.next

    # * REVERSE THE SECOND PART OF THE LINKED-LIST
    r1, r2 = None, m1
    while r2:
        r3 = r2.next
        r2.next = r1

        r1 = r2
        r2 = r3

    # * COMPARE THE LINKED-LIST FROM BOTH POINTS I.E  "head" AND "r1"
    s1, s2 = head, r1
    while s2:
        if s1.val != s2.val:
            return False
        s1 = s1.next
        s2 = s2.next
    return True


ll = LinkedList([1, 2, 2, 1])
print(isPalindrome(ll.getHead()))

ll = LinkedList([1, 2])
print(isPalindrome(ll.getHead()))
