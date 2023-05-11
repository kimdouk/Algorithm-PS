import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n,k = map(int,input().split())
    delay = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)] #진입차수
    dp = [0 for _ in range(n+1)] # index 건물까지 짓는데 소요되는시간
    for _ in range(k):
        a,b = map(int,input().split())
        graph[a].append(b)
        indegree[b] +=1
    ans = int(input())
    
    q = deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
            dp[i] = delay[i]
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i]-=1
            dp[i] = max(dp[i], dp[now] + delay[i])
            if indegree[i]==0:
                q.append(i)
    print(dp[ans])