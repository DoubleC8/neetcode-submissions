class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # checking row by row
        for row in board:
            seen_elements = set()
            print("row: ", row)
            for i in range(len(row)):
                if row[i] == ".":
                    continue
                if row[i] in seen_elements:
                    return False
                else:
                    seen_elements.add(row[i])
        
        # checking col by col
        for i in range(len(board)):
            seen_elements = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen_elements:
                    return False
                else: 
                    seen_elements.add(board[j][i])
        
        # checking 3x3 sub array
        for i in range(len(board)):
            box_row = (i // 3) * 3
            box_col = (i % 3) * 3
            seen_elements = set()
            for r in range(3):
                for c in range(3):
                    if board[box_row + r][box_col + c] == ".":
                        continue
                    if board[box_row + r][box_col + c] in seen_elements:
                        return False
                    else: 
                        seen_elements.add(board[box_row + r][box_col + c] )

        return True

        
        

            