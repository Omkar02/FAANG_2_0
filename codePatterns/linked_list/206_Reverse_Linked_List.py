"""
?DataStructure = https://github.com/Omkar02/FAANG_2_0/blob/master/codePatterns/linked_list/DataStructure.py

* Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
* Example 2:
    Input: head = [1,2]
    Output: [2,1]
* Example 3:
    Input: head = []
    Output: []
"""


from DataStructure import LinkedList, Node


def reverseList(head: LinkedList) -> Node:
    p1, p2 = None, head.getHead()
    while p2:
        p3 = p2.next
        p2.next = p1

        p1 = p2
        p2 = p3
        print()
        print("\t p1 = ", p1)
        print("\t p2 = ", p2)
        print("\t p3 = ", p3)

    head.setHead(p1)


ll = LinkedList([1, 2, 3, 4, 5]).display()
reverseList(ll)
ll.display()
print("-" * 40)

ll = LinkedList([1, 2]).display()
reverseList(ll)
ll.display()
print("-" * 40)

ll = LinkedList([]).display()
reverseList(ll)
ll.display()
