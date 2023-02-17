def dfs(v,visited,graph):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i,visited,graph)
t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    data = [0] + list(map(int,input().split()))
    visited = [False] *(n+1)
    for i in range(1,n+1):
        graph[i].append(data[i])
    
    result = 0
    for i in range(1,n+1):
        if not visited[i]:
            dfs(i,visited,graph)
            result+=1
    print(result)