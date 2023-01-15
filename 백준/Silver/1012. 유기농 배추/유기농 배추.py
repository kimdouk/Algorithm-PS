from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True

#고정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#입력받는 부분
n = int(input())
for _ in range(n):
    m, n, k = map(int,input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int,input().split()) #입력받는 좌표주의
        graph[x][y] = 1
    
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                result += 1
                bfs(i,j)
    print(result)