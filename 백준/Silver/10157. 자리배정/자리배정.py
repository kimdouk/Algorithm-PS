m,n = map(int,input().split())
target = int(input())
graph = [[0]*(n+1) for _ in range(m)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
x,y = 0,0
flag =0
while True:
    #종료조건 세우기, 
    for i in range(4):
        if i ==0:
            if graph[x+dx[i]][y+dy[i]]!=0:
                flag = 1
                break   
            for _ in range(n):
                nx,ny = x+dx[i], y+dy[i]
                graph[nx][ny] = graph[x][y]+1
                x,y = nx,ny

        if i==1:
            if graph[x+dx[i]][y+dy[i]]!=0:
                flag = 1
                break   
            for _ in range(m-1):
                nx,ny = x+dx[i],y+dy[i]
                graph[nx][ny] = graph[x][y] + 1
                x,y = nx,ny

        if i==2:
            if graph[x+dx[i]][y+dy[i]]!=0:
                flag = 1
                break   
            for _ in range(n-1):
                nx,ny = x+dx[i],y+dy[i]
                graph[nx][ny] = graph[x][y] + 1
                x,y = nx,ny

        if i==3:
            if graph[x+dx[i]][y+dy[i]]!=0:
                flag = 1
                break   
            for _ in range(m-2):
                nx,ny = x+dx[i],y+dy[i]        
                graph[nx][ny] = graph[x][y] + 1
                x,y = nx,ny

    if flag == 1:
        break
        
    n-=2
    m-=2

result = []
for i in range(len(graph)):
    if target in graph[i]:
        result.append(i+1)
        result.append(graph[i].index(target))
print(' '.join(map(str,result)) if len(result)!=0 else 0)