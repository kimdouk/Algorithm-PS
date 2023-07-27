from collections import deque
input = __import__('sys').stdin.readline
n,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
result = []
def bfs(x,y,temp):
    ret = graph[x][y]
    global result
    temp[x][y] = 1
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=k:continue
            if graph[nx][ny]!=0 and temp[nx][ny]==-1:
                temp[nx][ny] = temp[x][y]+1
                q.append((nx,ny))
    
    idx = []
    mx = 0
    for i in range(n):
        for j in range(k):
            if temp[i][j]>mx:
                mx = temp[i][j]
                idx = [i,j]
    result.append((mx,graph[idx[0]][idx[1]]+ret))

for i in range(n):
    for j in range(k):
        if graph[i][j]!=0:
            bfs(i,j,[[-1 for _ in range(k)] for _ in range(n)])
print(sorted(result)[-1][-1])