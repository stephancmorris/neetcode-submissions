class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = [0] * 9
        col_seen = [0] * 9
        square_seen = [0] * 9
        # create 9 masks per box, col, and row

        for row in range(9):
            for col in range(9):
                cell = board[row][col] 
                if cell == ".":
                    continue 
                

                bit = 1 << (int(cell) - 1)
                box = (row // 3) * 3 + (col // 3) #maps row and col to box indx

                if bit & row_seen[row]:
                    return False
                if bit & col_seen[col]:
                    return False
                if bit & square_seen[box]:
                    return False

                row_seen[row] |= bit
                col_seen[col] |= bit
                square_seen[box] |= bit
        return True

