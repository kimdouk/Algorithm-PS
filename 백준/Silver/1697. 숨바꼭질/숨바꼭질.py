#1차원에서의 BFS
from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        x = queue.popleft()
        for i in (x+1, x-1, 2*x): # 1차원 공간
            nx = i
            if 0 <= nx <= 100000 and not check[nx]: #check[nx] == 0 #범위 안에 있고, 방문한적이없을때
                check[nx] = check[x] + 1
                queue.append(nx)
n, k = map(int,input().split())
check = [0] * 100001 # 0<= <=100000
if n != k: bfs(n) 
# 주의 : n,k같으면 0이지만 bfs돌리면 0이라서 방문안한줄알고 방문해버린다.
#아니면 visited를 따로 만들던가 하자
print(check[k])