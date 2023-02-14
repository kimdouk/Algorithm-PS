n, m = map(int,input().split())
data = list(map(int,input().split()))
array = []
data.sort()
visited = [False] * n
def dfs():
    if len(array) == m:
        print(*array)
        return
    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != data[i]:
            visited[i] = True
            array.append(data[i])
            overlap = data[i]
            dfs()
            visited[i] = False
            array.pop()
dfs()