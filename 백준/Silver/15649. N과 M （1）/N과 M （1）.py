n, m = map(int,input().split())
visit = [0]*(n+1)
array = []

def dfs(step):
    if step == m:
        # print(' '.join(map(str,array)))
        print(*array)
        return
    for i in range(1,n+1):
        if not visit[i]:
            visit[i] = 1
            array.append(i)
            dfs(step+1)
            visit[i] = 0
            array.pop()
dfs(0)