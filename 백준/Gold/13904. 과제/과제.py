n = int(input())
data = []
for _ in range(n):
    a,b = list(map(int,input().split()))
    data.append((a,b))
result = 0
data.sort()
tmp = []
for i in range(n,0,-1):
    while data and data[-1][0]>=i:
        tmp.append(data.pop()[1])
    if tmp:
        tmp.sort()
        result+=tmp.pop()
print(result)