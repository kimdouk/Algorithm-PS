input = __import__('sys').stdin.readline
n,m = map(int,input().split())
data = list(map(int,input().split()))
prefix_sum = 0
mod = [0 for _ in range(m)]
for num in data:
    prefix_sum+=num
    mod[prefix_sum%m]+=1
result = mod[0]    
for num in mod:
    result += (num*(num-1))//2
print(result)