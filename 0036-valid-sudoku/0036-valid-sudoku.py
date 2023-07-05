class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=[]
        c=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] not in r:
                        r.append(board[i][j])
                    else:
                        return False
                if board[j][i]!=".":
                    if board[j][i] not in c:
                        c.append(board[j][i])
                    else:
                        return False
            r=[]
            c=[]
        cross3 = {}
        for i in range(3):
            for j in range(3):
                cross3 = {}
                for x in range(i*3, i*3+3):
                    for y in range(j*3, j*3+3):
                        if board[x][y] != '.':
                            if board[x][y] not in cross3:
                                cross3[board[x][y]] = ''
                            else:
                                return False
        return True
        