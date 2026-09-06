# KEY IDEA: 
# Treat the array like a linked list:
# each value points to the next index.
# The duplicate value creates a cycle.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        # Phase 1: Find a meeting point inside the cycle
        while True:
            slow = nums[slow]             # Move 1 step
            fast = nums[nums[fast]]       # Move 2 steps

            if slow == fast:
                break


        # Phase 2: Find the entrance of the cycle (the duplicate)
        slow = 0
        while True:
            slow = nums[slow]             # Move both pointers 1 step
            fast = nums[fast]

            if slow == fast:
                break

        return slow