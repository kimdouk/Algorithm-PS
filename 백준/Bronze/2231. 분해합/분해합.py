n = int(input())
result = []
for i in range(n+1):
    s = 0
    for j in str(i):
        s+=int(j)
    if n-s == i:
        result.append(i)
print(min(result) if len(result)!=0 else 0)