#HashSet
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n):
            if nums[i] > 0:
                break

            elif i > 0 and nums[i] == nums[i-1]:
                continue

            seen = set()

            for j in range(i + 1, n):
                complement = -(nums[i] + nums[j])

                if complement in seen:
                    triplet = tuple(sorted([nums[i], nums[j], complement]))
                    res.add(triplet)
                
                seen.add(nums[j])
            
        return [list(t) for t in res]
'''



#Two Pointer
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            low, high = i+1, n-1

            while low < high:
                sum = nums[i] + nums[low] + nums[high]

                if sum < 0:
                    low +=1
                
                elif sum > 0:
                    high -= 1

                else:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1

                    while low < high and nums[low] == nums[low-1]:
                        low += 1

                    while low < high and nums[high] == nums[high+1]:
                        high -= 1
        
        return res