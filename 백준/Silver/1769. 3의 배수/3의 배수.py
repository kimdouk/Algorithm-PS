n = list(map(int,input()))
cnt = 0
while True:
    if len(n)<2:
        break
    n = list(map(int,str(sum(n))))
    cnt+=1
print(cnt)
print('YES' if sum(n)%3==0 else 'NO')