class Solution: 
    def characterReplacement(self, s: str, k: int) -> int: 
        l = 0
        maxLen = 0
        charCount = {}  # Stores the frequency of each character in the current window
 
        for r in range(len(s)): 
            # Add the current character to the window
            charCount[s[r]] = charCount.get(s[r], 0) + 1
            
            # Calculate the current window length
            windowLen = r - l + 1
 
            # Shrink the window if more than k replacements are needed
            while windowLen - max(charCount.values()) > k: 
                # Remove the leftmost character from the window
                charCount[s[l]] -= 1 
                l += 1
                
                # Update the window length after shrinking
                windowLen = r - l + 1
 
 
            # Update the maximum valid window length
            maxLen = max(windowLen, maxLen) 
         
        return maxLen