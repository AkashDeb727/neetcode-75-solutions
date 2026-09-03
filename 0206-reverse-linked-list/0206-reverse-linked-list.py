# Method: Iterative Approach
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Handle an empty linked list
        if head == None:
            return None

        curr = head
        prev = None

        # Traverse the list and reverse each link
        while curr:
            # Save the next node before changing the pointer
            nextNode = curr.next

            # Reverse the current node's pointer
            curr.next = prev

            # Move prev and curr one step forward
            prev = curr
            curr = nextNode

        # prev is the new head of the reversed linked list
        return prev