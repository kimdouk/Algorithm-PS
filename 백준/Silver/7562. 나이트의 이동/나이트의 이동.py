from collections import deque

def bfs(startX,startY,endX,endY):
    queue = deque([(startX, startY)])
    graph[startX][startY] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:continue
            if graph[nx][ny] == -1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[endX][endY]# 나이트가 이동하려고 하는 칸으로 가기위한 최소이동 회수 반환

t = int(input()) #테스트케이스 개수
dx = [1,1,2,2,-1,-1,-2,-2]#나이트의 이동경로 좌표
dy = [-2,2,-1,1,-2,2,-1,1]
for i in range(t):
    n = int(input())
    graph = [[-1] * n for _ in range(n)] #모두 -1로 설정
    startX, startY = map(int,input().split())#나이트가 현재 있는 칸의 좌표
    endX, endY = map(int,input().split())#나이트가 이동하려고 하는 칸의 좌표
    print(bfs(startX,startY,endX,endY))#파라미터 4개