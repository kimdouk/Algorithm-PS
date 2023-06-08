n = int(input())
number = list(map(int,input().split()))
mx = max(number)
score = [0 for _ in range(mx+1)]
check = [False for _ in range(mx+1)]
for i in number:
    check[i] = True
for i in sorted(number):
    for j in range(i+i,mx+1,i):
        if check[j]:
            score[i]+=1
            score[j]-=1
for i in number:
    print(score[i],end=' ')
