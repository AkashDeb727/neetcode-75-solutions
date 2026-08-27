# Two Binary Searches: first search for the correct row, then search within that row

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])


# STEP 1: Find the row where target could exist

        top = 0
        bottom = rows - 1

        while top <= bottom:

            # Find the middle row
            row = (top + bottom) // 2

            # Target is smaller than the first element of this row
            # search rows above
            if target < matrix[row][0]:
                bottom = row - 1


            # Target is bigger than the last element of this row 
            # search rows below
            elif target > matrix[row][-1]:
                top = row + 1
            

            # Target could lie in the middle row
            else:
                break
        
        
# STEP 2: Binary search inside the selected row

        row = (top + bottom) // 2
        left = 0
        right = cols - 1

        while left <= right:
            mid = (left + right) // 2

            if target == matrix[row][mid]:
                return True

            elif target < matrix[row][mid]:
                right = mid - 1

            elif target > matrix[row][mid]:
                left = mid + 1
        
        return False



# One Binary Search: treat the 2D matrix as a flattened 1D sorted array
# main thing is row = mid // n and col = mid % n
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            # Convert the 1D index into row and column
            row = mid // n
            col = mid % n

            if target == matrix[row][col]:
                return True

            elif target < matrix[row][col]:
                right = mid - 1

            elif target > matrix[row][col]:
                left = mid + 1
        
        return False
'''
