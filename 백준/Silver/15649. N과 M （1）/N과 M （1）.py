n, m = map(int,input().split())
result = []
visited = [False] * (n+1)
def dfs():
    if len(result) == m:
        print(*result)
        return
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs()
            result.pop()
            visited[i] = False
dfs()