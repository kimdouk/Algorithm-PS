from collections import deque
input = __import__('sys').stdin.readline
n = int(input())
time = [0 for _ in range(n+1)]
result = [0 for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
def topology():
    q = deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
            result[i] = time[i]
    while q:
        x = q.popleft()
        for i in graph[x]:
            indegree[i]-=1
            result[i] = max(result[i], result[x]+time[i])
            if indegree[i]==0:
                q.append(i)

graph = [[] for _ in range(n+1)]
for i in range(n):
    data = list(map(int,input().split()))
    time[i+1] = data[0]
    indegree[i+1]+=(len(data)-2)
    for j in range(1,len(data)-1):
        graph[data[j]].append(i+1)
topology()
print(*result[1:], sep='\n')