n = int(input())
cnt = 0
for a in range(2,n-1,2):
    x = n-a
    for c in range(1,x):
        if c>=(x-c)+2:
            cnt+=1
print(cnt)