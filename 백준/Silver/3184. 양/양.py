from collections import deque
n,m = map(int,input().split())
graph = [input() for _ in range(n)]
visited = [[False] * (m) for _ in range(n)] 
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    v,o = 0,0
    visited[x][y] = True
    queue = deque([(x,y)])
    while queue:
        x,y = queue.popleft()
        if graph[x][y]=='v':v+=1
        elif graph[x][y] =='o':o+=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:continue
            if graph[nx][ny] != '#' and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
    return v,o

resultv, resulto = 0,0
for i in range(n):
    for j in range(m):
        if graph[i][j] != '#' and not visited[i][j]:
            v,o = bfs(i,j)
            if v<o:resulto+=o
            elif v>=o:resultv+=v
print(resulto, resultv)