"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToNew = {None : None}

        # create clone nodes in dictionary
        ptr = head
        while ptr:
            oldToNew[ptr] = Node(ptr.val)
            ptr = ptr.next

        # assign next and random pointers
        ptr = head
        while ptr:
            oldToNew[ptr].next = oldToNew[ptr.next]
            oldToNew[ptr].random = oldToNew[ptr.random]
            ptr = ptr.next
        
        return oldToNew[head]
        