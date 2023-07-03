def dragon(x,y,d,g):
    direction = [d]

    for i in range(g):
        for j in range(len(direction)-1,-1,-1):
            direction.append((direction[j]+1)%4)
    
    for i in direction:
        x += move[i][0]
        y += move[i][1]
        graph[x][y] = 1

move = [(1,0),(0,-1),(-1,0),(0,1)]
graph = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(int(input())):
    x,y,d,g = map(int,input().split())
    graph[x][y] = 1
    dragon(x,y,d,g)
    
result = 0
for i in range(100):
    for j in range(100):
        if graph[i][j]==1 and graph[i][j+1] == 1 and graph[i+1][j]==1 and graph[i+1][j+1]:
            result+=1
print(result)