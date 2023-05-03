import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
result = []
INF = float('inf')
ans = 0
for i in range(n):
    for j in range(n):
        temp = INF
        for k in range(n):
            if k==i or k==j or i==j:continue
            temp = min(temp, graph[i][k] + graph[k][j])
        if graph[i][j] <temp and i!=j:
            result.append((i,j))
        elif graph[i][j]>temp:
            ans = -1
if ans!=-1:
    for i,j in result:
        ans += graph[i][j]
    ans = ans//2
print(ans)