# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Dummy node simplifies building the result list
        dummy = ListNode()
        current = dummy
        carry = 0

        # Continue until both lists and the carry are exhausted
        while l1 or l2 or carry:

            # Get the current digit from each list
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            total = value1 + value2 + carry

            # Calculate the digit and carry for the next position
            carry = total // 10    # 50 // 10 gives 5
            digit = total % 10     # 50 // 10 gives 0

            # Add the digit to the result list
            current.next = ListNode(digit)
            current = current.next

            # Move to the next nodes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next