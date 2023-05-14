from collections import deque

def bfs(x,y):
    visited[x][y] = True
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        z = total -x-y
        if x==y==z:
            return 1
        for a,b in (x,y),(x,z),(y,z):
            if a==b:continue
            a,b = min(a,b),max(a,b)
            na,nc = min(a+a,b-a,total-(a+a)-(b-a)),max(a+a,b-a,total-(a+a)-(b-a))
            if not visited[na][nc]:
                visited[na][nc] = True
                q.append((na,nc))
    return 0

a,b,c = sorted(list(map(int,input().split())))
total = a+b+c
visited = [[False]*(total+1) for _ in range(total+1)]
print(0 if total%3 else bfs(a,c))
