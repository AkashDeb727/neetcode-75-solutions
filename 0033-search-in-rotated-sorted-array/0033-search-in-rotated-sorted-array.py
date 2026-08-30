class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # Search while there is at least one element left
        while l <= r:
            mid = (l + r) // 2

            # If middle element is the target, return its index
            if nums[mid] == target:
                return mid

            # If left half is sorted
            if nums[l] <= nums[mid]:

                # Target lies inside the sorted left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    # Target must be in the right half
                    l = mid + 1

            # Otherwise, right half is sorted
            else:

                # Target lies inside the sorted right half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    # Target must be in the left half
                    r = mid - 1

        # Target was not found
        return -1