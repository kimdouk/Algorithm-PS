import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(11)]
result = 0
for _ in range(n):
    a,b = map(int,input().split())
    graph[a].append(b)
for i in graph:
    if len(i)>=2:
        for j in range(len(i)-1):
            if i[j] != i[j+1]:
                result +=1
print(result)