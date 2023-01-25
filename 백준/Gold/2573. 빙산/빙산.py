from collections import deque
import sys

def bfs(x,y): #빙산 덩어리 확인을 위한 bfs
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:continue
            if graph[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
meltingYear = 0 #빙산이 분리되는 최초의 시간(년)

while True:
    meltIndexList = [[i,j] for i in range(n) for j in range(m) if graph[i][j] !=0]#빙산이 존재하는 인덱스 모음
    meltingHeight = [[0] * m for _ in range(n)]#녹일 빙산의 높이(나중에 한번에 녹이기 위함)
    if len(meltIndexList) ==0:#두 덩어리 이상으로 분리되지 않으면
        print(0) #0을 print
        break
    for meltIndex in meltIndexList:
        for i in range(4):#빙산주변(상하좌우)의 0의 개수를 meltingHeight에 저장
            nx = meltIndex[0] + dx[i]
            ny = meltIndex[1] + dy[i]
            if graph[nx][ny] == 0:
                meltingHeight[meltIndex[0]][meltIndex[1]] += 1
    for meltIndex in meltIndexList:#녹일 빙산의 높이(meltingHeight) 만큼 녹여준다.
        x,y = meltIndex[0], meltIndex[1]
        graph[x][y] = max(0,graph[x][y] - meltingHeight[x][y])#최소 0이므로(음수가 나오면 안된다.)
    meltingYear += 1 

    visited = [[False] * m for _ in range(n)]
    iceberg = 0 # 빙산의 덩어리
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                bfs(i,j)
                iceberg += 1
                if iceberg>=2:# 2덩어리 이상 나오면
                    print(meltingYear)#빙산이 분리되는 최초의 시간(년) print
                    sys.exit()