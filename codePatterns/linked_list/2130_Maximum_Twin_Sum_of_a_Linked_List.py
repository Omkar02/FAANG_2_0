"""
! [NOTION] LOCAL RUN FOR LEETCODE SOL SCROLL DOWN
? DataStructure = https://github.com/Omkar02/FAANG_2_0/blob/master/codePatterns/linked_list/DataStructure.py


* Example 1:
    Input: head = [5,4,2,1]
    Output: 6
    Explanation:
        Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
        There are no other nodes with twins in the linked list.
        Thus, the maximum twin sum of the linked list is 6. 
* Example 2:
    Input: head = [4,2,2,3]
    Output: 7
    Explanation:
        The nodes with twins present in this linked list are:
        - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
        - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
        Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
* Example 3:
    Input: head = [1,100000]
    Output: 100001
    Explanation:
        There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
"""


from DataStructure import LinkedList, Node


def pairSum(head: Node) -> int:
    # * FIND THE MIDDLE OF THE THE LINKED LIST
    m1 = m2 = head
    while m2 and m2.next:
        m2 = m2.next.next
        m1 = m1.next

    # * REVERSE THE SECOND HALF I.E FROM M1
    r1, r2 = None, m1
    while r2:
        r3 = r2.next
        r2.next = r1

        r1 = r2
        r2 = r3
    # * CALCULATE THE OF HEAD(N) + R1(N)
    max_val = float("-inf")
    p1, p2 = head, r1
    while p2:
        one = p1.val
        two = p2.val

        max_val = max(max_val, one + two)
        p1 = p1.next
        p2 = p2.next

    return max_val


ll: LinkedList = LinkedList([5, 4, 2, 1]).display()
print(pairSum(ll.getHead()))
print("-"*50)

ll: LinkedList = LinkedList([4, 2, 2, 3]).display()
print(pairSum(ll.getHead()))
print("-"*50)

ll: LinkedList = LinkedList([1, 100000]).display()
print(pairSum(ll.getHead()))
print("-"*50)
