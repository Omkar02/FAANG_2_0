"""
! [NOTION] LOCAL RUN FOR LEETCODE SOL SCROLL DOWN
? DataStructure = https://github.com/Omkar02/FAANG_2_0/blob/master/codePatterns/linked_list/DataStructure.py

* Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
* Example 2:
    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
* Example 3:
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.
"""
from DataStructure import LinkedList, Node


def hasCycle(head: Node) -> bool:
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
    return False


ll: LinkedList = LinkedList([3, 2, 0, -4]).display()
ll.insertLoop(loopNodeVal=2)
print(hasCycle(ll.getHead()))

print("-" * 50)

ll: LinkedList = LinkedList([1, 2]).display()
ll.insertLoop(loopNodeVal=1)
print(hasCycle(ll.getHead()))

print("-" * 50)

ll: LinkedList = LinkedList([1]).display()
ll.insertLoop(loopNodeVal=-1)
print(hasCycle(ll.getHead()))
