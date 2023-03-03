from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[-1] * 101 for _ in range(101)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for r in rectangle:
        x1,y1,x2,y2 = 2*r[0],2*r[1],2*r[2],2*r[3]
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2:
                    graph[i][j] = 0
                elif graph[i][j] !=0:
                    graph[i][j] = 1
    
    queue = deque([(2*characterX, 2*characterY)])
    graph[2*characterX][2*characterY] = 0
    while queue:
        x,y = queue.popleft()
        if x==2*itemX and y==2*itemY:
            return (graph[x][y]//2)
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=101 or ny>=101:continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                
                    