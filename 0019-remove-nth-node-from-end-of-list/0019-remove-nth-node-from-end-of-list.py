
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Dummy node handles the case where the head needs to be removed.
        dummy = ListNode(0, head)

        left = dummy
        right = head

        # Move right pointer n steps ahead.
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both pointers until right reaches the end.
        # left will stop just before the node to remove.
        while right:
            left = left.next
            right = right.next

        # Skip the node that needs to be removed.
        left.next = left.next.next

        return dummy.next
