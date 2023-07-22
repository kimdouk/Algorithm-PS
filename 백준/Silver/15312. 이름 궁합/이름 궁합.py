a = input()
b = input()
name = []
cnt = [3,2,1,2,3,3,2,3,3,2,2,1,2,2,1,2,2,2,1,2,1,1,1,2,2,1]
for i in range(len(a)):
    name.append(cnt[ord(a[i])-65])
    name.append(cnt[ord(b[i])-65])
for i in range(len(name)-2):
    for j in range(len(name)-1-i):
        name[j] = name[j]+name[j+1]
print(str(name[0])[-1]+str(name[1])[-1])