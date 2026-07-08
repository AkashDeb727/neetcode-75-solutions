# Brute Force Method O(n2)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
"""



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement not in hash_map:
                hash_map[nums[i]] = i
            
            else:
                return [hash_map[complement], i]
