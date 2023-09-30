from collections import defaultdict
for _ in range(int(input())):
    data = input()
    k = int(input())
    cnt = defaultdict(list)
    mn,mx = float('inf'), -float('inf')
    flag = False
    for i in range(len(data)):
        cnt[data[i]].append(i)
    for key,v in cnt.items():
        if len(v)>=k:
            flag = True
            for j in range(len(v)-k+1):
                mn = min(mn,v[j+k-1]-v[j]+1)
                mx = max(mx,v[j+k-1]-v[j]+1)
    if not flag:print(-1)
    else:print(mn,mx)