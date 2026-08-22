class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        for row in range(len(board)):
            if not validRow(row, board):
                return False

        for col in range(len(board[0])):
           if not validCol(col, board):
                return False
        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not validSquare(row, col, board):
                    return False
        
        return True



def validRow(rowNumber: int, board: List[List[str]]) -> bool:

    s = set()
    for i in range(len(board)):
        spot = board[rowNumber][i]
        if spot != "." and spot in s:
            return False
        else:
            s.add(board[rowNumber][i])
    
    return True

def validCol(colNumber: int, board: List[List[str]]) -> bool:

    s = set()
    for i in range(len(board[0])):
        spot = board[i][colNumber]
        if spot != "." and board[i][colNumber] in s:
            return False
        else:
            s.add(board[i][colNumber])
    
    return True

def validSquare(x: int, y: int, board: List[List[str]]) -> bool:

    s = set()
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            spot = board[i][j]
            if spot != "." and spot in s:
                return False
            else:
                s.add(board[i][j])

    return True