from bisect import bisect_left
input = __import__('sys').stdin.readline
n,h = map(int,input().split())
odd,even = [],[]
for i in range(n):
    num = int(input())
    if i%2==0:odd.append(num)
    else:even.append(h-num)
even.sort()
odd.sort()
result = []

for std in range(1,h+1):
    cnt = 0
    cnt+=(len(odd)-bisect_left(odd,std))
    cnt+=bisect_left(even,std)
    result.append(cnt)
ans = sorted(result)[0]
print(ans,result.count(ans))