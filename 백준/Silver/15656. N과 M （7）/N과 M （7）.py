n,m = map(int,input().split())
data = sorted(list(map(int,input().split())))
result = []
def dfs():
    if len(result) ==m:
        print(' '.join(map(str,result)))
        return
    for i in data:
        result.append(i)
        dfs()
        result.pop()
dfs()