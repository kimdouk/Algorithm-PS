a,b = input().split()
result = float('inf')
for i in range(len(b)-len(a)+1):
    newb = b[i:i+len(a)]
    partResult = 0
    for j in range(len(a)):
        if a[j]!=newb[j]:
            partResult+=1
    result = min(result,partResult)
print(result)