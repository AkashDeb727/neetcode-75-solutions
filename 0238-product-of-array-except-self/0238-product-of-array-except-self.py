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



# best solution
# O(n)
# no extra memory space

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]


        suffix = 1
        for i in range(len(nums)-1, -1 , -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res