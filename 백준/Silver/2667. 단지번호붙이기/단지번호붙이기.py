from collections import deque

def bfs(x,y):
    size = 0
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        size += 1
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
    return size

n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i,j))
result.sort()
print(len(result), *result ,sep='\n')