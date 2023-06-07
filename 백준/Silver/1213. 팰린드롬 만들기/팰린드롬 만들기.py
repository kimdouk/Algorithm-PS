from collections import defaultdict
name = input()
alpha = defaultdict(int)
for i in name:
    alpha[i]+=1
cnt = 0
palin=''
mid = ''
alpha = dict(sorted(alpha.items(), key=lambda x:x[0]))
for a,b in alpha.items():
    if b%2:
        cnt+=1
        mid = a
if cnt>1:
    print("I'm Sorry Hansoo")
else:
    for a,b in alpha.items():
        palin+=(b//2)*a
    print(palin+mid+palin[::-1])