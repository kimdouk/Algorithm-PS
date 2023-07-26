n,k,a,b = map(int,input().split())
date = [k for _ in range(n)]
cnt = 0
while True:
    date.sort()
    if date[0]<=0:break
    for i in range(a):
        date[i]+=b
    for j in range(n):
        date[j]-=1
    cnt+=1
print(cnt)