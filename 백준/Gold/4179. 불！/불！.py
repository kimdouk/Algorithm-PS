from collections import deque
import sys
input = sys.stdin.readline

def bfs(start,jx,jy):
    fire_q, jihoon_q = deque(),deque()
    for x,y in start:
        fire_q.append((x,y))
    jihoon_q.append((jx,jy))

    while fire_q:
        x,y = fire_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=r or ny>=c:continue
            if graph[nx][ny] !='#' and not F_visited[nx][ny]:
                F_visited[nx][ny] = F_visited[x][y] + 1
                fire_q.append((nx,ny))

    while jihoon_q:
        x,y = jihoon_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=r or ny>=c:
                return J_visited[x][y] +1
            if graph[nx][ny] =='.' and not J_visited[nx][ny]:
                if not F_visited[nx][ny] or J_visited[x][y] + 1 < F_visited[nx][ny]:
                    J_visited[nx][ny] = J_visited[x][y] + 1
                    jihoon_q.append((nx,ny))
    return 'IMPOSSIBLE'

r,c = map(int,input().split())
graph = [input().rstrip() for _ in range(r)]
F_visited = [[0]*(c) for _ in range(r)]
J_visited = [[0]*(c) for _ in range(r)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
start = []

for i in range(r):
    for j in range(c):
        if graph[i][j] =='J':jx,jy = i,j
        elif graph[i][j] =='F':start.append((i,j))
print(bfs(start, jx, jy))