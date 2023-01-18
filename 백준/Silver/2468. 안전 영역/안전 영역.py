from collections import deque

def bfs(x,y,rain,visited):#시작좌표(x,y), 물의높이, 방문정보
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny < 0 or ny>=n or nx>=n: continue
            if graph[nx][ny]>rain and not visited[nx][ny]: #물의 높이보다 높고(안전하고) 방문안한 좌표
                queue.append((nx,ny))
                visited[nx][ny] = True

n = int(input())
graph = []
maxRow = []
for i in range(n):
    row = list(map(int,input().split()))
    graph.append(row)
    maxRow.append(max(row)) #최대높이를 얻기 위해 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

resultList = []
for rain in range(max(maxRow)):
    result = 0
    visited = [[False] * n for _ in range(n)] # 물의 높이만큼 반복해야하기 때문에 방문정보 초기화(코드위치 중요)
    for j in range(n):
        for k in range(n):
            if graph[j][k]>rain and not visited[j][k]: #물의높이보다 높고(안전하고) 방문언헌 좌표이면
                bfs(j,k,rain,visited)#bfs돌린다.
                result += 1#result는 물에 잠기지 않는 안전한 영역
    resultList.append(result)
print(max(resultList))#물에 잠기지 않는 안전한 영역의 최대 개수