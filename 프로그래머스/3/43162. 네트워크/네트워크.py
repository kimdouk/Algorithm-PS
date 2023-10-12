from collections import deque
def solution(n, computers):
    visited = [False for _ in range(n)]
    def bfs(x):
        visited[x] = True
        q = deque([x])
        while q:
            x = q.popleft()
            for i in range(len(computers[x])):
                if not visited[i] and computers[x][i]:
                    q.append(i)
                    visited[i] = True
    cnt = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt+=1
    return cnt