n, m = map(int,input().split())
array = []

def dfs():
    if len(array) == m:
        print(*array)
        return
    for i in range(1,n+1):
            array.append(i)
            dfs()
            array.pop()
dfs()