n = int(input())
liquids = list(map(int,input().split()))
left,right = 0,n-1
result = liquids[left] + liquids[right]
liquid_sum_min = abs(result)
while left<right:
    liquid_sum = liquids[left] + liquids[right]
    if liquid_sum ==0:
        result = liquid_sum
        break
    if abs(liquid_sum) < liquid_sum_min:
        liquid_sum_min = abs(liquid_sum)
        result = liquid_sum
    if liquid_sum<0:left+=1
    elif liquid_sum>0:right-=1
print(result)