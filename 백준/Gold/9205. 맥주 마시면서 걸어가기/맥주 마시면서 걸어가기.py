import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
def bfs(start,end):
    queue = deque([(start,end)])
    visited[0] = True
    while queue:
        x,y = queue.popleft()
        if abs(festival[0] - x)+abs(festival[1]-y)<=1000:
            return "happy"
        for i in range(n):
            if not visited[i+1]:
                if abs(market[i][0] - x) +abs(market[i][1]-y)<=1000:
                    visited[i+1] = True
                    queue.append((market[i][0], market[i][1]))
    return "sad"

for _ in range(t):
    n = int(input())
    home = list(map(int,input().split()))
    market = [list(map(int,input().split())) for _ in range(n)]
    festival = list(map(int,input().split()))
    visited = [False]*(n+1)
    result = bfs(home[0],home[1])
    print(result)