input = __import__('sys').stdin.readline
n = int(input())
xy = sorted([list(map(int,input().split())) for _ in range(n)])
for i in xy:print(*i)