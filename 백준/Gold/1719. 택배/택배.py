input = __import__('sys').stdin.readline
n,m = map(int,input().split())
INF = float('inf')
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
result = [[i for i in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]
                result[i][j] = result[i][k]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:result[i][j] = '-'
        print(result[i][j],end=' ')
    print()