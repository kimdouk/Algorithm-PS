input = __import__('sys').stdin.readline
n = int(input())
data = [0] + list(map(int,input().split()))
for i in range(1,n+1):
    data[i]+=data[i-1]
for _ in range(int(input())):
    a,b = map(int,input().split())
    print(data[b]-data[a-1])