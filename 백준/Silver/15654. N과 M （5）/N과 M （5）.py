n,m=map(int,input().split())
data = [0]+sorted(list(map(int,input().split())))
result = []
visited = [False] * (max(data)+1)
def dfs():
    if len(result) ==m:
        print(*result)
        return
    for i in range(1,n+1):
        if not visited[data[i]]:
            visited[data[i]] = True
            result.append(data[i])
            dfs()
            result.pop()
            visited[data[i]] = False
dfs()