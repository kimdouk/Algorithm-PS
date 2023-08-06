input = __import__('sys').stdin.readline
n,k = map(int,input().split())
data = [0] + (list(map(int,input().split())))*2
mx = 0
for i in range(1,2*n+1):
    data[i] +=data[i-1]
for i in range(k,2*n+1):
    mx = max(mx,data[i]-data[i-k])
print(mx)