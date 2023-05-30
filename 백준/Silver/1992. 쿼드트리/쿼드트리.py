n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
result = []
def dfs(x,y,n):
    global result
    check = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=graph[i][j]:
                result.append('(')
                n//=2
                dfs(x,y,n)
                dfs(x,y+n,n)
                dfs(x+n,y,n)
                dfs(x+n,y+n,n)
                result.append(')')
                return
    result.append(check)


dfs(0,0,n)
print(''.join(map(str,result)))