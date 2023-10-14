from collections import deque
input = __import__('sys').stdin.readline
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx,dy = [-1,1,0,0,-1,-1,1,1], [0,0,-1,1,-1,1,-1,1]
def bfs(x,y):
    flag = True
    visited[x][y] = True
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:continue
            if graph[nx][ny]>graph[x][y]:
                flag = False
            if graph[nx][ny]!=0 and not visited[nx][ny] and graph[nx][ny] == graph[x][y] :
                q.append((nx,ny))
                visited[nx][ny] = True
    return flag
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]!=0 and not visited[i][j]:
            if bfs(i,j):
                cnt+=1
print(cnt)