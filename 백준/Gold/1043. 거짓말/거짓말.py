input = __import__('sys').stdin.readline
n,m = map(int,input().split())
people = list(map(int,input().split()))[1:]
graph = [[] for _ in range(n+1)]
last = []
result = 0
for _ in range(m):
    data = list(map(int,input().split()))
    last.append(data[1:])
    for i in range(1,len(data)):
        for j in range(1,len(data)):
            if i!=j:graph[data[i]].append(data[j])
            

know = set()
def dfs(x):
    know.add(x)
    for i in graph[x]:
        if i not in know:
            dfs(i)

for i in people:
    dfs(i)
for i in last:
    flag = 0
    for j in i:
        if j in know:
            flag = 1
            break
    if not flag:
        result+=1
print(result)