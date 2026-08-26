# Time: O(n)
# Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0 
        right = len(height) - 1
        curArea = 0
        maxArea = 0

        while left < right:
            # Area = width × shorter wall
            curArea = (right - left) * min(height[left], height[right])
            maxArea = max(curArea, maxArea)

            if height[left] < height[right]:
                left += 1
            else: 
                # Move the right pointer when the right wall is shorter or equal
                right -= 1

        return maxArea