n,m=map(int,input().split())
result = []
def dfs(idx):
    if len(result) == m:
        print(*result)
        return
    for i in range(idx,n+1):
        result.append(i)
        dfs(i)
        result.pop()
dfs(1)