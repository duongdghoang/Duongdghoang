class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        count = {}
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                count[board[i][j]] = count.get(board[i][j],0) + 1
                if count[board[i][j]] > 1:
                    return False
            count.clear()
        for j in range(9):
            for i in range(9):
                if board[i][j] == ".":
                    continue
                count[board[i][j]] = count.get(board[i][j],0) + 1
                if count[board[i][j]] > 1:
                    return False
            count.clear()
        for a in range(0,9,3):
            for b in range(0,9,3):
                for i in range(a,a+3):
                    for j in range(b,b+3):
                        if board[i][j] == ".":
                            continue
                        count[board[i][j]] = count.get(board[i][j],0) + 1
                        if count[board[i][j]] > 1:
                            return False
                count.clear()
        return True     



            
                
                