n, m = map(int,input().split())
result = []
visited = [False] * (n+1)
def dfs(idx):
    if len(result) ==m:
        print(*result)
        return
    for i in range(idx,n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(i+1)
            result.pop()
            visited[i] = False
dfs(1)