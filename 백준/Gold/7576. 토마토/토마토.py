from collections import deque

def bfs():
    queue = deque()
    for redTomato in redTomatoList: #익은 토마토의 좌표를 큐에 넣어줌
        queue.append(redTomato)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:#안익은 토마토일경우
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


m, n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
redTomatoList = [(i,j)for i in range(n) for j in range(m) if graph[i][j]==1]#익은토마토의 좌표 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs()
result = []
for i in range(n):
    for j in range(m):
        result.append(graph[i][j])
print(-1 if 0 in result else max(result)-1) #0이 있으면 토마토가 모두 익지 않은 상황이므로 -1