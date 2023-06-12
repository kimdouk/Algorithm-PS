import string
s = input()
cnt = {}
for i in string.ascii_lowercase:
    cnt[i]=0
for char in s:
    cnt[char]+=1
print(*cnt.values())