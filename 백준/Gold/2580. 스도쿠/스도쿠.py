import sys

def rowCheck(r,num):
    for c in range(9):
        if board[r][c] == num:return False
    return True

def colCheck(c,num):
    for r in range(9):
        if board[r][c] == num:return False
    return True

def squareCheck(r,c,num):
    nr = (r//3)*3
    nc = (c//3)*3
    for i in range(nr,nr+3):
        for j in range(nc,nc+3):
            if board[i][j] == num:return False
    return True

def dfs(depth):
    if depth == len(zero):
        for i in range(9):
            print(*board[i],end='\n')
        sys.exit()
    
    x,y = zero[depth]
    for i in range(1,10):
        if rowCheck(x,i) and colCheck(y,i) and squareCheck(x,y,i):
            board[x][y] = i
            dfs(depth+1)
            board[x][y] = 0

board = [list(map(int,input().split())) for _ in range(9)]
zero = [(i,j) for i in range(9) for j in range(9) if not board[i][j]]
dfs(0)