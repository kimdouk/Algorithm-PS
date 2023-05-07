n = int(input())
num1 = int(input())
data = [int(input()) for _ in range(n-1)]
data.sort(reverse=True)
result = 0
if n==1:print(0)
else:
    while data[0]>=num1:
        data[0]-=1
        num1+=1
        result+=1
        data.sort(reverse=True)
    print(result)