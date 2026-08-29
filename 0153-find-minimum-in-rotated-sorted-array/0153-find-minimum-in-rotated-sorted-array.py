'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                return min(res,nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            
            elif nums[mid] < nums[l]:
                r = mid - 1

        return res
'''



class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1 # the minimum must be to the right of mid so thts y mid + 1
 
            elif nums[mid] < nums[r]:
                r = mid # mid could itself be the minimum so we cant do mid - 1

        # l == r, so this is the minimum element
        return nums[r]