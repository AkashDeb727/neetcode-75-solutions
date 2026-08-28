class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i = 1
        while i < n+1:
            j = n - i

            while '0' in str(i) or '0' in str(j):
                i += 1
                j -= 1
            
            if i+j == n:
                return [i, j]
                
        