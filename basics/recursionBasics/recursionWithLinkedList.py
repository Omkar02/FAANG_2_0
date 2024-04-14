import os

os.system('clear')
depthNumber = [0]

def final(res):
    depthNumber[0] = 0
    print(f'Final result = {res}')
    print('-' * 100 + '\n')
# -------------------------| Code |---------------------------------------- 
class Node:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.nextNode = nextNode

class LinkedList:
    def __init__(self):
        self.head = None
        self.curNode = None
    
    def insert(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.curNode = self.head
            return
        self.curNode.nextNode = newNode
        self.curNode = self.curNode.nextNode

    def __str__(self) -> str:
        curNode = self.head
        res = ''
        while curNode:
            res += f'{curNode.val} -> '
            curNode = curNode.nextNode
        res += 'None'
        return res

def reverse_linked_list(node):
    def _reverse_recurcive(p1, p2):
        if not p2: return p1

        p3 = p2.nextNode
        p2.nextNode = p1

        return _reverse_recurcive(p2, p3)
    return _reverse_recurcive(None, node)


l = LinkedList()
[l.insert(x) for x in range(1, 11)]

print(l)
l.head = reverse_linked_list(l.head)
print(l)