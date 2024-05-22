"""
?DataStructure = https://github.com/Omkar02/FAANG_2_0/blob/master/codePatterns/linked_list/DataStructure.py

* Example 1:
    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]
    Explanation: You are given the second node with value 5, 
        the linked list should become 4 -> 1 -> 9 after calling your function.
* Example 2:
    Input: head = [4,5,1,9], node = 1
    Output: [4,5,9]
    Explanation: You are given the third node with value 1, the 
        linked list should become 4 -> 5 -> 9 after calling your function.
"""
from DataStructure import LinkedList, Node


def deleteNode(node: Node):
    node.val = node.next.val
    node.next = node.next.next


head = [4, 5, 1, 9]
node = 5
ll = LinkedList(head).display()
deleteNode(ll.getNodeWithVal(node))
ll.display()

print()
head = [4, 5, 1, 9]
node = 1
ll = LinkedList(head).display()
deleteNode(ll.getNodeWithVal(node))
ll.display()
