n, m = map(int,input().split())
data = sorted(list(map(int,input().split())))
temp_result, result = [],[]
def dfs(idx):
    if len(temp_result) ==m:
        result.append(tuple(temp_result))
        return
    for i in range(idx,n):
        temp_result.append(data[i])
        dfs(i+1)
        temp_result.pop()
dfs(0)
for i in sorted(set(result)):
    print(*i)