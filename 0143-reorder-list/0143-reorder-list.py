# O(n) Time | O(1) Space
class Solution: 
    def reorderList(self, head: Optional[ListNode]) -> None: 
        
        # Edge case: empty list or list with only one node
        if not head or not head.next: 
            return 
 
        # --------------------------------------------------
        # 1. Find the middle of the linked list
        # --------------------------------------------------
        slow = head 
        fast = head 
 
        # slow moves 1 step, fast moves 2 steps
        # When fast reaches the end, slow is at the middle
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
 
        # --------------------------------------------------
        # 2. Reverse the second half of the linked list
        # --------------------------------------------------
        prev = None 
        curr = slow 
 
        while curr: 
            nextNode = curr.next  # Save the next node
            curr.next = prev      # Reverse the pointer
            prev = curr           # Move prev forward
            curr = nextNode       # Move curr forward
 
        # --------------------------------------------------
        # 3. Merge the first half and reversed second half
        # --------------------------------------------------
        first = head 
        second = prev 
 
        # Connect nodes alternately from both halves
        while second.next: 
            firstNext = first.next    # Save next node of first half
            secondNext = second.next  # Save next node of second half
 
            first.next = second       # First → Second
            second.next = firstNext   # Second → Next First
 
            first = firstNext         # Move first forward
            second = secondNext       # Move second forward