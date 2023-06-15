from collections import deque
import sys

def move():
    flag = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                isPos = bfs(i,j)
                if isPos>1:
                    flag = 1
    return flag

def bfs(x,y):
    visited[x][y] = True
    q = deque([(x,y)])
    result = [(x,y)]
    total = graph[x][y]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:continue
            if not visited[nx][ny] and l<=abs(graph[nx][ny] - graph[x][y])<=r:
                q.append((nx,ny))
                visited[nx][ny] = True
                total +=graph[nx][ny]
                result.append((nx,ny))
    for i,j in result:
        graph[i][j] = total//len(result)
    return len(result)
    

input = sys.stdin.readline
n,l,r = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
dx, dy = [-1,1,0,0], [0,0,-1,1]
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    if not move():
        break
    cnt+=1
print(cnt)