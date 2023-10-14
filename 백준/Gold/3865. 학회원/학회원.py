from collections import defaultdict
input = __import__('sys').stdin.readline
def dfs(st):
    global result
    for i in data[st]:
        if not visited[i]:
            visited[i]+=1
            if data[i]:
                dfs(i)
            else:result.append(i)
    return

while True:
    n = int(input())
    if n==0:break
    data = defaultdict(list)
    visited = defaultdict(int)
    result = []
    for _ in range(n):
        a,b = input().split(':')
        data[a]=b[:-2].split(',')
    dfs(list(data)[0])
    print(len(result))