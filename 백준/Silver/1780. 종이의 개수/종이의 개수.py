__import__('sys').stdin.readline
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
result = [0,0,0]
def dfs(x,y,t):
    for i in range(x,x+t):
        for j in range(y,y+t):
            if graph[x][y]!=graph[i][j]:
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*(t//3), y+l*(t//3), t//3)
                return

    if graph[x][y]==-1:result[0]+=1
    elif graph[x][y]==0:result[1]+=1
    else:result[2]+=1

dfs(0,0,n)
print(*result,sep='\n')