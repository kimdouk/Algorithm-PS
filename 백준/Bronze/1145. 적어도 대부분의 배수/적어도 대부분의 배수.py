nums = list(map(int,input().split()))
ans = min(nums)
while True:
    cnt = 0
    for num in nums:
        if ans % num ==0:
            cnt+=1
    if cnt>=3:break
    ans+=1
print(ans)