"""
! [NOTION] LOCAL RUN FOR LEETCODE SOL SCROLL DOWN
? DataStructure = https://github.com/Omkar02/FAANG_2_0/blob/master/codePatterns/linked_list/DataStructure.py

* Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
* Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]
* Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
"""
from DataStructure import LinkedList, Node


def addTwoNumbers(l1: Node, l2: Node) -> Node:
    dummy_node = cur_node = Node(-1)
    carry = 0
    while l1 or l2:
        val_one = l1.val if l1 else 0
        val_two = l2.val if l2 else 0

        t_sum = (val_one + val_two) + carry
        carry = t_sum // 10
        # print(carry)

        # * SINCE WE ARE GOING FROM START TO END REV ORDER TO THE MATH ALGO
        # * WE NEED TO CALCULATE THE NEXT VAL AS T_SUM % 10
        cur_node.next = Node(t_sum % 10)
        cur_node = cur_node.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry:
        cur_node.next = Node(carry)
    return dummy_node.next


llOne: LinkedList = LinkedList([2, 4, 3]).display("l1 = ")
llTwo: LinkedList = LinkedList([5, 6, 4]).display("l2 = ")
addTwoNumbers(l1=llOne.getHead(), l2=llTwo.getHead()).traverse('\nre = ')
print("-" * 50)

llOne: LinkedList = LinkedList([0]).display("l1 = ")
llTwo: LinkedList = LinkedList([0]).display("l2 = ")
addTwoNumbers(l1=llOne.getHead(), l2=llTwo.getHead()).traverse('\nre = ')
print("-" * 50)

llOne: LinkedList = LinkedList([9, 9, 9, 9, 9, 9, 9]).display("l1 = ")
llTwo: LinkedList = LinkedList([9, 9, 9, 9]).display("l2 = ")
addTwoNumbers(l1=llOne.getHead(), l2=llTwo.getHead()).traverse('\nre = ')
print("-" * 50)
