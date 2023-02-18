import sys
input = sys.stdin.readline
n = int(input())
data = sorted([int(input()) for _ in range(n)], reverse = True)
result = 0
for i in range(n-2):
    if data[i]<data[i+1]+data[i+2]:
        result = sum(data[i:i+3])
        break
print(result if result!=0 else -1)