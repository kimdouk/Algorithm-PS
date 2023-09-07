import bisect
n,m,p = map(int,input().split())
score = []
if n!=0:score = list(map(int,input().split()))
if n==p and score[-1]>=m:print(-1)
else:
    score.append(m)
    score.sort(reverse=True)
    ans = 0
    for s in score:
        ans+=1
        if s==m:
            print(ans)
            break