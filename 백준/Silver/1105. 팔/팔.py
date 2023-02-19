l, r = input().split()
result = 0
if len(l) == len(r):
    for i in range(len(l)):
        if (l[i] == r[i]) and l[i]=='8':
            result+=1
        elif l[i]!=r[i]:
            break
    print(result)
else:print(0)