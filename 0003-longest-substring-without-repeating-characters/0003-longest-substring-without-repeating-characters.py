class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        charSet = set()

        for r in range(len(s)):

            # Shrink the window until the duplicate is removed
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            # Add the current character to the window
            charSet.add(s[r])

            # Update the maximum length
            currLen = len(charSet)
            maxLen = max(currLen, maxLen) # maxLen = max(maxLen, r - l + 1)

        return maxLen