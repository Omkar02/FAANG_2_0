"""
! [NOTION] LOCAL RUN FOR LEETCODE SOL SCROLL DOWN
? DataStructure = https://github.com/Omkar02/FAANG_2_0/blob/master/codePatterns/linked_list/DataStructure.py

* Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]
* Example 2:
    Input: head = [0,1,2], k = 4
    Output: [2,0,1]

"""
from DataStructure import LinkedList, Node


def rotateRight(head: Node, k: int) -> Node:
    end_node = head
    length = 1
    # * get the length of the list and the last node in the list
    while end_node.next:
        end_node = end_node.next
        length += 1

    # * Set the last node to point to head node
    # * The list is now a circular linked list with last node pointing to first node
    end_node.next = head

    # * If k is equal to the length of the list then k == 0
    # *  ElIf k is greater than the length of the list then k = k % length
    k = k % length

    # * Traverse the list to get to the node just before the ( length - k )th node.
    # * Example: In 1 -> 2 -> 3 -> 4 -> 5, and k = 2
    # *          we need to get to the Node(3)
    temp_node = head
    for _ in range(length - k - 1):
        temp_node = temp_node.next

    # * Get the next node from the tempNode and then set the tempNode.next as None
    # * Example: In 1 -> 2 -> 3 -> 4 -> 5, and k = 2
    # *          tempNode = Node(3)
    # *          answer = Node(3).next => Node(4)
    # *          Node(3).next = None ( cut the linked list from here )
    res = temp_node.next
    temp_node.next = None

    return res


ll: LinkedList = LinkedList([1, 2, 3, 4, 5]).display()
rotateRight(head=ll.getHead(), k=2).traverse()
print("-" * 50)

ll: LinkedList = LinkedList([0, 1, 2]).display()
rotateRight(head=ll.getHead(), k=4).traverse()
print("-" * 50)
