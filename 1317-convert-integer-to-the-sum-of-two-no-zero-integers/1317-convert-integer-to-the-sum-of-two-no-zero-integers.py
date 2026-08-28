class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i = 1
        j = n - i

        # Keep trying pairs whose sum is always n
        while '0' in str(i) or '0' in str(j):

            # Move to the next pair
            i += 1
            j -= 1

        # Both numbers contain no zero
        return [i, j]