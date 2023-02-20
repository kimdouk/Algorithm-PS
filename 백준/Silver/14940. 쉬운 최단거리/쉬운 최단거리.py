from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            x,y = i,j
        if graph[i][j] ==1:
            graph[i][j] = -1
def bfs(x,y):
    queue = deque([(x,y)])
    graph[x][y] =0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:continue
            if graph[nx][ny]==-1 and not visited[nx][ny]:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
                visited[nx][ny] = True

bfs(x,y)
for i in range(n):
    print(*graph[i])