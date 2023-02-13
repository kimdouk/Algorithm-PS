n = int(input())
numbers = sorted(list(map(int,input().split())))
result = 0
for i in reversed(range(n)):
    target = numbers[i]
    tmp_numbers = numbers[:i]+numbers[i+1:]
    left,right = 0,len(tmp_numbers)-1
    while left<right:
        goodNum = tmp_numbers[left] + tmp_numbers[right]
        if goodNum == target:
            result+=1
            break
        elif goodNum < target:left+=1
        else:right-=1
print(result)