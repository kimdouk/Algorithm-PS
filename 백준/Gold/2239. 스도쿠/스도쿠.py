import sys

def rowCheck(r,num):
    for j in range(9):
        if board[r][j]==num:
            return False
    return True

def colCheck(c,num):
    for i in range(9):
        if board[i][c] ==num:
            return False
    return True

def squareCheck(r,c,num):
    nr,nc = (r//3)*3, (c//3)*3
    for i in range(3):
        for j in range(3):
            if board[nr+i][nc+j]==num:
                return False
    return True

def dfs(depth):
    if depth == len(zero):
        for i in range(9):
            print(*board[i],sep='',end='\n')
        sys.exit()

    r,c = zero[depth]
    for i in range(1,10):
        if rowCheck(r,i) and colCheck(c,i) and squareCheck(r,c,i):
            board[r][c] = i
            dfs(depth+1)
            board[r][c] = 0

board = [list(map(int,input())) for _ in range(9)]
zero = [(i,j) for i in range(9) for j in range(9) if not board[i][j]]
dfs(0)