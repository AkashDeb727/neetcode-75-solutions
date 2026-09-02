# Solution 1: HashMap + Fixed-Size Sliding Window
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # A permutation of s1 cannot exist if s1 is longer than s2
        if len(s1) > len(s2):
            return False

        s1Count = {}  # Store the character frequencies of s1
        window = {}   # Store the character frequencies of the current sliding window

        for char in s1:
            s1Count[char] = s1Count.get(char, 0) + 1

        l = 0
        for r in range(len(s2)):
            # Add the current character to the window
            window[s2[r]] = window.get(s2[r], 0) + 1

            if (r - l + 1) > len(s1):  # Shrink the window if it becomes larger than s1
        
                window[s2[l]] -= 1   # Remove the leftmost character from the window

                # Remove the character completely if its frequency becomes 0
                if window[s2[l]] == 0: 
                    del window[s2[l]]

                l += 1

            if window == s1Count:
                return True

        return False
'''



# Solution 2: Frequency Array + Fixed-Size Sliding Window
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        windowCount = [0] * 26

        for char in s1:
            idx = ord(char) - ord('a')
            s1Count[idx] += 1

        
        l = 0
        for r in range(len(s2)):
            idx = ord(s2[r]) - ord('a')
            windowCount[idx] += 1

            if r - l + 1 > len(s1):
                idx = ord(s2[l]) - ord('a')
                windowCount[idx] -= 1
                l += 1

            if windowCount == s1Count:
                return True
    
        return False
'''



# Solution 3: Frequency Arrays + Matches Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26   
        windowCount = [0] * 26  # Store character frequencies of the current window in s2

        for char in s1:
            idx = ord(char) - ord('a')
            s1Count[idx] += 1

        for char in range(len(s1)): # Build the first window of size len(s1)
            idx = ord(s2[char]) - ord('a')
            windowCount[idx] += 1

        # Count how many of the 26 character frequencies currently match
        matches = 0
        for i in range(26):  
            if s1Count[i] == windowCount[i]:
                matches += 1


        l = 0
        # Start after the first window since its characters have already been counted
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True


            # Add the new character entering from the right
            rightIdx = ord(s2[r]) - ord('a')
            windowCount[rightIdx] += 1

            if windowCount[rightIdx] == s1Count[rightIdx]:
                matches += 1
            elif windowCount[rightIdx] == s1Count[rightIdx] + 1:
                matches -= 1
            


            # Remove the character leaving from the left
            leftIdx= ord(s2[l]) - ord('a')
            windowCount[leftIdx] -= 1

            if windowCount[leftIdx] == s1Count[leftIdx]:
                matches += 1
            elif windowCount[leftIdx] == s1Count[leftIdx] - 1:
                matches -= 1

            l += 1

        return matches == 26
