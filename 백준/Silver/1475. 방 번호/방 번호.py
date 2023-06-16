from math import ceil
n = input()
cnt = [0 for i in range(10)]
data = []
for i in n:
    if i=='6':data.append(9)
    else:data.append(int(i))
for i in data:
    cnt[int(i)]+=1
print(max(cnt) if cnt.index(max(cnt))!=9 else ceil(max(cnt)/2))