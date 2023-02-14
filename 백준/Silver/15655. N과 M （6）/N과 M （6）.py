n,m=map(int,input().split())
data = sorted(list(map(int,input().split())))
result = []
def dfs(idx):
    if len(result) == m:
        print(*result)
        return
    for i in data[idx:]:
            result.append(i)
            dfs(data.index(i)+1)
            result.pop()
dfs(0)