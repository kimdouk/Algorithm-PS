import sys
input = sys.stdin.readline
n, m = map(int,input().split())
data = [int(input()) for _ in range(n)]
data.sort()
end = 0
mn = sys.maxsize
for start in range(n):
    while end<n and data[end] - data[start] < m:end += 1
    if end==n:break
    mn = min(mn,data[end] - data[start])
print(mn)