from collections import deque
def bfs(x,y):
    queue = deque([(x,y)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:continue
            if graph[nx][ny]==graph[x][y] and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True

n = int(input())
graph = [list(input()) for _ in range(n)]
visited= [[False] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result_X, result_O = 0, 0

#이렇게 푸는게 최선인지는 모르겠다.순서에따라 하드코딩한느낌?아닌가,,
for i in range(n): #적록색약아닐때
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            result_X += 1

visited= [[False] * n for _ in range(n)] #방문 초기화
for i in range(n): #적록색약일때 G를 R로 치환
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n): #적록색약일때
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            result_O += 1
print(result_X, result_O) #적록색약아닐떄, 적록색약일때