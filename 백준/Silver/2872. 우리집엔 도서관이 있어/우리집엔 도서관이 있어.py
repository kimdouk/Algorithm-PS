input = __import__('sys').stdin.readline
n = int(input())
data = [int(input()) for _ in range(n)]
cnt = 0
for i in data[::-1]:
    if i==n:n-=1
    else:cnt+=1
print(cnt)