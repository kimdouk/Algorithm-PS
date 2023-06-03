n,l = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
result = 0

def possible(line):
    check = [False for _ in range(n)]
    for i in range(n-1):
        if abs(line[i]-line[i+1])>1:return False
        if line[i]==line[i+1]:continue
        if line[i]<line[i+1]:
            if i+1-l<0:return False
            for k in range(i+1-l,i+1):
                if check[k] or line[k]!=line[i]:
                    return False
                if line[k]==line[i]:
                    check[k]=True

        elif line[i]>line[i+1]:
            if i+l+1>n:return False
            for k in range(i+1,i+l+1):
                if check[k] or line[k]!=line[i+1]:
                    return False
                if line[k]==line[i+1]:
                    check[k] = True
    return True

for i in graph:
    if possible(i):
        result+=1
for j in range(n):
    a = [graph[i][j] for i in range(n)]
    if possible(a):
        result+=1

print(result)