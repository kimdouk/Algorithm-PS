import sys
from copy import deepcopy
input = sys.stdin.readline

def up(board):
    for j in range(n):
        pointer = 0
        for i in range(1,n):
            if board[i][j]!=0:
                tmp = board[i][j]
                board[i][j] = 0
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                elif board[pointer][j] == tmp:
                    board[pointer][j]*=2
                    pointer+=1
                else:
                    pointer+=1
                    board[pointer][j] = tmp # 하아 ..
    return board

def down(board):
    for j in range(n):
        pointer = n-1
        for i in range(n-2,-1,-1):
            if board[i][j]!=0:
                tmp = board[i][j]
                board[i][j] = 0
                if board[pointer][j] ==0:
                    board[pointer][j] = tmp
                elif board[pointer][j] == tmp:
                    board[pointer][j]*=2
                    pointer-=1
                else:
                    pointer-=1
                    board[pointer][j] = tmp
    return board

def left(board):
    for i in range(n):
        pointer = 0
        for j in range(1,n):
            if board[i][j]!=0:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] ==0:
                    board[i][pointer] = tmp
                elif board[i][pointer] == tmp:
                    board[i][pointer]*=2
                    pointer+=1
                else:
                    pointer+=1
                    board[i][pointer] = tmp
    return board

def right(board):
    for i in range(n):
        pointer = n-1
        for j in range(n-2,-1,-1):
            if board[i][j]!=0:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] ==0:
                    board[i][pointer] = tmp
                elif board[i][pointer] == tmp:
                    board[i][pointer]*=2
                    pointer-=1
                else:
                    pointer-=1
                    board[i][pointer] = tmp
    return board

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
result = 0

def dfs(board,cnt):
    global result
    if cnt==5:
        result = max(result,(max(list(map(max,board)))))
        return
    for i in range(4):
        copy_board = deepcopy(board)
        if i==0:dfs(up(copy_board),cnt+1)
        elif i==1:dfs(right(copy_board),cnt+1)
        elif i==2:dfs(down(copy_board),cnt+1)
        else: dfs(left(copy_board),cnt+1)

dfs(board,0)
print(result)