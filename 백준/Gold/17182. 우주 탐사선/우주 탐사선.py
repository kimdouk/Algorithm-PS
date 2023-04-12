from itertools import permutations
import sys
input = sys.stdin.readline

n,ana = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

number = [i for i in range(n) if i!=ana]
result = float('inf')
for move in list(permutations(number,n-1)):
    total = 0
    for i in range(len(move)-1):
        total += graph[move[i]][move[i+1]]
    total +=graph[ana][move[0]]
    result = min(total, result)
print(result)