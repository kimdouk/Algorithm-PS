import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

n = int(input())
m = int(input())
INF = float('inf')
graph = [[INF]*(n+1) for _ in range(n+1)]
path = [[0]*(n+1) for _ in range(n+1)]

def trace(i,j):
    if path[i][j] ==0:
        return []
    k = path[i][j]
    return trace(i,k) + [k] + trace(k,j)

#graph 입력
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b], c) #주의
#같은노드 = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:graph[i][j] = 0
#i->k,k->j 더 짧으면 갱신 및 경로 k기록
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] >graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = k

#graph출력
for i in range(1,n+1):
    for j in range(1,n+1):
        print(0 if graph[i][j] == INF else graph[i][j], end = ' ')
    print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == 0 or graph[i][j]==INF:
            print(0)
            continue
        result = [i] + trace(i,j) + [j]
        print(len(result),*result, end = '\n')