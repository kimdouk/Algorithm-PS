from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    localmax = 0

    while queue:
        x, y = queue.popleft()
        localmax += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
            # if graph[nx][ny] ==0 or visited[nx][ny]:
            #     continue
            # visited[nx][ny] = True
            # queue.append((nx,ny))
    return localmax


n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count, finalmax = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            count += 1
            finalmax = max(finalmax, bfs(i,j))
print(count, finalmax, sep='\n')