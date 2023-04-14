import sys
input = sys.stdin.readline

n,m = map(int,input().split())
INF = float('inf')
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:graph[i][j] = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
k = int(input())
city = list(map(int,input().split()))
result = []
for b in range(1,n+1):
    mx = 0
    for a in city:
        mx = max(mx,graph[a][b] + graph[b][a])
    result.append(mx)
minVal = min(result)
for i in range(len(result)):
    if result[i] == minVal:
        print(i+1,end=' ')
