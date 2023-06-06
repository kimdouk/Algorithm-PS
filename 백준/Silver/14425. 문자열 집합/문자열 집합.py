n,m = map(int,input().split())
alphaSet = {}
result =0
for _ in range(n):
    string = input()
    alphaSet[string]=0
for _ in range(m):
    alpha = input()
    if alpha in alphaSet:
        result +=1
print(result)