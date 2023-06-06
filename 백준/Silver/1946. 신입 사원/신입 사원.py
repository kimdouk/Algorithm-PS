import sys
input = sys.stdin.readline
for _ in range(int(input())):
    ranking = []
    for _ in range(int(input())):
        a,b = map(int,input().split())
        ranking.append((a,b))
    ranking.sort(key=lambda x:x[0])
    st1,st2 = ranking[0][0],ranking[0][1]
    cnt = 1
    for a,b in ranking[1:]:
        if st2>b:
            st1,st2 = a,b
            cnt+=1
    print(cnt)