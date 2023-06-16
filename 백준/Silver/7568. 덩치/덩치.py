data, result = [],[]
for _ in range(int(input())):
    a,b = map(int,input().split())
    data.append((a,b))
for x,y in data:
    cnt =1
    for p,q in data:
        if x<p and y<q:
            cnt+=1
    result.append(cnt)
print(*result)