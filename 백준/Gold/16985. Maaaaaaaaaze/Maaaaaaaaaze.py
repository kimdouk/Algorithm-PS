from itertools import permutations
from collections import deque
import sys

input = sys.stdin.readline
graph = [[list(map(int,input().split())) for _ in range(5)]for _ in range(5)]
board = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
result = float('inf')
dx,dy,dz = [-1,1,0,0,0,0],[0,0,-1,1,0,0],[0,0,0,0,-1,1]

def stack():
    for d in list(permutations(range(5))):
        for i in range(5):
            board[d[i]] = graph[i]
        dfs(0)

def rotate(arr):
    new = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new[j][4-i] = arr[i][j]
    return new

def bfs(board):
    global result
    dist = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    q = deque([(0,0,0)])
    dist[0][0][0]=0
    while q:
        z,x,y = q.popleft()
        if (z,x,y)==(4,4,4):
            result = min(result,dist[4][4][4])
            if result==12:
                print(result)
                sys.exit()
            return
        for i in range(6):
            nx,ny,nz = x+dx[i], y+dy[i], z+dz[i]
            if nx<0 or ny<0 or nz<0 or nx>=5 or ny>=5 or nz>=5:continue
            if dist[nz][nx][ny]==-1 and board[nz][nx][ny]==1:
                dist[nz][nx][ny] = dist[z][x][y]+1
                q.append((nz,nx,ny))
    # return dist[4][4][4]


def dfs(depth):
    global board
    if depth==5:
        if board[4][4][4]:
            bfs(board)
        return
    for i in range(4):
        if board[0][0][0]:
            dfs(depth+1)
        board[depth] = rotate(board[depth])

stack()
print(-1 if result==float('inf') else result)
