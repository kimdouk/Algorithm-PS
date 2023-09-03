input = __import__('sys').stdin.readline
n,k = map(int,input().split())
data = input()
visited = [False for _ in range(n)]
cnt = 0
for i in range(n):
    if data[i] =='P':
        for j in range(i-k,i+k+1):
            if j<0 or j>=n:continue
            if data[j] =='H' and not visited[j]:
                visited[j] = True
                cnt+=1
                break
print(cnt)