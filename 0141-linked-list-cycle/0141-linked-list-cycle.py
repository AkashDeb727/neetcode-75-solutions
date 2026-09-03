# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# Floyd's Cycle Detection Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Initialize both pointers at the head
        slow = head
        fast = head

        # Continue while the fast pointer can move two steps
        while fast and fast.next:

            # Move slow pointer one step
            slow = slow.next

            # Move fast pointer two steps
            fast = fast.next.next

            # If both pointers meet, a cycle exists
            if slow == fast:
                return True

        # Fast pointer reached the end, so there is no cycle
        return False