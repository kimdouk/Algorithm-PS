input = __import__('sys').stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n)]
result = []

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    global flag
    visited[x] = True
    result.append(x)

    if len(result)>=5:
        flag = 1
        return

    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            visited[i] = False
            result.pop()
flag = 0
for i in range(n):
    dfs(i)
    if flag:break
    visited[i] = False
    result.pop()
print(flag)