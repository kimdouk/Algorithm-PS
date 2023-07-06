from math import ceil
n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())
cnt = 0
for i in range(n):
    if a[i]-b<=0:
        a[i]=0
    else:
        a[i]-=b
    cnt+=1
for num in a:
    cnt+=(ceil(num/c))
print(cnt)