class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_len = len(board)

        # checking rows
        for i in range(board_len):
            seen = set()
            for j in board[i]:
                if j == ".":
                    continue
                if j in seen:
                    return False
                else:
                    seen.add(j)
        
        # cheking columns
        for i in range(board_len):
            seen = set()
            for j in range(board_len):
                element = board[j][i]
                if element == ".":
                    continue
                if element in seen:
                    return False
                else:
                    seen.add(element)
        

        # checking rows, we need to create starts array 
        # (top left corners of each sub array)
        starts = [(0,0), (0, 3), (0, 6),
                  (3, 0), (3, 3), (3, 6), 
                  (6, 0), (6, 3), (6, 6)]

        # now loop through them
        for i, j in starts:
            seen = set()
            for col in range(3):
                for col_index in range(3):
                    element = board[col_index + i][col + j]
                    if element == ".":
                        continue
                    if element in seen:
                        return False
                    else:
                        seen.add(element)
        
        return True



        
        

            