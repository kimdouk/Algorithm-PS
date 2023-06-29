import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split()))for _ in range(n)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
result=[]
def bfs(x,y):
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True
    q = deque([(x,y)])
    melt = []
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:continue
            if graph[nx][ny]==0 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
            elif graph[nx][ny]==1 and not visited[nx][ny]:
                melt.append((nx,ny))
                visited[nx][ny] =True
    for i,j in melt:
        graph[i][j] = 0
    return melt
cnt = 0
while True:
    result.append(bfs(0,0))
    if len(result[-1])==0:break
    cnt+=1
print(cnt, len(result[-2]),sep='\n')