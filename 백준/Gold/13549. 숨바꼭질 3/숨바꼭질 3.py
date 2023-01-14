from collections import deque

def bfs():
    queue = deque([n])# or queue.append(n)
    check[n] = 0
    while queue:
        x = queue.popleft()
        for i in (x-1, x+1, 2*x):
            nx = i
            if 0<=nx<=100000 and check[nx] == -1:
                if nx == 2*x: #순간이동인 경우 appendleft이용,먼저 모든 순간이동 경우를 0으로 만듬
                    queue.appendleft(nx)
                    check[nx] = check[x]
                else: #순간이동 다 갱신 이후 걸어서 가는 경우
                    queue.append(nx)
                    check[nx] = check[x] + 1

n, k = map(int,input().split())
check = [-1] * 100001 # -1로 초기화하여 visited필요 x, 순간이동으로 방문했지만 0이여서 재방문할 필요x
bfs()
print(check[k])