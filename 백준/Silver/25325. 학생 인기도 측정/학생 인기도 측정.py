n = int(input())
names = list(input().split())
cnt = dict()
for name in names:
    cnt[name] = 0
for _ in range(n):
    names = list(input().split())
    for name in names:
        cnt[name]+=1
result = sorted(list(cnt.items()), key=lambda x:(-x[1],x[0]))
for name,cnt in result:
    print(name,cnt)