n,m,x,y,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dirs = list(map(int,input().split()))
dice = [0] * 7
dx = [0,0,-1,1] # 동서북남
dy = [1,-1,0,0]

while dirs:
    direction = dirs.pop(0)
    nx,ny = x + dx[direction-1], y + dy[direction-1]
    if nx < 0 or ny<0 or nx>=n or ny>=m:continue
    a,b,c,d,e,f = dice[1],dice[2],dice[3],dice[4],dice[5],dice[6]

    if direction == 1:#동
        dice[6],dice[4],dice[1],dice[3] = c,f,d,a
    elif direction ==2:#서
        dice[6],dice[4],dice[1],dice[3] = d,a,c,f
    elif direction ==3:#북
        dice[1],dice[5],dice[6],dice[2] = b,a,e,f
    elif direction ==4:#남
        dice[1],dice[5],dice[6],dice[2] = e,f,b,a

    if graph[nx][ny] ==0:
        graph[nx][ny] = dice[6]
    else:
        dice[6] = graph[nx][ny]
        graph[nx][ny] = 0
    x,y = nx,ny
    print(dice[1])