n, m = map(int,input().split())
data = sorted(list(map(int,input().split())))
temp_result, result = [],[]
def dfs():
    if len(temp_result) == m:
        result.append(tuple(temp_result))
        return
    for i in range(n):
        temp_result.append(data[i])
        dfs()
        temp_result.pop()
dfs()
for i in sorted(set(result)):
    print(*i)