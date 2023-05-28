import sys
n = int(input())
h = sorted(list(map(int,input().split())))
ans = float('inf')
for i in range(n):
    for j in range(i+3,n):
        left,right = i+1,j-1
        while left<right:
            temp = (h[left] + h[right]) - (h[i] + h[j])
            if abs(ans) > abs(temp):
                ans = abs(temp)
            if temp>0:right-=1
            else : left+=1
print(ans)