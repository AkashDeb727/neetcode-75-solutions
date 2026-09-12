class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Store numbers already seen in each row, column, and 3x3 box
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)  # key = (row // 3, col // 3)

        # Visit every cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # Ignore empty cells
                if val == ".":
                    continue

                # Identify which 3x3 box this cell belongs to
                box_id = (r // 3, c // 3)

                # If the value already exists in the same row, column, or box,
                # the Sudoku board is invalid
                if (val in rows[r] or
                    val in cols[c] or
                    val in boxes[box_id]):
                    return False

                # Add the value to the corresponding row, column, and box
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_id].add(val)

        # No duplicates were found, so the board is valid
        return True


'''
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]

for this we would hav to use this: 
    box_id = (r // 3) * 3 + (c // 3)

'''