# Time Complexity: O(n)
# Space Complexity: O(n)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        res = []

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for j in range(n - 2, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j + 1]

        for i in range(n):
            res.append(prefix[i] * suffix[i])

        return res
'''


# Space Complexity: O(1)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        suffix_product = 1

        for i in range(1,n):
            res[i] *= res[i-1] * nums[i-1]
        
        for j in range(n - 1, -1, -1):
            res[j] *= suffix_product
            suffix_product *= nums[j]

        return res
'''

#Same but easy to understand

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        suffix = 1

        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        for j in range(n-1,-1,- 1):
            res[j] *= suffix
            suffix *= nums[j]

        return res
