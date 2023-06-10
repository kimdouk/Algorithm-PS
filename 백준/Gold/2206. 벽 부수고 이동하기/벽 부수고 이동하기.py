from collections import deque
import sys

def bfs(x,y,broke):
    visited[x][y][broke] = 1
    q = deque()
    q.append((x,y,broke))
    while q:
        x,y,z = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:continue
            if graph[nx][ny] == 1 and z==0:
                visited[nx][ny][1] = visited[x][y][z]+1
                q.append((nx,ny,1))
            elif graph[nx][ny] ==0 and not visited[nx][ny][z]:
                visited[nx][ny][z] = visited[x][y][z]+1
                q.append((nx,ny,z))

input = sys.stdin.readline
n,m = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]
visited = [[[0,0] for _ in range(m)] for _ in range(n)]
dx,dy = [0,0,-1,1],[-1,1,0,0]

bfs(0,0,0)

if 0 in visited[n-1][m-1]:
    if max(visited[n-1][m-1])==0:print(-1)
    else:print(max(visited[n-1][m-1]))
else:print(min(visited[n-1][m-1]))