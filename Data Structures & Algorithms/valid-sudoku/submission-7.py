class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we know this is 9 but it makes more sense for me to do this way
        board_len = len(board) 

        # checking all rows:
        for row in board:
            seen = set()
            for element in row:
                if element == ".":
                    continue
                if element in seen:
                    return False
                else:
                    seen.add(element)
        
        # checking all columns:
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

        # make an array of all top left indices
        starts = [(0, 0), (0, 3), (0, 6), 
                  (3, 0), (3, 3), (3, 6), 
                  (6, 0), (6, 3), (6, 6)]
        
        for i, j in starts:
            seen = set()
            for row in range(i, i + 3):
                for col in range(j, j+ 3):
                    element = board[row][col]

                    if element == ".":
                        continue
                    if element in seen:
                        return False
                    else:
                        seen.add(element)
        
        return True


        
        

            