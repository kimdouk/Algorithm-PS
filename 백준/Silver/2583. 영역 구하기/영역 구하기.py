from collections import deque

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    count = 0

    while queue:
        x, y = queue.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:continue
            if board[nx][ny]==1 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
    return count

#입력부분    
n, m, k = map(int,input().split())
board = [[1]*m for _ in range(n)] #초기 1로 설정하고 직사각형구간을 0으로 받는다.not
visited = [[False]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(k):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(y1,y2): #좌표설정주의
        for j in range(x1,x2):
            board[i][j] = 0 #직사각형 영역은 0

result = []
for i in range(n):
    for j in range(m): #따라서 1인 구간만 bfs돌면 된다.
        if board[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i,j))
print(len(result))
print(*sorted(result), sep=' ')