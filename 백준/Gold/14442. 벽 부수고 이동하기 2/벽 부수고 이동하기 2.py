import sys
from collections import deque

def bfs(x,y,z):
    visited[x][y][z] = 1
    q = deque([(x,y,z)])
    while q:
        x,y,z = q.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:continue
            if graph[nx][ny] ==1 and z<k and not visited[nx][ny][z+1]:
                visited[nx][ny][z+1] = visited[x][y][z]+1
                q.append((nx,ny,z+1))
            elif graph[nx][ny] ==0 and not visited[nx][ny][z]:
                visited[nx][ny][z] = visited[x][y][z]+1
                q.append((nx,ny,z))
    return -1

input = sys.stdin.readline
n,m,k = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]
visited = [[[0 for _ in range(k+1)]for _ in range(m)]for _ in range(n)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
print(bfs(0, 0, 0))