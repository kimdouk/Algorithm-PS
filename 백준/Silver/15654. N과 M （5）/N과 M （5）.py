n, m = map(int,input().split())
result = []
data = sorted(list(map(int,input().split())))
def dfs():
    if len(result) ==m:
        print(*result)
        return
    for i in data:
        if i not in result:
            result.append(i)
            dfs()
            result.pop()
dfs()