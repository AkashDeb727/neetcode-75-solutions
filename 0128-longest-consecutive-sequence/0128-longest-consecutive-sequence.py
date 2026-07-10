#Brute Force
# TC -> O(n2) -> while loop
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        nums = set(nums)

        for n in nums:
            current = n
            length = 1

            while current+1 in nums:
                length += 1
                current += 1
            
            longest = max(longest, length)
        
        return longest
'''

#Optimal Approach
# TC -> O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    length += 1

                longest = max(longest, length)

        return longest
                    