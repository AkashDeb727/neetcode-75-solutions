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
        if not head:
            return None
        
        # Maps each original node to its copied node
        oldToCopy = {None : None}


        # First pass: Create a copy of every node
        curr = head
        while curr:
            copy = Node(curr.val)
            
            oldToCopy[curr] = copy
            
            curr = curr.next



        # Second pass: Connect next and random pointers
        curr = head
        while curr:
            copy = oldToCopy[curr]

            # Point to the copied versions of the original pointers
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]

            curr = curr.next


        # Return the copied version of the original head
        return oldToCopy[head]