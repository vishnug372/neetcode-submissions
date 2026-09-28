class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True
        arr = [set() for _ in range(9)]
        for i in range(len(board)):
            row = set()
            col = set()
            for j in range(len(board[i])):
                subIdx = (i//3) * 3 + (j//3)
                if board[i][j] in row:
                    return False
                if board[j][i] in col:
                    return False 
                if board[i][j] in arr[subIdx]:
                    return False
                if board[i][j] != ".":
                    row.add(board[i][j])
                if board[j][i] != ".":
                    col.add(board[j][i])
                if board[i][j] != ".":
                    arr[subIdx].add(board[i][j])
                
        
        
                
        return True





