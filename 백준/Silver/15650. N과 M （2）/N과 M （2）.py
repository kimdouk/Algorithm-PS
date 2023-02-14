n, m = map(int,input().split())
array = []

def dfs(idx):
    if len(array) == m:
        # print(' '.join(map(str,array)))
        print(*array)
        return
    for i in range(idx,n+1):
        if i not in array:
            array.append(i)
            dfs(i+1)
            array.pop()
dfs(1)