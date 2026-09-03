# Definition for singly-linked list. 
# class ListNode: 
#     def __init__(self, val=0, next=None): 
#         self.val = val 
#         self.next = next 


class Solution: 
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
 
        # Dummy node helps us keep track of the head of the merged list
        dummy = ListNode() 
        curr = dummy 
 
        # Compare nodes from both lists until one list is exhausted
        while list1 and list2: 
 
            # Attach the smaller node to the merged list
            if list1.val <= list2.val: 
                curr.next = list1 
                list1 = list1.next 
 
            else: 
                curr.next = list2 
                list2 = list2.next 
 
            # Move curr forward to the newly added node
            curr = curr.next 
 
        # Attach all remaining nodes from the non-empty list
        curr.next = list1 if list1 else list2 
         
        # Return the actual head, skipping the dummy node
        return dummy.next